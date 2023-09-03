#include <libiec61850/hal_thread.h>
#include "iec61850_model_extensions.h"
#include "XSWI.h"


// callback for open/close signal from input-> will trigger process 
void XSWI_callback(InputEntry *extRef)
{
  XSWI * inst = extRef->callBackParam;
  if(inst->XSWI_callback_ln == NULL)
    return;

  bool state = MmsValue_getBoolean(extRef->value);
  inst->XSWI_callback_ln(inst, state);
}

int setXSWI_Callback(XSWI *instance, XSWICallback callback)
{
    if (instance == NULL || instance->XSWI_callback_ln != NULL)
    {
        printf("ERROR: could not assign callback");
        return 1;
    }
    instance->XSWI_callback_ln = callback;
    return 0;
}

// initialise XSWI instance for process simulation, and publish/subscription of GOOSE
void *XSWI_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
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
      if (strcmp(extref->intAddr, "Tr") == 0) // TODO: should be Op, but then also modify in SCL
      {
        // register callbacks for input nodes
        extref->callBack = (callBackFunction)XSWI_callback;
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

void XSWI_change_switch(XSWI *inst, Dbpos value)
{
  //printf("*** XSWI_change_switch ***\n");
  uint64_t timestamp = Hal_getTimeInMs();
  IedServer_updateDbposValue(inst->server, inst->Pos_stVal, value);
  IedServer_updateUTCTimeAttributeValue(inst->server, inst->Pos_t, timestamp);
  InputValueHandleExtensionCallbacks(inst->Pos_stVal_callback); // update the associated callbacks with this Data Element
}

