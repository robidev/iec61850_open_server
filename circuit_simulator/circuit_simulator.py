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

from PySpice.Probe.Plot import plot
import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Spice.NgSpice.Shared import NgSpiceShared



circuit = """
.title substation model
* substation components
#.options interp  ; strongly reduces memory requirements
.save none       ; ensure only last step is kept each iteration
.tran 19us 3600s uic; run for an hour max, with 100 samples per cycle (201u stepsize does not distort, 200 does...)
"""

example = """
* example substation description
*xIFL            v_220_4/3  v_220_5/1/2  v_220_6  IFL vss=220000
*xCTR1           v_220_4/3  v_220_5/1/2  v_220_6  v_220_7  v_220_8  v_220_9  CTR
*xPTR            v_220_7  v_220_8  v_220_9  v_132_1  v_132_2  v_132_3  PTR
*xCBR            v_132_1  v_132_2  v_132_3  v_132_4  v_132_5  v_132_6  CBR
*xVTR2           v_132_4, v_132_5, v_132_6                             VTR
*xCTR2           v_132_4  v_132_5  v_132_6  v_132_7  v_132_8  v_132_9  CTR
*xDIS            v_132_7  v_132_8  v_132_9  v_132_10 v_132_11 v_132_12 DIS
*xload           v_132_10 v_132_11 v_132_12 load rload=5500
"""


PORT = 65000

logger = Logging.setup_logging(logging_level=0)

measurantsV = {}
measurantsA = {}
actuators = {}
simulation_nodes = {}

scd_schema = xmlschema.XMLSchema("../schema/SCL.xsd")
scl = scd_schema.to_dict("../open_substation.scd")
#pprint.pprint(scl)


# process LNode in substation section, attach relevant LD/LN data, and initiate a tcp connection to the ied
# lnode can be attached at each level of the substation
def LNode(item, levelRef, SubEquipment):
  lItem = None
  if 'LNode' in item:
    lItem = item
  elif SubEquipment is not None and 'LNode' in SubEquipment:
    lItem = SubEquipment
  else:
    return

  for LNode in lItem['LNode']:
    print("    LNode:" + levelRef + " > " + LNode['@iedName'] + " class:" + LNode["@lnClass"]) 
    IP = getIEDIp(LNode['@iedName'])
    LNref = LNode['@iedName'] + LNode['@ldInst'] + "/" + LNode['@prefix'] + LNode['@lnClass'] + LNode['@lnInst']
    
    if LNode["@lnClass"] == "TCTR":
      #register ref for TCTR-IED
      phase = SubEquipment["@phase"].lower()
      if phase == 'a' or phase == 'b' or phase == 'c':
        measurantsA["v.x" + levelRef.lower() + "_ctr.vctr" + phase] = { 
          'Name' : LNode['@iedName'], 
          'IP' : IP, 
          'LNref' : LNref,
          'Connection' : init_conn(IP, LNref) } 

        print("v.x" + levelRef.lower() + "_ctr.vctr" + phase)
    if LNode["@lnClass"] == "TVTR" and "Terminal" in item:
      #register ref for TCTR-IED
      measurantsV[ item["Terminal"][0]["@connectivityNode"].lower() + "_" + SubEquipment["@phase"].lower() ] = { 
        'Name' : LNode['@iedName'], 
        'IP' : IP, 
        'LNref' : LNref,
        'Connection' : init_conn(IP, LNref) } 

      print(item["Terminal"][0]["@connectivityNode"].lower() + "_" + SubEquipment["@phase"].lower())
    if LNode["@lnClass"] == "XCBR":
      #register ref for XCBR-IED
      actuators["v.x" + levelRef.lower() + "_cbr.vsig"] = { 
        'Name' : LNode['@iedName'], 
        'IP' : IP, 
        'LNref' : LNref,
        'Connection' : init_conn(IP, LNref) } 

      print("v.x" + levelRef.lower() + "_cbr.vsig")
    if LNode["@lnClass"] == "XSWI":
      #register ref for XSWI-IED
      actuators["v.x" + levelRef.lower() + "_dis.vsig"] = { 
        'Name' : LNode['@iedName'], 
        'IP' : IP, 
        'LNref' : LNref,
        'Connection' : init_conn(IP, LNref) } 
      print("v.x" + levelRef.lower() + "_dis.vsig")


def init_conn(IP, LNref):
  conn = None
  return None
  try:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.settimeout(1.0)
    #conn.connect(("127.0.0.1", PORT)) 
    conn.connect((IP, PORT))
    conn.sendall(b'i ' + LNref.encode('utf-8') + b'\n')
    data = conn.recv(1024)
    if data == b'OK\n':
      print("OK")
      return conn
  except:
    print("ERROR: could not connect")
  
  conn.close()
  print("not OK")
  return None


