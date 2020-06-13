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

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.List;

import com.libiec61850.scl.SclParser;
import com.libiec61850.scl.SclParserException;
import com.libiec61850.scl.communication.ConnectedAP;
import com.libiec61850.scl.communication.PhyComAddress;
import com.libiec61850.scl.model.AccessPoint;
import com.libiec61850.scl.model.DataSet;
import com.libiec61850.scl.model.Inputs;
import com.libiec61850.scl.model.ExtRef;
import com.libiec61850.scl.model.FunctionalConstraintData;
import com.libiec61850.scl.model.GSEControl;
import com.libiec61850.scl.model.SampledValueControl;
import com.libiec61850.scl.model.IED;
import com.libiec61850.scl.model.LogicalDevice;
import com.libiec61850.scl.model.LogicalNode;

public class DynamicModelGenerator_input {

    private ConnectedAP connectedAP;
    private IED ied = null;
    
    public DynamicModelGenerator_input(InputStream stream, String icdFile, PrintStream output, String iedName, String accessPointName) 
    		throws SclParserException {

        SclParser sclParser = new SclParser(stream);
        
        if (iedName == null)
        	ied = sclParser.getFirstIed();
        else
        	ied = sclParser.getIedByName(iedName);

        if (ied == null)
            throw new SclParserException("No data model present in SCL file! Exit.");

        AccessPoint accessPoint = null;
        
        if (accessPointName != null)
        	accessPoint = ied.getAccessPointByName(accessPointName);
        else
        	accessPoint = ied.getFirstAccessPoint();

        if (accessPoint == null)
        	throw new SclParserException("No valid access point found!");
        
        this.connectedAP = sclParser.getConnectedAP(ied, accessPoint.getName());
        
        List<LogicalDevice> logicalDevices = accessPoint.getServer().getLogicalDevices();

        output.println("MODEL(" + ied.getName() + "){");
        for (LogicalDevice logicalDevice : logicalDevices) {
            output.print("LD(");
            output.print(logicalDevice.getInst() + "){\n");

            exportLogicalNodes(output, logicalDevice);

            output.println("}");
        }
        printSubscribeDataSets(output, sclParser, accessPointName);
        output.println("}");
    }

    private void exportLogicalNodes(PrintStream output, LogicalDevice logicalDevice) {
        for (LogicalNode logicalNode : logicalDevice.getLogicalNodes()) {
            output.print("LN(" + logicalNode.getName() + "){\n");

            exportLogicalNode(output, logicalNode, logicalDevice);

            output.println("}");
        }
    }
    
    private static String toMmsString(String iecString) {
        return iecString.replace('.', '$');
    }

    private void exportLogicalNode(PrintStream output, LogicalNode logicalNode, LogicalDevice logicalDevice) {
         output.println("CL(" + logicalNode.getLnClass() + ");");

        for (Inputs inputs : logicalNode.getInputs())
            exportInputs(output, inputs, logicalNode);//should be only one

        for (SampledValueControl svCB : logicalNode.getSampledValueControlBlocks()) {
            String svString = "";
            
            String phyCom = "";
            String phyComAddrName="";
            PhyComAddress svAddress = connectedAP.lookupSMVAddress( logicalDevice.getInst(), svCB.getName());                            
            if (svAddress != null) {
                phyCom += svAddress.getVlanPriority() + " ";
                phyCom += svAddress.getVlanId() + " ";
                phyCom += svAddress.getAppId();
                phyComAddrName = "";
                for (int i = 0; i < 6; i++) {
                    phyComAddrName += String.format("%02x", svAddress.getMacAddress()[i]);
                }
            }
            //order: name        svID         dataSet      convRev  smpMod  smpRate  optFlds  isUnicast {prio,id,appid,mac}

            svString += svCB.getName() + " ";
            
            if (svCB.getSmvID() == null)
                svString += ", ";
            else
                svString += svCB.getSmvID() + " ";
            
            if (svCB.getDatSet() != null)
                svString += svCB.getDatSet() + " ";
            else
                svString += ", ";
            
            svString += svCB.getConfRev() + " 0 ";

            svString += svCB.getSmpRate() + " ";

            svString += svCB.getSmvOpts().getIntValue() + " ";
                        
            if (svCB.isMulticast())
                svString += "0";
            else
                svString += "1";
            
            //svString += svCB.getNofASDI();

            output.println("SV(" + svString + "){"); 
            if (svAddress != null)
                output.println("PS(" + phyCom + " " + phyComAddrName + ")");
            else
                output.println("PS(0,0,0,000000000000);");  
             output.println("}"); 
        }

    }

