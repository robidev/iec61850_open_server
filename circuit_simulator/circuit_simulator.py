#!/usr/bin/env python3
# export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
#
# this python program will simulate the primary process using PySpice with the ngspice library interactively
# it takes input from the SCL, and generates the circuit based on the substation-section using assumed values and an ideal model 
# allthough this ideal model does not behave (yet) like a real substation, it is good enough for simple protection use-cases
# the simulator can be influenced with values from the breakers and switches, and can feed the calculated voltage and current
# back to the merging-units, creating a closed loop process simulation
#

import os
import numpy
import pprint
import matplotlib.pyplot as plt
import xmlschema
import socket
import time
import sys
import math

from PySpice.Probe.Plot import plot
import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Spice.NgSpice.Shared import NgSpiceShared

PORT = 65000 #port for connecting the simulation with the IED's 

# process LNode in substation section, attach relevant LD/LN data, and initiate a tcp connection to the ied
# lnode can be attached at each level of the substation
def _LNode(item, levelRef, SubEquipment,scl):
  #list of items that should be measured during simulation
  measurantsV = {}
  measurantsA = {}
  #list of items that can be switched during simulation
  actuators = {}

  lItem = None
  if 'LNode' in item:
    lItem = item
  elif SubEquipment is not None and 'LNode' in SubEquipment:
    lItem = SubEquipment
  else:
    return measurantsA, measurantsV, actuators

  for LNode in lItem['LNode']:
    print("    LNode:" + levelRef + " > " + LNode['@iedName'] + " class:" + LNode["@lnClass"]) 
    IP = _getIEDIp(LNode['@iedName'],scl)
    LNref = LNode['@iedName'] + LNode['@ldInst'] + "/" + LNode['@prefix'] + LNode['@lnClass'] + LNode['@lnInst']
    
    if LNode["@lnClass"] == "TCTR":
      #register ref for TCTR-IED
      phase = SubEquipment["@phase"].lower()
      if phase == 'a' or phase == 'b' or phase == 'c':
        measurantsA["v.x" + levelRef.lower() + "_ctr.vctr" + phase] = { 
          'Name' : LNode['@iedName'], 
          'IP' : IP, 
          'LNref' : LNref,
          'Connection' : _init_conn(IP, LNref) } 

        print("v.x" + levelRef.lower() + "_ctr.vctr" + phase)
    if LNode["@lnClass"] == "TVTR" and "Terminal" in item:
      #register ref for TCTR-IED
      measurantsV[ item["Terminal"][0]["@connectivityNode"].lower() + "_" + SubEquipment["@phase"].lower() ] = { 
        'Name' : LNode['@iedName'], 
        'IP' : IP, 
        'LNref' : LNref,
        'Connection' : _init_conn(IP, LNref) } 

      print(item["Terminal"][0]["@connectivityNode"].lower() + "_" + SubEquipment["@phase"].lower())
    if LNode["@lnClass"] == "XCBR":
      #register ref for XCBR-IED
      actuators["v.x" + levelRef.lower() + "_cbr.vsig"] = { 
        'Name' : LNode['@iedName'], 
        'IP' : IP, 
        'LNref' : LNref,
        'Connection' : _init_conn(IP, LNref) } 

      print("v.x" + levelRef.lower() + "_cbr.vsig")
    if LNode["@lnClass"] == "XSWI":
      #register ref for XSWI-IED
      actuators["v.x" + levelRef.lower() + "_dis.vsig"] = { 
        'Name' : LNode['@iedName'], 
        'IP' : IP, 
        'LNref' : LNref,
        'Connection' : _init_conn(IP, LNref) } 
      print("v.x" + levelRef.lower() + "_dis.vsig")
  return measurantsA, measurantsV, actuators


def _init_conn(IP, LNref):
  conn = None
  #if IP != "10.0.0.0":
  #  return None
  try:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.settimeout(1.0)
    #conn.connect(("10.0.0.4", PORT)) 
    conn.connect((IP, PORT))
    print("connecting to: %s:%i" % (IP,PORT))

    conn.sendall(b'i ' + LNref.encode('utf-8') + b'\n')
    data = conn.recv(1024)
    if data == b'OK\n':
      print("connected to: %s:%i" % (IP,PORT))
      return conn
  except:
    print("ERROR: could not connect: %s:%i, oh no!" % (IP,PORT))
  
  conn.close()
  print("not OK")
  return None


