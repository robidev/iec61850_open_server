# functions to cast data-types
import ctypes, time
# functions for reading/writing the active datamodel
import python_plugin
# functions for working with MmsValue's and such
import lib61850

# note, the extref parameter contains a callback parameter, but it is in a c-struct.
def cb(extref):
    var = ctypes.cast(extref,ctypes.POINTER(python_plugin.InputEntry)).contents # cast the extref struct
    print("PYTHON_APP: callback for '" + var.Ref + "' with argument: " + var.callBackParam)

def main(server_instance):
    # convert the server instance to the right type
    srv = python_plugin.castOpenServerInstance(server_instance) 

    # retrieve an MmsValue* from the datamodel
    mms_pos = python_plugin.getDataRefFromModel(srv,"IED1_XCBRGenericIO/XCBR1.Pos.stVal")

    # check if the MmsValue* could be found
    if not mms_pos:
        print("PYTHON_APP: could not find mms_pos data ref @IED1_XCBRGenericIO/XCBR1.Pos.stVal. quitting...")
        return 1

    print("PYTHON_APP: found mms_pos data ref @IED1_XCBRGenericIO/XCBR1.Pos.stVal")

    # register a callback for when a DA is updated
    #cbRef = python_plugin.callBackFunction(cb)
    #python_plugin.registerDaCallback(srv,"IED1_XCBRGenericIO/XCBR1.Pos.stVal",cbRef,42)

    # cast the type to the correct MmsValue* type for use by libiec61850
    pos = ctypes.cast(mms_pos,ctypes.POINTER(lib61850.struct_sMmsValue ) )

    # use the standard libiec61850 functions to read from the MmsValue* an int value. 
    # Use libiec61850 C documentation to see what functions exist. 
    # Ensure base types(int, bool, float) or MmsValue* is the input/output. 
    # Else you need to cast/convert using ctype library functions (see iec61850_open_client for more complex examples)
    print("PYTHON_APP: position value: ", str(lib61850.MmsValue_getBitStringAsInteger(pos)) )

    # the python plugin can update most basic types, such as bool, bitstring and VisString
    # this will also update GOOSE, SMV and notify extref connected logical nodes if connected via input definitions
    #python_plugin.updateDataRefBitString(srv,"IED1_XCBRGenericIO/XCBR1.Pos.stVal",2)

    # read out the new value. the MmsValue* is a pointer, so it will contain the updated value.
    #print("PYTHON_APP: new position value: ", str(lib61850.MmsValue_getBitStringAsInteger(pos)) )

    ######################################################################################
    # example to dynamically modify simulation values by calling another plugin
    #  time.sleep(10)
    #  lss = python_plugin.load_library("../liblocal_sample_simulation.so")
    #  update_sample_simulation_magnitude = lss.update_sample_simulation_magnitude
    #  update_sample_simulation_magnitude.restype=ctypes.c_int
#  
    #  result = update_sample_simulation_magnitude(ctypes.c_int(2),ctypes.c_double(5.0))
    #  if result:
    #      print("value updated")
    #  else:
    #      print("could not find value")
    #  time.sleep(0.15)
    #  result = update_sample_simulation_magnitude(ctypes.c_int(2),ctypes.c_double(0.2))
    #  if result:
    #      print("value reset")
    #  else:
    #      print("could not find value")
    #######################################################################################
        
    # dont quit the python app if callbacks are registered, or the program will segfault
    while True:
        time.sleep(1)
    return 0