# retrieve ip from SCL based on IED name
def getIEDIp(ied):
  global scl
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
def PowerTransformer(item, levelRef):
  spice_model = ""
  if 'PowerTransformer' in item:
      for Powertransformer in item['PowerTransformer']:
        print(" Powertransformer:" + levelRef + "_" + Powertransformer["@name"])
        LNode(Powertransformer, levelRef + "_" + Powertransformer["@name"], None)

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

  return spice_model


# parse conductingequipment, and generate spice model entries
def ConductingEquipment(item, levelRef, Voltagelevel):
  spice_model = ""
  if "ConductingEquipment" in item:
    for ConductingEquipment in item["ConductingEquipment"]:
      Cond_fullRef = levelRef + "_" + ConductingEquipment["@name"]
      type = ConductingEquipment["@type"]

      print("  ConductingEquipment:" + Cond_fullRef + " type:" + type)
      LNode(ConductingEquipment, Cond_fullRef, None)

      if "SubEquipment" in ConductingEquipment:
        for SubEquipment in ConductingEquipment["SubEquipment"]:
          Sub_fullRef = Cond_fullRef + "_" + SubEquipment["@phase"]
          print("   SubEquipment:" + Sub_fullRef + " name: " + SubEquipment["@name"] )
          LNode(ConductingEquipment, Cond_fullRef, SubEquipment)

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
      spice_model += checkoptions(type, Voltagelevel)
      spice_model += "\n"

      if type == "IFL":
        simulation_nodes[Cond_fullRef] = {
          "device" : "x" + Cond_fullRef + "_" + type,
          "type" : type,
        }

  return spice_model

# add spice model options
def checkoptions(type, Voltagelevel):
  option = ""
  if type == "IFL":
    if "Voltage" in Voltagelevel:
      option = "vss=" + str(Voltagelevel["Voltage"]['$']) + Voltagelevel["Voltage"]['@multiplier']
  return option


def updateValue(ied, value):
  # send value
  #initiate tcp, if not existing yet, or do this at init, and just get it here
  #send value to ied
  # "s LNref val"
  if ied['Connection'] == None:
    return -1
  try:
    ied['Connection'].sendall(b's ' + ied['LNref'].encode('utf-8') + b' ' + str(int(value*100)).encode('utf-8') )
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


def getValue(ied):
  # request value
  #initiate tcp, if not existing yet, or do this at init, and just get it here
  #retrieve value from ied
  # val = "g LNref"
  if ied['Connection'] == None:
    return 1

  try:
    ied['Connection'].sendall(b'g ' + ied['LNref'].encode('utf-8') )
    data = ied['Connection'].recv(1024)
    if data[-1:] == b'\n':
      return float(data[0:-1].decode("utf-8"))
  except:
    print("ERROR: exception while requesting value, closing connection")
    try:
      ied['Connection'].close()
    except:
      print("ERROR: could not close connection after error")
    ied['Connection'] = None
  return 1

def nextStep(ied_conn):
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


dont_add_commands = False
command_que = []

#que_commands("alter @r.xs12_e1_w1_bb1_load.r1[r]=0")
#que_commands("alter @r.xs12_e1_w1_bb1_load.r1[r]=1000000000")
# each ConnectivityNode can have a fault/load attached
# if the substation model in the scl indicates a fault/load element, it can be referenced: "@r.x" + s12_e1_w1_bb1 + "_load.r1[r]"

def que_commands(command):
  global dont_add_commands
  global command_que
  while dont_add_commands == True:
    time.sleep(0.001)
  dont_add_commands = True

  command_que.append(command)
  dont_add_commands = False
  

def execute_commands(ngspice_shared):
  global dont_add_commands
  global command_que
  while dont_add_commands == True:
    time.sleep(0.001)
  dont_add_commands = True

  for key in command_que:
    print(ngspice_shared.exec_command(command_que[key]))

  command_que.clear()
  dont_add_commands = False

class MyNgSpiceShared(NgSpiceShared):
    def __init__(self, ngspice_id=0, send_data=False):
        super(MyNgSpiceShared, self).__init__(ngspice_id, send_data)
        #self._logger = logger

    def get_vsrc_data(self, voltage, time, node, ngspice_id):
        #self._logger.debug('ngspice_id-{} get_vsrc_data @{} node {}'.format(ngspice_id, time, node))
        #TODO: provide voltage based on switch/cbr position
        #print(node)
        if node in actuators:
          # get position data from actuators[node], by retrieving the status over tcp(or buffered)
          if getValue(actuators[node]) > 0:
            voltage[0] = 10 #circuitbreaker is closed
          else:
            voltage[0] = -10 #circuitbreaker is open
        return 0