# retrieve ip from SCL based on IED name
def _getIEDIp(ied,scl):
  if 'Communication' in scl and 'SubNetwork' in scl['Communication']:
    for SubNetwork in scl["Communication"]['SubNetwork']:
      if 'ConnectedAP' in SubNetwork:
        for ConnectedAP in SubNetwork['ConnectedAP']:
          if ied == ConnectedAP['@iedName']:
            for P in ConnectedAP['Address']['P']:
              if P['@type'] == 'IP':
                return P['$']
  return "NONE"


# process powertransformer substation item and generate spice model entry
def _PowerTransformer(item, levelRef,scl):
  measurantsV = {}
  measurantsA = {}
  #list of items that can be switched during simulation
  actuators = {}

  spice_model = ""
  if 'PowerTransformer' in item:
      for Powertransformer in item['PowerTransformer']:
        print(" Powertransformer:" + levelRef + "_" + Powertransformer["@name"])
        A,V,M = _LNode(Powertransformer, levelRef + "_" + Powertransformer["@name"], None,scl)
        measurantsA.update(A)
        measurantsV.update(V)
        actuators.update(M)

        spice_model += "x" + levelRef + "_" + Powertransformer["@name"] + " "

        if 'TransformerWinding' in Powertransformer:
          for TransformerWinding in Powertransformer['TransformerWinding']:
            if "Terminal" in TransformerWinding:
              for Terminal in TransformerWinding["Terminal"]:
                t = Terminal["@connectivityNode"]
                spice_model += t + "_a " 
                spice_model += t + "_b " 
                spice_model += t + "_c " 

        spice_model += "PTR\n"

  return measurantsA, measurantsV, actuators, spice_model


# parse conductingequipment, and generate spice model entries
def _ConductingEquipment(item, levelRef, Voltagelevel,scl):
  measurantsV = {}
  measurantsA = {}
  #list of items that can be switched during simulation
  actuators = {}

  simulation_nodes = {}

  spice_model = ""
  if "ConductingEquipment" in item:
    for ConductingEquipment in item["ConductingEquipment"]:
      Cond_fullRef = levelRef + "_" + ConductingEquipment["@name"]
      type = ConductingEquipment["@type"]

      print("  ConductingEquipment:" + Cond_fullRef + " type:" + type)
      A,V,M = _LNode(ConductingEquipment, Cond_fullRef, None,scl)
      measurantsA.update(A)
      measurantsV.update(V)
      actuators.update(M)

      if "SubEquipment" in ConductingEquipment:
        for SubEquipment in ConductingEquipment["SubEquipment"]:
          Sub_fullRef = Cond_fullRef + "_" + SubEquipment["@phase"]
          print("   SubEquipment:" + Sub_fullRef + " name: " + SubEquipment["@name"] )
          A,V,M = _LNode(ConductingEquipment, Cond_fullRef, SubEquipment,scl)
          measurantsA.update(A)
          measurantsV.update(V)
          actuators.update(M)

      if "Terminal" in ConductingEquipment:
        for Terminal in ConductingEquipment["Terminal"]:
          print("   Terminal:" + Terminal["@connectivityNode"])

      #generate the spice model element
      spice_model += "x" + Cond_fullRef + "_" + type + " "

      if "Terminal" in ConductingEquipment:
        for Terminal in ConductingEquipment["Terminal"]:
          t = Terminal["@connectivityNode"]
          spice_model += t + "_a " 
          spice_model += t + "_b " 
          spice_model += t + "_c " 

      spice_model += type + " "
      spice_model += _checkoptions(type, Voltagelevel)
      spice_model += "\n"

      if type == "IFL":
        simulation_nodes[Cond_fullRef] = {
          "device" : "x" + Cond_fullRef + "_" + type,
          "type" : type,
        }

  return measurantsA, measurantsV, actuators, spice_model, simulation_nodes

