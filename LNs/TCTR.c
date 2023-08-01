#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "TCTR.h"

#include <libiec61850/iec61850_server.h>
#include <libiec61850/hal_thread.h>
#include <sys/socket.h> 

typedef void (*processFunction) (int sd, char * buffer, void* param);

typedef struct sTCTR
{
  void *da;
  IedServer server;
  void * da_callback;
} TCTR;


void *TCTR_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues )
{
  TCTR* inst = (TCTR *) malloc(sizeof(TCTR));//create new instance with MALLOC
  inst->server = server;
  inst->da = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Amp.instMag.i");//the node to operate on
  inst->da_callback = _findAttributeValueEx(inst->da, allInputValues);

  return inst;
}