#generalequipment is ignored, as they are not part of the spice simulation
#function elements are ignored,as they are not part of the primary process
spice = ""

directory = r'./models/'
for entry in os.scandir(directory):
    if entry.path.endswith(".subckt") and entry.is_file():
      f = open(entry.path, "r")
      if f.mode == 'r':
        spice += f.read()
        spice += "*\n"


if "Substation" in scl:
  for substation in scl["Substation"]:
    sub_name = substation["@name"]
    print("--- Substation:" + sub_name + " ---")
    LNode(substation, sub_name, None)
    spice += PowerTransformer(substation, sub_name)

    if 'VoltageLevel' in substation:
      for Voltagelevel in substation['VoltageLevel']:
        vlvl_name = Voltagelevel["@name"]
        vlvl_fullRef = sub_name + "_" + vlvl_name
        print("Voltagelevel:" + vlvl_fullRef)

        LNode(Voltagelevel, vlvl_fullRef, None)
        spice += PowerTransformer(Voltagelevel, vlvl_fullRef)

        if 'Bay' in Voltagelevel:
          for Bay in Voltagelevel['Bay']:
            Bay_name = Bay["@name"]
            Bay_fullRef = vlvl_fullRef + "_" + Bay_name
            print(" Bay:" + Bay_fullRef)

            LNode(Bay, Bay_fullRef, None)
            spice += ConductingEquipment(Bay, Bay_fullRef, Voltagelevel)

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
                    spice += spice_model
                    simulation_nodes[ConnectivityNode["@pathName"]] = {
                      "device" : "x" + Bay_fullRef + "_" + ConnectivityNode["@name"] + "_" + type,
                      "type" : type,
                    }


circuit += spice + ".end\n"

print("--- model ---")
print(spice)
print("---")


ngspice_shared = MyNgSpiceShared(send_data=False)
ngspice_shared.load_circuit(circuit)

ngspice_shared.step(2)

arrA = {}
arrV = {}

# generate list for unique connections, as to identify when the command for next step/iteration in the simulation can be given
# all threats in the simulated IED-process will wait until the next-step command, so that the simulation is synced with the IED's
nextStep_dict = {}

for key in measurantsA:
  if measurantsA[key]['Connection'] != None:
    ip = measurantsA[key]['IP']
    if ip not in nextStep_dict:
      nextStep_dict[ip] = measurantsA[key]['Connection']

for key in measurantsV:
  if measurantsV[key]['Connection'] != None:
    ip = measurantsV[key]['IP']
    if ip not in nextStep_dict:
      nextStep_dict[ip] = measurantsV[key]['Connection']

#print(ngspice_shared.exec_command("print @r.xs12_e1_w1_bb1_load.r1[r]"))

# run the simulation
for _ in range(200):
  ngspice_shared.step(10)
  analysis = ngspice_shared.plot(plot_name='tran1', simulation=None).to_analysis()
  #TODO: send values back to the merging units
  for key in measurantsA:
    #print(key)
    if not key in arrA:
      arrA[key] = numpy.array([])
    arrA[key] = numpy.append(arrA[key], float(analysis.branches[key][0]))
    updateValue(measurantsA[key], float(analysis[key][0]))

  for key in measurantsV:
    #print(key)
    if not key in arrV:
      arrV[key] = numpy.array([])
    arrV[key] = numpy.append(arrV[key], float(analysis[key][0]))
    updateValue(measurantsV[key], float(analysis[key][0]))

  # sync primary-process simulation with simulated ied's
  for key in nextStep_dict:
    #print("next step for ip: " + key)
    nextStep(nextStep_dict[key])
    #break # during tests

  execute_commands(ngspice_shared)
  
  #arr1 = numpy.append(arr1, float(analysis['S12/D1/Q1/L0_a'][0]))
  #arr2 = numpy.append(arr2, float(analysis['S12/E1/Q1/L2_b'][0]))
  #arr3 = numpy.append(arr3, float(analysis['S12/E1/W1/BB1_a'][0]))
  #v.xs12_e1_q1_i1_ctr.vctra
  #v.xs12_d1_q1_i1_ctr.vctra
  #print(analysis.nodes)
  

pprint.pprint(simulation_nodes)
print(ngspice_shared.plot_names)

figure = plt.figure(1, (20, 10))
axe = plt.subplot(111)
plt.title('')
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')
plt.grid()

for key in arrA:
  plt.plot(arrA[key])
for key in arrV:
  plt.plot(arrV[key])

plt.legend(('I1', 'I2', 'I3','V1'), loc=(.05,.1))

plt.tight_layout()
plt.show()