# add spice model options
def _checkoptions(type, Voltagelevel):
  option = ""
  if type == "IFL":
    if "Voltage" in Voltagelevel:
      volt = int(float(Voltagelevel["Voltage"]['$'])*math.sqrt(2))
      option = "vss=" + str(volt) + Voltagelevel["Voltage"]['@multiplier']
      #print("++++ IFL:" + option)
  return option


def _parse_substation(scl):
  #list of items that should be measured during simulation
  measurantsV = {}
  measurantsA = {}
  #list of items that can be switched during simulation
  actuators = {}
  # netlist of substation
  netlist = ""
  #parameters that can be altered during simulation
  simulation_nodes = {} # 

  #parse the substation section of the scd, and build the netlist using its components
  if "Substation" in scl:
    for substation in scl["Substation"]:
      sub_name = substation["@name"]
      print("--- Substation:" + sub_name + " ---")
      A,V,M = _LNode(substation, sub_name, None,scl)
      measurantsA.update(A)
      measurantsV.update(V)
      actuators.update(M)

      A,V,M,s = _PowerTransformer(substation, sub_name,scl)
      netlist += s
      measurantsA.update(A)
      measurantsV.update(V)
      actuators.update(M)

      if 'VoltageLevel' in substation:
        for Voltagelevel in substation['VoltageLevel']:
          vlvl_name = Voltagelevel["@name"]
          vlvl_fullRef = sub_name + "_" + vlvl_name
          print("Voltagelevel:" + vlvl_fullRef)

          A,V,M = _LNode(Voltagelevel, vlvl_fullRef, None,scl)
          measurantsA.update(A)
          measurantsV.update(V)
          actuators.update(M)

          A,V,M,s = _PowerTransformer(Voltagelevel, vlvl_fullRef,scl)
          netlist += s
          measurantsA.update(A)
          measurantsV.update(V)
          actuators.update(M)

          if 'Bay' in Voltagelevel:
            for Bay in Voltagelevel['Bay']:
              Bay_name = Bay["@name"]
              Bay_fullRef = vlvl_fullRef + "_" + Bay_name
              print(" Bay:" + Bay_fullRef)

              A,V,M = _LNode(Bay, Bay_fullRef, None,scl)
              measurantsA.update(A)
              measurantsV.update(V)
              actuators.update(M)

              A,V,M,s,n = _ConductingEquipment(Bay, Bay_fullRef, Voltagelevel,scl)
              measurantsA.update(A)
              measurantsV.update(V)
              actuators.update(M)
              netlist += s
              simulation_nodes.update(n)

              if 'ConnectivityNode' in Bay:
                for ConnectivityNode in Bay['ConnectivityNode']:
                  print("  ConnectivityNode:" + Bay_fullRef + "_" + ConnectivityNode["@name"])
                  # allow for definition of additional elements in substation section to help the simulation
                  if "Private" in ConnectivityNode:
                    for Private in ConnectivityNode['Private']:
                      type = Private['@type']
                      arguments = Private['$']

                      spice_model = "x" + Bay_fullRef + "_" + ConnectivityNode["@name"] + "_" + type + " "
                      spice_model += ConnectivityNode["@pathName"] + "_a " 
                      spice_model += ConnectivityNode["@pathName"] + "_b " 
                      spice_model += ConnectivityNode["@pathName"] + "_c " 
                      spice_model += type + " "
                      spice_model += arguments + "\n"
                      netlist += spice_model
                      simulation_nodes[ConnectivityNode["@pathName"]] = {
                        "device" : "x" + Bay_fullRef + "_" + ConnectivityNode["@name"] + "_" + type,
                        "type" : type,
                      }

  return measurantsA, measurantsV, actuators, netlist, simulation_nodes


def _updateValue(ied, value):
  # send value
  #initiate tcp, if not existing yet, or do this at init, and just get it here
  #send value to ied
  # "s LNref val"
  if ied['Connection'] == None:
    return -1
  try:
    ied['Connection'].sendall(b's ' + ied['LNref'].encode('utf-8') + b' ' + str(int(value)).encode('utf-8') + b'\n')
    #print(b"->" + b's ' + ied['LNref'].encode('utf-8') + b' ' + str(int(value*100)).encode('utf-8') )
    data = ied['Connection'].recv(1024)
    if data == b'OK\n':
      return 0
  except:
    print("ERROR: exception while updating value, closing connection")
    try:
      ied['Connection'].close()
    except:
      print("ERROR: could not close connection after error")
    ied['Connection'] = None
  return -1


