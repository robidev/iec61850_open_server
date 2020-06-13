#include "iec61850_model_extensions.h"
#include "inputs_api.h"

typedef struct sCSWI
{
  IedServer server;
  DataAttribute* Pos_stVal;
  DataAttribute* Pos_t;
  DataAttribute* opOk;
  void * Pos_stVal_callback;
} CSWI;


//reveice status from circuit breaker
void CSWI_xcbr_callback(InputEntry* extRef)
{
  CSWI* inst = extRef->callBackParam;

  if(extRef->value != NULL)
  {
    char printBuf[1024];

    MmsValue_printToBuffer(extRef->value, printBuf, 1024);
    printf("CSWI: Received Breaker position: %s\n", printBuf);
  }
}

static ControlHandlerResult controlHandlerForBinaryOutput(ControlAction action, void* parameter, MmsValue* value, bool test)
{
    uint64_t timestamp = Hal_getTimeInMs();
    CSWI* inst = parameter;

    printf("control handler called\n");
    printf("  ctlNum: %i\n", ControlAction_getCtlNum(action));

    //IedServer_updateUTCTimeAttributeValue(inst->server, inst->Pos_t, timestamp);
    IedServer_updateAttributeValue(inst->server, inst->opOk, value);

    //return CONTROL_RESULT_FAILED;

    return CONTROL_RESULT_OK;
}

void CSWI_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues)
{
  CSWI* inst = (CSWI *) malloc(sizeof(CSWI));//create new instance with MALLOC

  inst->server = server;
  inst->Pos_stVal = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Pos.stVal");//the node to operate on when a operate is triggered
  inst->Pos_t = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Pos.t");//the node to operate on when a operate is triggered
  inst->opOk = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Pos.opOk");
  inst->Pos_stVal_callback = _findAttributeValueEx(inst->Pos_stVal, allInputValues);//find node that this element was subscribed to, so that it will be called during an update
 
  //find extref for the last SMV, using the intaddr
  if(input != NULL)
  {
    InputEntry* extRef = input->extRefs;

    while(extRef != NULL)
    {
      //receive status of associated XCBR
      if(strcmp(extRef->intAddr,"xcbr_stval") == 0)
      {
        extRef->callBack = (callBackFunction) CSWI_xcbr_callback;
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }
  // initialise control logic
  IedServer_setControlHandler(server, (DataObject *)ModelNode_getChild((ModelNode*) ln, "Pos"), (ControlHandler) controlHandlerForBinaryOutput, inst);
  //during an operate, a certain element will need to update in the CSWI model(opOk element? ctlVal is not subscribable), to which the XCBR is subscribed (goose or directly)
}

