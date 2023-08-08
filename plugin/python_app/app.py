#import sys
#sys.path.insert(0, '/usr/lib/python3/dist-packages')
#sys.path.insert(0, '/usr/local/lib/python3.10/dist-packages')
#sys.path.insert(0, '/home/user/.local/lib/python3.10/site-packages')
#sys.path.insert(0, '/usr/lib/python3.10/lib-dynload')
#sys.path.insert(0, '/usr/lib/python3.10')
#sys.path.insert(0, '/usr/lib/python310.zip')

import ctypes
import python_plugin
import lib61850

def main(server_instance):
    #srv = python_plugin.castOpenServerInstance(server_instance) # convert the server instance to the right type
    #mms_pos = python_plugin.getDataRefFromModel(srv,"IED1_XCBRGenericIO/XCBR1.Pos.stVal")

    #pos = ctypes.cast(mms_pos,ctypes.POINTER(lib61850.struct_sMmsValue ) )
    #print("position value: ", str(lib61850.MmsValue_getBitStringAsInteger(pos)) )

    return 0