def _getValue(ied):
  # request value
  #initiate tcp, if not existing yet, or do this at init, and just get it here
  #retrieve value from ied
  # val = "g LNref"
  if ied['Connection'] == None:
    return 1

  try:
    ied['Connection'].sendall(b'g ' + ied['LNref'].encode('utf-8') + b'\n')
    data = ied['Connection'].recv(1024)
    if data[-1:] == b'\n':
      #print("ret: %s: %s" % (ied['LNref'].encode('utf-8') , data[0:-1].decode("utf-8")))
      return float(data[0:-1].decode("utf-8"))
  except:
    print("ERROR: exception while requesting value, closing connection")
    try:
      ied['Connection'].close()
    except:
      print("ERROR: could not close connection after error")
    ied['Connection'] = None
  return 1


def _nextStep(ied_conn):
  # send value
  #initiate tcp, if not existing yet, or do this at init, and just get it here
  #send value to ied
  # "s LNref val"
  if ied_conn == None:
    return -1
  try:
    ied_conn.sendall(b'n step')
    data = ied_conn.recv(1024)
    if data == b'OK\n':
      return 0
  except:
    print("ERROR: exception while updating step, closing connection")
    try:
      ied_conn.close()
    except:
      print("ERROR: could not close connection after error")
    ied_conn = None
  return -1


class _sclNgSpiceShared(NgSpiceShared):
    def __init__(self, actuators, logger = None, ngspice_id=0, send_data=False):
        super(_sclNgSpiceShared, self).__init__(ngspice_id, send_data)
        self.actuators = actuators
        self.actuatorCache = {}
        for node in self.actuators:
          self.actuatorCache[node] = _getValue(self.actuators[node])

        if logger != None:
          self._logger = logger

    def get_vsrc_data(self, voltage, time, node, ngspice_id):
        self._logger.debug('ngspice_id-{} get_vsrc_data @{} node {}'.format(ngspice_id, time, node))
        #provide voltage based on switch/cbr position
        if node in self.actuators:
          # get position data from actuators[node], by retrieving the status over tcp(or buffered)
          #if _getValue(self.actuators[node]) > 0:
          if self.actuatorCache[node] > 0:
            voltage[0] = 10 #circuitbreaker is closed
          else:
            voltage[0] = -10 #circuitbreaker is open
        return 0


