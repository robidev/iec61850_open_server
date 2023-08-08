import ctypes
import python_plugin
import lib61850

def main(server_instance):
    srv = python_plugin.castOpenServerInstance(server_instance) # convert the server instance to the right type

    mms_pos = python_plugin.getDataRefFromModel(srv,"IED1_XCBRGenericIO/XCBR1.Pos.stVal")

    if not mms_pos:
        print("could not find mms_pos")
        return 1
    print("found mms_pos")
    pos = ctypes.cast(mms_pos,ctypes.POINTER(lib61850.struct_sMmsValue ) )
    print("position value: ", str(lib61850.MmsValue_getBitStringAsInteger(pos)) )

    return 0

