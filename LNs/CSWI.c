#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h> /* for Thread_sleep() */

typedef struct sCSWI
{
  IedServer server;

  DataAttribute* Pos_stVal;
  DataAttribute* Pos_t;
  void * Pos_stVal_callback;

  DataAttribute* opOk;
  void * opOk_callback;
  Dbpos currentValue;
  int timeout;
  bool EnaOpn;
  bool EnaCls;
} CSWI;


//receive status from circuit breaker
void CSWI_currentValue_callback(InputEntry* extRef)
{
  CSWI* inst = extRef->callBackParam;

  if(extRef->value != NULL)
  {
    inst->currentValue = Dbpos_fromMmsValue(extRef->value);
    //MmsValue_printToBuffer(extRef->value, printBuf, 1024);
    //printf("CSWI: Received Breaker position: %s\n", printBuf);
  }
}

//receive status from circuit breaker
void CSWI_EnaOpn_callback(InputEntry* extRef)
{
  CSWI* inst = extRef->callBackParam;

  if(extRef->value != NULL)
  {
    inst->EnaOpn = MmsValue_getBoolean(extRef->value);
    if(inst->EnaOpn)
      printf("CSWI: Received CILO EnaOpn: true\n");
    else
      printf("CSWI: Received CILO EnaOpn: false\n");
  }
}

//receive status from circuit breaker
void CSWI_EnaCls_callback(InputEntry* extRef)
{
  CSWI* inst = extRef->callBackParam;

  if(extRef->value != NULL)
  {
    
    inst->EnaCls = MmsValue_getBoolean(extRef->value);
    if(inst->EnaCls)
      printf("CSWI: Received CILO EnaCls: true\n");
    else
      printf("CSWI: Received CILO EnaCls: false\n");
  }
}

static CheckHandlerResult checkHandler(ControlAction action, void* parameter, MmsValue* ctlVal, bool test, bool interlockCheck)
{
    if (ControlAction_isSelect(action))
        printf("check handler called by select command!\n");
    else
        printf("check handler called by operate command!\n");

    if (interlockCheck)
    {
        printf("  with interlock check bit set, interlock is always checked anyway!\n");
    }

    printf("  ctlNum: %i\n", ControlAction_getCtlNum(action));

    CSWI* inst = parameter;
    if(inst != NULL)
    {
      //check interlocking
      bool state = MmsValue_getBoolean(ctlVal);
      if(state == true && inst->EnaOpn == true)//if we try to open the switch, and opOpen allows it
        return CONTROL_ACCEPTED;
      if(state == false && inst->EnaCls == true)//if we try to close the switch, and opClose allows it
        return CONTROL_ACCEPTED;
      //else the object will be refused
      ControlAction_setAddCause(action, ADD_CAUSE_BLOCKED_BY_INTERLOCKING);//ControlAddCause addCause
      return CONTROL_OBJECT_ACCESS_DENIED;
    }
    
    return CONTROL_OBJECT_UNDEFINED;
}

static ControlHandlerResult controlHandlerForBinaryOutput(ControlAction action, void* parameter, MmsValue* value, bool test)
{
    CSWI* inst = parameter;

    int state = MmsValue_getBoolean(value);

    if(inst->timeout == 0)
    {
      printf("control handler called with value: %i\n", state);
      printf("  ctlNum: %i\n", ControlAction_getCtlNum(action));

      uint64_t timestamp = Hal_getTimeInMs();
      IedServer_updateUTCTimeAttributeValue(inst->server, inst->Pos_t, timestamp);

      IedServer_updateAttributeValue(inst->server, inst->opOk, value);
      InputValueHandleExtensionCallbacks(inst->opOk_callback); //update the associated callbacks with this Data Element
    }

    if((state == 1 && inst->currentValue == DBPOS_OFF) || (state == 0 && inst->currentValue == DBPOS_ON))
    {
      inst->timeout = 0;
      ControlAction_setAddCause(action, ADD_CAUSE_POSITION_REACHED);
      return CONTROL_RESULT_OK;
    }
    if(inst->currentValue == DBPOS_BAD_STATE)// if desired state is not reached in time;
    {
      inst->timeout = 0;
      ControlAction_setAddCause(action, ADD_CAUSE_INVALID_POSITION);
      return CONTROL_RESULT_FAILED;
    }
      
    inst->timeout++;
    // wait until desired state is reached, or timeout ocurred
    if(inst->timeout < 1000)//TODO: check for elapsed time instead of iterations
    {
      Thread_sleep(10);
      //printf("CSWI: waiting on status-change of pysical equipment...\n");
      return CONTROL_RESULT_WAITING;
    }
    inst->timeout = 0;
    ControlAction_setAddCause(action, ADD_CAUSE_INVALID_POSITION);//ControlAddCause addCause
    return CONTROL_RESULT_FAILED;
}




void CSWI_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues)
{
  CSWI* inst = (CSWI *) malloc(sizeof(CSWI));//create new instance with MALLOC

  inst->server = server;
  inst->currentValue = 0;
  inst->timeout = 0;
  inst->EnaOpn = true;
  inst->EnaCls = true;
  inst->Pos_stVal = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Pos.stVal");//the node to operate on when a operate is triggered
  inst->Pos_t = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Pos.t");//the node to operate on when a operate is triggered
  inst->Pos_stVal_callback = _findAttributeValueEx(inst->Pos_stVal, allInputValues);//find node that this element was subscribed to, so that it will be called during an update

  inst->opOk = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Pos.opOk");
  inst->opOk_callback = _findAttributeValueEx(inst->opOk, allInputValues);

  //find extref for the last SMV, using the intaddr
  if(input != NULL)
  {
    InputEntry* extRef = input->extRefs;

    while(extRef != NULL)
    {
      //receive status of associated XCBR
      if(strcmp(extRef->intAddr,"xcbr_stval") == 0)
      {
        extRef->callBack = (callBackFunction) CSWI_currentValue_callback;
        extRef->callBackParam = inst;
      }
      if(strcmp(extRef->intAddr,"EnaOpn") == 0)
      {
        //register callbacks for GOOSE-subscription
        extRef->callBack = (callBackFunction) CSWI_EnaOpn_callback;
        extRef->callBackParam = inst;//pass instance in param
      }
      if(strcmp(extRef->intAddr,"EnaCls") == 0)
      {
        //register callbacks for GOOSE-subscription
        extRef->callBack = (callBackFunction) CSWI_EnaCls_callback;
        extRef->callBackParam = inst;//pass instance in param
      }
      extRef = extRef->sibling;
    }
  }
  // initialise control logic
  IedServer_setControlHandler(server, (DataObject *)ModelNode_getChild((ModelNode*) ln, "Pos"), (ControlHandler) controlHandlerForBinaryOutput, inst);
  //during an operate, a certain element will need to update in the CSWI model(opOk element? ctlVal is not subscribable), to which the XCBR is subscribed (goose or directly)
  IedServer_setPerformCheckHandler(server, (DataObject *)ModelNode_getChild((ModelNode*) ln, "Pos"), checkHandler, inst);
}