#####################################################################
class circuit_simulator():
  def __init__(self, scl_file, scl_schema_file, logger = None):
    if logger == None:
      logger = Logging.setup_logging(logging_level=20)
    self.logger = logger
    
    logger.info("init simulation")

    self._dont_add_commands = False #semaphore for commands during simulation
    self._command_que = [] # list for commands during simulation

    self.scl_schema_file = scl_schema_file
    self.scd_schema = None
    self.scl_file = scl_file
    self.scl = None

    self.measurantsA = {}
    self.measurantsV = {}
    self.actuators = {}
    self.circuit = ""
    self.simulation_nodes = {}

    self.arrA = {} # list of simulated amperes during simulation
    self.arrV = {} # list of simulated voltages during simulation
    self.nextStep_dict = {} #list of IED's that need a nextstep signal during simulation

    if os.path.exists('static/plot.png'):
      os.remove('static/plot.png') 
    #general simulation options, these should not be altered during simulation
    self.title = ".title substation model"
    self.options = "#.options interp  ; strongly reduces memory requirements"
    self.save = ".save none       ; ensure only last step is kept each iteration"
    #values: 19 us, 25 us, 250us
    self.tran = ".tran 19us 3600s uic; run for an hour max, with 100 samples per cycle (201u stepsize does not distort, 200 does...)"

    self.ngspice_shared = None

    self.init_simulator()


  def init_simulator(self):
    self.scd_schema = xmlschema.XMLSchema(self.scl_schema_file)
    self.scl = self.scd_schema.to_dict(self.scl_file)

    if self.scl is None:
      self.logger.error("could not parse SCL")
      return

    #generalequipment is ignored, as they are not part of the spice simulation
    #function elements are ignored,as they are not part of the primary process
    spice = ""

    #load all subcircuit models in subdir models. by using the name of components in the substation section, they can be correctly matched
    directory = r'./models/'
    for entry in os.scandir(directory):
        if entry.path.endswith(".subckt") and entry.is_file():
          f = open(entry.path, "r")
          if f.mode == 'r':
            spice += f.read()
            spice += "*\n"
    
    if spice == "":
      self.logger.error("Could not load spice models")
      return

    measurantsA,measurantsV,actuators,netlist,simulation_nodes = _parse_substation(self.scl)

    if netlist == "":
      self.logger.error("Could not build netlist from SCL")
      return

    spice += netlist

    #build the complete netlist

    circuit = self.title + "\n"
    circuit += self.options + "\n"
    circuit += self.save + "\n"
    circuit += self.tran + "\n"
    circuit += spice 
    circuit += ".end\n"

    self.measurantsA = measurantsA
    self.measurantsV = measurantsV
    self.actuators = actuators
    self.circuit = circuit
    self.simulation_nodes = simulation_nodes

    if self.ngspice_shared != None:
      self.ngspice_shared.destroy()
    else:
      self.ngspice_shared = _sclNgSpiceShared(self.actuators, send_data=False) # create the shared ngspice object, that supports callbacks for interactive voltage-sources(actuators)


    self.ngspice_shared.load_circuit(self.circuit) # load the netlist
    self.ngspice_shared.step(2) #needed to initialise simulation

    #generate dict of alterable elements
    listing = self.ngspice_shared.exec_command("listing deck expand").splitlines()

    for sn in simulation_nodes:
      for l in listing:
        if simulation_nodes[sn]['device'].lower() in l:
          ref = l.split(' ')[0]
          if not 'elements' in simulation_nodes[sn]:
            simulation_nodes[sn]['elements'] = []
          if ref[0:1] == 'r':
            simulation_nodes[sn]['elements'].append("@" + ref + "[r]")
          if ref[0:1] == 'v':
            simulation_nodes[sn]['elements'].append("@" + ref + "[acmag]")

    # generate list for unique connections, as to identify when the command for next step/iteration in the simulation can be given
    # all threats in the simulated IED-process will wait until the next-step command, so that the simulation is synced with the IED's
    for key in measurantsA:
      if measurantsA[key]['Connection'] != None:
        ip = measurantsA[key]['IP']
        if ip not in self.nextStep_dict:
          self.nextStep_dict[ip] = measurantsA[key]['Connection']

    for key in measurantsV:
      if measurantsV[key]['Connection'] != None:
        ip = measurantsV[key]['IP']
        if ip not in self.nextStep_dict:
          self.nextStep_dict[ip] = measurantsV[key]['Connection']

    for key in actuators:
      if actuators[key]['Connection'] != None:
        ip = actuators[key]['IP']
        if ip not in self.nextStep_dict:
          self.nextStep_dict[ip] = actuators[key]['Connection']

  def run_simulation(self, steps = 10, steps_range = 200):
    # run the simulation
    for _ in range(steps_range):
      self.simulation_step(steps)


  def simulation_step(self,steps = 10):
    self.ngspice_shared.step(steps) # perform simulation steps
    analysis = self.ngspice_shared.plot(plot_name='tran1', simulation=None).to_analysis() # perform an analysis step
    #send values back to the merging units
    for key in self.measurantsA:
      # send value to IED
      _updateValue(self.measurantsA[key], float(analysis[key][0])) 
      # store data for plot
      if not key in self.arrA:
        self.arrA[key] = numpy.array([])
      self.arrA[key] = numpy.append(self.arrA[key], float(analysis.branches[key][0]))

    for key in self.measurantsV:
      # send value to IED
      _updateValue(self.measurantsV[key], float(analysis[key][0])) 
      # store data for plot
      if not key in self.arrV:
        self.arrV[key] = numpy.array([])
      self.arrV[key] = numpy.append(self.arrV[key], float(analysis[key][0]))

    for node in self.actuators:
      # get value from IED
      self.ngspice_shared.actuatorCache[node] = _getValue(self.actuators[node])

    # sync primary-process simulation with simulated ied's
    for key in self.nextStep_dict:
      self.logger.debug("next step for ip: " + key)
      _nextStep(self.nextStep_dict[key])

    self.execute_commands()


  def plot_simulation(self, sel = 3):
    ### Simulation end ###
    self.logger.info(self.ngspice_shared.plot_names)
    plt.close('all')
    # draw graph of resulting data
    figure = plt.figure(1, (4.5, 2.5))
    axe = plt.subplot(111)
    #plt.title('')
    #plt.xlabel('Time [s]')
    #plt.ylabel('Voltage [V]')
    plt.grid()
    

    if sel & 0x01:
      for key in self.arrA:
        plt.plot(self.arrA[key])
    if sel & 0x02:
      for key in self.arrV:
        plt.plot(self.arrV[key])

    #plt.legend(('1', '2', '3'), loc=(.05,.1))

    plt.tight_layout()

    if os.path.exists('static/plot.png'):
      os.remove('static/plot.png') 
    plt.savefig('static/plot.png')
    #plt.show()


  def clear_plot(self):
    self.logger.info("clearing plots")
    self.arrA.clear()
    self.arrV.clear()
    if os.path.exists('static/plot.png'):
      os.remove('static/plot.png') 


  # this can be used to print part values during simulation
  def simulation_node(self, node):
    return(self.ngspice_shared.exec_command("print " + node))


    # this is called to alter parts during simulation
  def execute_commands(self):
    while self._dont_add_commands == True:
      time.sleep(0.001)
    self._dont_add_commands = True

    for i in range(len(self._command_que)):
      print(self.ngspice_shared.exec_command(self._command_que[i]))

    self._command_que.clear()
    self._dont_add_commands = False


  # this can be used to alter parts during simulation
  def que_commands(self, command):
    while self._dont_add_commands == True:
      time.sleep(0.001)
    self._dont_add_commands = True

    self._command_que.append(command)
    self._dont_add_commands = False

