#include <libiec61850/hal_thread.h>
#include "iec61850_model_extensions.h"
#include "XCBR.h"
#include "XSWI.h"


// callback for trip signal -> will trigger process
void XCBR_callback_Tr(InputEntry *extRef)
{
  XSWI *inst = extRef->callBackParam;
  bool state = MmsValue_getBoolean(extRef->value);

  if(inst->XSWI_callback_ln == NULL)
    return;
  // only one type of extref is expected: ctlVal
  if (state == true)
  {
    inst->XSWI_callback_ln(inst, false);
  }
}

// callback for operate signal -> will trigger process
void XCBR_callback_Op(InputEntry *extRef)
{
  XSWI * inst = extRef->callBackParam;
  bool state = MmsValue_getBoolean(extRef->value);

  if(inst->XSWI_callback_ln == NULL)
    return;

  inst->XSWI_callback_ln(inst, state);
}

// initialise XCBR instance for process simulation, and publish/subscription of GOOSE
void *XCBR_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  XSWI *inst = (XSWI *)malloc(sizeof(XSWI)); // create new instance with MALLOC
  inst->server = server;
  inst->Pos_stVal = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Pos.stVal");
  inst->Pos_t = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Pos.t");       // the node to operate on when a operate is triggered
  inst->Pos_stVal_callback = _findAttributeValueEx(inst->Pos_stVal, allInputValues); // find node that this element was subscribed to, so that it will be called during an update
  inst->XSWI_callback_ln = NULL;
  inst->config = NULL;
  inst->sem = Semaphore_create(1);
  
  if (input != NULL)
  {
    InputEntry *extref = input->extRefs;
    while (extref != NULL)
    {
      if (strcmp(extref->intAddr, "Tr") == 0)
      {
        // register callbacks for poll and GOOSE-subscription
        extref->callBack = (callBackFunction)XCBR_callback_Tr;
        extref->callBackParam = inst; // pass instance in param
      }
      if (strcmp(extref->intAddr, "Op") == 0)
      {
        // register callbacks for poll and GOOSE-subscription
        extref->callBack = (callBackFunction)XCBR_callback_Op;
        extref->callBackParam = inst; // pass instance in param
      }

      extref = extref->sibling;
    }
  }
  else
  {
    printf("ERROR: no input element defined");
    return 0;
  }

  return inst;
}

