#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h> /* for Thread_sleep() */

typedef struct sCSWI
{
  IedServer server;

  DataAttribute *Pos_stVal;
  DataAttribute *Pos_t;
  void *Pos_stVal_callback;

  DataAttribute *OpOpn;
  void *OpOpn_callback;
  DataAttribute *OpCls;
  void *OpCls_callback;
  Dbpos currentValue;
  int timeout;
  bool EnaOpn;
  bool EnaCls;
  bool Loc;
} CSWI;

// receive status from circuit breaker
void CSWI_currentValue_callback(InputEntry *extRef)
{
  CSWI *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {
    Dbpos oldvalue = inst->currentValue;
    inst->currentValue = Dbpos_fromMmsValue(extRef->value);

    if(oldvalue != inst->currentValue)
    {
      uint64_t timestamp = Hal_getTimeInMs();
      IedServer_updateUTCTimeAttributeValue(inst->server, inst->Pos_t, timestamp);
      IedServer_updateAttributeValue(inst->server, inst->Pos_stVal, extRef->value);
      InputValueHandleExtensionCallbacks(inst->Pos_stVal_callback); // update the associated callbacks with this Data Element
    }
  }
}

void CSWI_EnaOpn_callback(InputEntry *extRef)
{
  CSWI *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {
    inst->EnaOpn = MmsValue_getBoolean(extRef->value);
    if (inst->EnaOpn)
      printf("CSWI: Received CILO EnaOpn: true\n");
    else
      printf("CSWI: Received CILO EnaOpn: false\n");
  }
}

void CSWI_EnaCls_callback(InputEntry *extRef)
{
  CSWI *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {

    inst->EnaCls = MmsValue_getBoolean(extRef->value);
    if (inst->EnaCls)
      printf("CSWI: Received CILO EnaCls: true\n");
    else
      printf("CSWI: Received CILO EnaCls: false\n");
  }
}

void CSWI_Loc_callback(InputEntry *extRef)
{
  CSWI *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {
    bool value = MmsValue_getBoolean(extRef->value);
    printf("CSWI received Loc status: %d from %s\n", value, extRef->Ref);
    inst->Loc = value;
  }
}

static CheckHandlerResult checkHandler(ControlAction action, void *parameter, MmsValue *ctlVal, bool test, bool interlockCheck)
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

  CSWI *inst = parameter;
  if (inst != NULL)
  {
    if (inst->Loc == true) // we are in local operation
    {
      ControlAction_setAddCause(action, ADD_CAUSE_BLOCKED_BY_SWITCHING_HIERARCHY); // ControlAddCause addCause
      return CONTROL_OBJECT_ACCESS_DENIED;
    }

    // check interlocking
    bool state = MmsValue_getBoolean(ctlVal);
    if (state == false && inst->EnaOpn == true) // if we try to open(ctlVal==false) the switch, and opOpen allows it
      return CONTROL_ACCEPTED;
    if (state == true && inst->EnaCls == true) // if we try to close(ctlVal==true) the switch, and opClose allows it
      return CONTROL_ACCEPTED;
    // else the object will be refused
    ControlAction_setAddCause(action, ADD_CAUSE_BLOCKED_BY_INTERLOCKING); // ControlAddCause addCause
    return CONTROL_OBJECT_ACCESS_DENIED;
  }

  return CONTROL_OBJECT_UNDEFINED;
}

void pulseOp(CSWI *inst, Dbpos pos, bool on)
{
  if(on == true)
  {
    MmsValue *opValue = MmsValue_newBoolean(true);
    if(pos == DBPOS_OFF)//open the switch, so pulse OpOpn to true
    {
      IedServer_updateAttributeValue(inst->server, inst->OpOpn, opValue);
      InputValueHandleExtensionCallbacks(inst->OpOpn_callback); // update the associated callbacks with this Data Element
    }
    if(pos == DBPOS_ON)//close the switch, so pulse OpCls to true
    {
      IedServer_updateAttributeValue(inst->server, inst->OpCls, opValue);
      InputValueHandleExtensionCallbacks(inst->OpCls_callback); // update the associated callbacks with this Data Element
    }
    MmsValue_delete(opValue);
  }
  else
  {
    MmsValue *opValue = MmsValue_newBoolean(false);
    if(pos == DBPOS_OFF)//open the switch done, so reset OpOpn to false
    {
      IedServer_updateAttributeValue(inst->server, inst->OpOpn, opValue);
      InputValueHandleExtensionCallbacks(inst->OpOpn_callback); // update the associated callbacks with this Data Element
    }
    if(pos == DBPOS_ON)//close the switch done, so reset OpCls to false
    {
      IedServer_updateAttributeValue(inst->server, inst->OpCls, opValue);
      InputValueHandleExtensionCallbacks(inst->OpCls_callback); // update the associated callbacks with this Data Element
    }
    MmsValue_delete(opValue);
  }

}