######################################################################
 

# main
if __name__=="__main__":

  """
  * example substation netlist description
  *xIFL            v_220_4/3  v_220_5/1/2  v_220_6  IFL vss=220000
  *xCTR1           v_220_4/3  v_220_5/1/2  v_220_6  v_220_7  v_220_8  v_220_9  CTR
  *xPTR            v_220_7  v_220_8  v_220_9  v_132_1  v_132_2  v_132_3  PTR
  *xCBR            v_132_1  v_132_2  v_132_3  v_132_4  v_132_5  v_132_6  CBR
  *xVTR2           v_132_4, v_132_5, v_132_6                             VTR
  *xCTR2           v_132_4  v_132_5  v_132_6  v_132_7  v_132_8  v_132_9  CTR
  *xDIS            v_132_7  v_132_8  v_132_9  v_132_10 v_132_11 v_132_12 DIS
  *xload           v_132_10 v_132_11 v_132_12 load rload=5500
  """

  # start main execution
  
  #load the simulation from scl
  sim = circuit_simulator("../scd/open_substation.scd","../schema/SCL.xsd")

  #print("--- model ---")
  #print(sim.circuit)
  #print("---")

  pprint.pprint(sim.simulation_nodes)

  # run the simulation for 1 second simulated time, 50hz, 80 samples per cycle = 4000 samples 
  for _ in range(200):
    sim.simulation_step(10)

  #print(self.ngspice_shared.exec_command("show v.xs12_d1_q1_external_ifl.vphasea"))
  #print(self.ngspice_shared.exec_command("show r.xs12_e1_w1_bb1_load.r1"))
  #print(self.ngspice_shared.exec_command("show r"))
  #print(self.ngspice_shared.exec_command("show v"))
  #print(self.ngspice_shared.exec_command("display"))
  #print(self.ngspice_shared.exec_command("print r.xs12_e1_w1_bb1_load.r3[r]"))
  #sim.simulation_step(100)
  #sim.que_commands("alter @r.xs12_e1_w1_bb1_load.r1[r]=0")
  # each ConnectivityNode can have a fault/load attached
  # if the substation model in the scl indicates a fault/load element, it can be referenced: "@r.x" + s12_e1_w1_bb1 + "_load.r1[r]"

  # draw graph of resulting data
  #sim.plot_simulation(1)

