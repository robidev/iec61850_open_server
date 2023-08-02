#include "TCTR.h"
#include "iec61850_model_extensions.h"

void *TCTR_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  TCTR *inst = (TCTR *)malloc(sizeof(TCTR)); // create new instance with MALLOC
  inst->server = server;
  inst->da = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Amp.instMag.i"); // the node to operate on
  inst->da_callback = _findAttributeValueEx(inst->da, allInputValues);

  return inst;
}