    private void exportInputs(PrintStream output, Inputs inputs, LogicalNode logicalNode) {
        output.print("IN{\n");
        for (ExtRef extRef : inputs.getExtRef()) {

            //TODO: ensure a description with spaces is handled correctly
            output.print("ER(" + extRef.getDesc() + " " + extRef.ExtRefToString() + " " + extRef.getIntAddr() + " " + extRef.getServiceType() + " " + extRef.srcToString() + ");\n");
            
        }
        output.println("}");
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println("Dynamic model generator");

        if (args.length < 1) {
            System.out.println("Usage: genconfig <ICD file> [-ied  <ied-name>] [-ap <access-point-name>] [<output filename>]");
            System.exit(1);
        }

        String icdFile = args[0];

        PrintStream outputStream = System.out;
        
        String accessPointName = null;
        String iedName = null;
        
        if (args.length > 1) {
        	for (int i = 1; i < args.length; i++) {
        		if (args[i].equals("-ap")) {
        			accessPointName = args[i+1];
        			
        			System.out.println("Select access point " + accessPointName);
        			
        			i++;
        		}
        		else if (args[i].equals("-ied")) {
        			iedName = args[i+1];
        			
        			System.out.println("Select IED " + iedName);
        			
        			i++;
        			
        		}
        		else {
        			 outputStream = new PrintStream(new FileOutputStream(new File(args[i])));
        		}
        	}
        	      
        }

        InputStream stream = new FileInputStream(icdFile);

        try {
			new DynamicModelGenerator_input(stream, icdFile, outputStream, iedName, accessPointName);
		} catch (SclParserException e) {
			System.err.println("ERROR: " + e.getMessage());
		}
    }


    private void printSubscribeDataSets(PrintStream output, SclParser sclParser, String accessPointName_local) {
        AccessPoint accessPoint_local;
        //Collection<IED> ieds;

        for (IED ied_local : sclParser.getIeds()){
            accessPoint_local = null;

            if (accessPointName_local == null)
                accessPoint_local = ied_local.getFirstAccessPoint();
            else
                accessPoint_local = ied_local.getAccessPointByName(accessPointName_local);

            ConnectedAP connectedAP_local = sclParser.getConnectedAP(ied_local, accessPoint_local.getName());

            /* create list of data set names */
            for (LogicalDevice logicalDevice : accessPoint_local.getServer().getLogicalDevices()) {

                for (LogicalNode logicalNode : logicalDevice.getLogicalNodes()) {

                    for (DataSet dataSet : logicalNode.getDataSets()) {

                        //String dataSetVariableName = ied_local.getName() + "_ds_" + logicalDevice.getInst() + "_" + logicalNode.getName() + "_" + dataSet.getName();
                        String datasetName_ = dataSet.getName();

                        String AppID = "0";
                        String ethAddr =  "000000000000";
                        String cbRef = "NULL";
                        String ID = "NULL";
                        for (LogicalNode logicalNode2 : logicalDevice.getLogicalNodes()) {
                            List<GSEControl> gseControlBlocks = logicalNode2.getGSEControlBlocks();           
                            for (GSEControl gseControlBlock : gseControlBlocks) {
                                if(datasetName_.equals(gseControlBlock.getDataSet()))
                                {
                                    PhyComAddress gseAddress = connectedAP_local.lookupGSEAddress(logicalDevice.getInst(), gseControlBlock.getName());
                                    if (gseAddress != null) {
                                        AppID = "" + gseAddress.getAppId();

                                        ethAddr = "";
                                        for (int i = 0; i < 6; i++) {
                                            ethAddr += String.format("%02x", gseAddress.getMacAddress()[i]);
                                        }
                                    }
                                    
                                    if (gseControlBlock.getAppID() != null)
                                        ID = gseControlBlock.getAppID();
                                    
                                    cbRef = ied_local.getName() + logicalDevice.getInst() + "/" + logicalNode2.getName() + "$GO$" + gseControlBlock.getName();
                                }
                            }

                            List<SampledValueControl> svControlBlocks = logicalNode2.getSampledValueControlBlocks();                      
                            for (SampledValueControl svCB : svControlBlocks) {
                                if(datasetName_.equals(svCB.getDatSet()))
                                {
                                    PhyComAddress svAddress = connectedAP_local.lookupSMVAddress( logicalDevice.getInst(), svCB.getName());                            
                                    if (svAddress != null) {
                                        AppID = "" + svAddress.getAppId();
                                        
                                        ethAddr = "";
                                        for (int i = 0; i < 6; i++) {
                                            ethAddr += String.format("%02x", svAddress.getMacAddress()[i]);
                                        }
                                    }
                                    
                                    if (svCB.getSmvID() != null)
                                        ID = svCB.getSmvID();

                                    cbRef =  ied_local.getName() + logicalDevice.getInst() + "/" + logicalNode2.getName() + "$SV$" + svCB.getName();
                                }
                            }
                        }

                        for (FunctionalConstraintData fcda : dataSet.getFcda()) {
                            String mmsVariableName = ied_local.getName() + fcda.getLdInstance() + "/";
                            if (fcda.getPrefix() != null)
                                mmsVariableName += fcda.getPrefix();
                            mmsVariableName += fcda.getLnClass();
                            if (fcda.getLnInstance() != null)
                                mmsVariableName += fcda.getLnInstance();
                            //mmsVariableName += "$" + fcda.getFc().toString();
                            mmsVariableName += "." + toMmsString(fcda.getDoName());
                            if (fcda.getDaName() != null)
                                mmsVariableName += "." + toMmsString(fcda.getDaName());

                            output.print("SD(" + mmsVariableName + " " + datasetName_ + " " + AppID + " " + ethAddr + " " + cbRef + " " + ID + ");\n");
            
                        }
                    }
                }
            }
        }
    }

}