static ControlHandlerResult controlHandlerForBinaryOutput(ControlAction action, void *parameter, MmsValue *value, bool test)
{
  CSWI *inst = parameter;

  int state = MmsValue_getBoolean(value);

  if (inst->timeout == 0)
  {
    printf("control handler called with value: %i\n", state);
    printf("  ctlNum: %i\n", ControlAction_getCtlNum(action));

    if(state == true) // True is closed, i.e. on
      pulseOp(inst, DBPOS_ON, true); // set signal for OPEN
    else // False is open, i.e. off
      pulseOp(inst, DBPOS_OFF, true); // set signal for CLOSE,
  }

  if ((state == 1 && inst->currentValue == DBPOS_ON) || (state == 0 && inst->currentValue == DBPOS_OFF))
  {
    inst->timeout = 0;
    ControlAction_setAddCause(action, ADD_CAUSE_POSITION_REACHED);
    pulseOp(inst, inst->currentValue, false); // unset signal for OPEN or CLOSE
    return CONTROL_RESULT_OK;
  }
  if (inst->currentValue == DBPOS_BAD_STATE) // if desired state is not reached in time;
  {
    inst->timeout = 0;
    ControlAction_setAddCause(action, ADD_CAUSE_INVALID_POSITION);
    pulseOp(inst, DBPOS_ON, false); // unset signal for OPEN AND CLOSE
    pulseOp(inst, DBPOS_OFF, false); // unset signal for OPEN AND CLOSE
    return CONTROL_RESULT_FAILED;
  }

  inst->timeout++;
  // wait until desired state is reached, or timeout ocurred
  if (inst->timeout < 1000) // TODO: check for elapsed time instead of iterations
  {
    Thread_sleep(10);
    // printf("CSWI: waiting on status-change of pysical equipment...\n");
    return CONTROL_RESULT_WAITING;
  }
  inst->timeout = 0;
  ControlAction_setAddCause(action, ADD_CAUSE_INVALID_POSITION); // ControlAddCause addCause
  pulseOp(inst, DBPOS_ON, false); // unset signal for OPEN AND CLOSE
  pulseOp(inst, DBPOS_OFF, false); // unset signal for OPEN AND CLOSE
  return CONTROL_RESULT_FAILED;
}

void * CSWI_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  CSWI *inst = (CSWI *)malloc(sizeof(CSWI)); // create new instance with MALLOC

  inst->server = server;
  inst->currentValue = 0;
  inst->timeout = 0;
  inst->EnaOpn = true;
  inst->EnaCls = true;
  inst->Loc = false;
  inst->Pos_stVal = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Pos.stVal"); // the node to operate on when a operate is triggered
  inst->Pos_t = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Pos.t");         // the node to operate on when a operate is triggered
  inst->Pos_stVal_callback = _findAttributeValueEx(inst->Pos_stVal, allInputValues);   // find node that this element was subscribed to, so that it will be called during an update

  inst->OpOpn = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "OpOpn.general");
  inst->OpOpn_callback = _findAttributeValueEx(inst->OpOpn, allInputValues);
  inst->OpCls = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "OpCls.general");
  inst->OpCls_callback = _findAttributeValueEx(inst->OpCls, allInputValues);

  // find extref for the last SMV, using the intaddr
  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      // receive status of associated XCBR
      if (strcmp(extRef->intAddr, "stval") == 0)
      {
        extRef->callBack = (callBackFunction)CSWI_currentValue_callback;
        extRef->callBackParam = inst;
      }
      if (strcmp(extRef->intAddr, "EnaOpn") == 0)
      {
        // register callbacks for GOOSE-subscription
        extRef->callBack = (callBackFunction)CSWI_EnaOpn_callback;
        extRef->callBackParam = inst; // pass instance in param
      }
      if (strcmp(extRef->intAddr, "EnaCls") == 0)
      {
        // register callbacks for GOOSE-subscription
        extRef->callBack = (callBackFunction)CSWI_EnaCls_callback;
        extRef->callBackParam = inst; // pass instance in param
      }
      if (strcmp(extRef->intAddr, "Loc") == 0)
      {
        // register callbacks for CILO subscription
        extRef->callBack = (callBackFunction)CSWI_Loc_callback;
        extRef->callBackParam = inst; // pass instance in param
      }
      extRef = extRef->sibling;
    }
  }
  // initialise control logic
  IedServer_setControlHandler(server, (DataObject *)ModelNode_getChild((ModelNode *)ln, "Pos"), (ControlHandler)controlHandlerForBinaryOutput, inst);
  // during an operate, OpOpn, OpCls will need to update in the CSWI model,to which the XCBR is subscribed (goose or directly)
  IedServer_setPerformCheckHandler(server, (DataObject *)ModelNode_getChild((ModelNode *)ln, "Pos"), checkHandler, inst);
  return inst;
}
