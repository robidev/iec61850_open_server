#include "TVTR.h"
#include "iec61850_model_extensions.h"

void *TVTR_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  TVTR *inst = (TVTR *)malloc(sizeof(TVTR)); // create new instance with MALLOC
  inst->server = server;
  inst->da = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Vol.instMag.i"); // the node to operate on
  inst->da_callback = _findAttributeValueEx(inst->da, allInputValues);

  return inst;
}
