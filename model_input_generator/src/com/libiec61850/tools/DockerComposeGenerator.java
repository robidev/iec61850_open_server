package com.libiec61850.tools;

/*
 *  DynamicModelGenerator.java
 *
 *  Copyright 2014-2016 Michael Zillgith
 *
 *  This file is part of libIEC61850.
 *
 *  libIEC61850 is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  libIEC61850 is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with libIEC61850.  If not, see <http://www.gnu.org/licenses/>.
 *
 *  See COPYING file for the complete license text.
 */

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.List;
import java.util.Collection;

import java.io.File;
import java.io.FileOutputStream;
import java.net.InetAddress;
import java.net.UnknownHostException;

import com.libiec61850.scl.SclParser;
import com.libiec61850.scl.SclParserException;
import com.libiec61850.scl.communication.ConnectedAP;
import com.libiec61850.scl.communication.SubNetwork;
import com.libiec61850.scl.model.AccessPoint;
import com.libiec61850.scl.model.IED;


public class DockerComposeGenerator {

    public static int convertNetmaskToCIDR(InetAddress netmask){
      byte[] netmaskBytes = netmask.getAddress();
      int cidr = 0;
      boolean zero = false;
      for(byte b : netmaskBytes){
          int mask = 0x80;

          for(int i = 0; i < 8; i++){
              int result = b & mask;
              if(result == 0){
                  zero = true;
              }else if(zero){
                  throw new IllegalArgumentException("Invalid netmask.");
              } else {
                  cidr++;
              }
              mask >>>= 1;
          }
      }
      return cidr;
    }

    public DockerComposeGenerator(InputStream stream, String icdFile, PrintStream output) 
    		throws SclParserException {
        SclParser sclParser = new SclParser(stream);

        Collection<IED> ieds = sclParser.getIeds();

        if(ieds.size() == 0)
          throw new SclParserException("No data model present in SCL file! Exit.");

        output.println("version: \"3.3\"");
         output.println("services:");

        for(IED ied : ieds) {    
          int networks_printed = 0;
          output.println("  " + ied.getName().toLowerCase() + ":");
          output.println("    build:");
          output.println("      context: .");
          output.println("      dockerfile: Dockerfile.libiec61850_server");
          output.println("    hostname: " + ied.getName() );

          //add the model config
          output.println("    command: \"/srv/libiec61850_server eth0 102 /cfg/" + ied.getName() + ".cfg /cfg/" + ied.getName() + ".ext\"");
          
          //add a volume to host the configuration files
          output.println("    volumes:");
          output.println("      - ./cfg:/cfg");

         	List<AccessPoint> accessPoints = ied.getAccessPoints();

          if(accessPoints.size() == 0)
          	throw new SclParserException("No valid access point found!");
          
          for(AccessPoint accessPoint : accessPoints){
            ConnectedAP connectedAP = sclParser.getConnectedAP(ied, accessPoint.getName());

            //find the right subnetwork(s) for this IED, and print them
            for(SubNetwork subNetwork : sclParser.getCommunication().getSubNetworks()){
              for(ConnectedAP subN_connectedAP : subNetwork.getConnectedAPs() ){
                if(subN_connectedAP.getApName() == connectedAP.getApName()){
                  if(networks_printed == 0) {
                    output.println("    networks:");
                    networks_printed = 1;
                  }
                  output.println("      " + subNetwork.getName() + ":");
                  output.println("        ipv4_address: " + connectedAP.getAddress().getAddressParameter("IP").getText());
                }
              }
            }
            output.println("    privileged: true");
            output.println("");
          }
        }
        for(SubNetwork subNetwork : sclParser.getCommunication().getSubNetworks()){
          output.println("networks:");
          output.println("  " + subNetwork.getName() + ":");
          output.println("    driver: bridge");
          output.println("    ipam:");
          output.println("      driver: default");
          output.println("      config:");
          
          try
          {
            InetAddress subnetmask = InetAddress.getByName( subNetwork.getConnectedAPs().get(0).getAddress().getAddressParameter("IP-SUBNET").getText());
            InetAddress gateway = InetAddress.getByName( subNetwork.getConnectedAPs().get(0).getAddress().getAddressParameter("IP-GATEWAY").getText());
            int cidr = convertNetmaskToCIDR(subnetmask);
            byte[] subnet = gateway.getAddress();
            subnet[3] = 0;
            output.println("        - subnet: " + InetAddress.getByAddress(subnet).getHostAddress() + "/" + cidr );
            //output.println("          gateway: " + gateway.getHostAddress() );
          }
          catch(UnknownHostException e)
          {
            output.println("ERROR: could not parse IP-addresses in subnetwork section");
          }
        }
    }




    public static void main(String[] args) throws FileNotFoundException {
        System.out.println("Docker compose generator");

        if (args.length < 1) {
            System.out.println("Usage: gencompose <ICD file> ");
            System.exit(1);
        }

        String icdFile = args[0];

        PrintStream outputStream = System.out;
        
        if(args[1] != null){
          outputStream = new PrintStream(new FileOutputStream(new File(args[1])));
        }
        
        //String accessPointName = null;
        //String iedName = null;
        

        InputStream stream = new FileInputStream(icdFile);

        try {
			new DockerComposeGenerator(stream, icdFile, outputStream);
		} catch (SclParserException e) {
			System.err.println("ERROR: " + e.getMessage());
		}
    }


}
