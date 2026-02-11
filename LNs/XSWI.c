#include <libiec61850/hal_thread.h>
#include "iec61850_model_extensions.h"
#include "XSWI.h"



void XSWI_EnaOpn_callback(InputEntry *extRef)
{
  XSWI *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {
    inst->BlkOpn = !MmsValue_getBoolean(extRef->value);
    if (inst->BlkOpn) 
      printf("XSWI: BlkOpn: true\n");
    else
      printf("XSWI: BlkOpn: false\n");

    IedServer_updateBooleanAttributeValue(inst->server, inst->BlkOpn_stVal, inst->BlkOpn);
    InputValueHandleExtensionCallbacks(inst->BlkOpn_stVal_callback); // update the associated callbacks with this Data Element
  }
}

void XSWI_EnaCls_callback(InputEntry *extRef)
{
  XSWI *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {

    inst->BlkCls = !MmsValue_getBoolean(extRef->value);
    if (inst->BlkCls)
      printf("XSWI: BlkCls: true\n");
    else
      printf("XSWI: BlkCls: false\n");

    IedServer_updateBooleanAttributeValue(inst->server, inst->BlkCls_stVal, inst->BlkCls_stVal);
    InputValueHandleExtensionCallbacks(inst->BlkCls_stVal_callback); // update the associated callbacks with this Data Element
  }
}

// callback for open signal from input-> will trigger process 
void XSWI_callback_Opn(InputEntry *extRef)
{
  XSWI * inst = extRef->callBackParam;
  if(MmsValue_getBoolean(extRef->value))
  {
    XSWI_Opn(inst);
  }
}

// callback for close signal from input-> will trigger process 
void XSWI_callback_Cls(InputEntry *extRef)
{
  XSWI * inst = extRef->callBackParam;
  if(MmsValue_getBoolean(extRef->value))
  {
    XSWI_Cls(inst);
  }
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

  inst->BlkOpn = false;
  inst->BlkOpn_stVal = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "BlkOpn.stVal");
  inst->BlkOpn_stVal_callback = _findAttributeValueEx(inst->BlkOpn_stVal, allInputValues); // find node that this element was subscribed to, so that it will be called during an update
  inst->BlkCls = false;
  inst->BlkCls_stVal = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "BlkCls.stVal");
  inst->BlkCls_stVal_callback = _findAttributeValueEx(inst->BlkCls_stVal, allInputValues); // find node that this element was subscribed to, so that it will be called during an update


  inst->XSWI_callback_ln = NULL;
  inst->config = NULL;
  inst->sem = Semaphore_create(1);

  if (input != NULL)
  {
    InputEntry *extref = input->extRefs;
    
    while (extref != NULL)
    {
      if (extref->intAddr != NULL && strncmp(extref->intAddr, "OpOpn", 5) == 0) // open from CSWI or RREC
      {
        extref->callBack = (callBackFunction)XSWI_callback_Opn;
        extref->callBackParam = inst; // pass instance in param
      }
      if (extref->intAddr != NULL && strncmp(extref->intAddr, "OpCls", 5) == 0) // close from CSWI or recloser
      {
        extref->callBack = (callBackFunction)XSWI_callback_Cls;
        extref->callBackParam = inst; // pass instance in param
      }

      if (strcmp(extref->intAddr, "EnaOpn") == 0)
      {
        // register callbacks for CILO subscription
        extref->callBack = (callBackFunction)XSWI_EnaOpn_callback;
        extref->callBackParam = inst; // pass instance in param
      }
      if (strcmp(extref->intAddr, "EnaCls") == 0)
      {
        // register callbacks for CILO subscription
        extref->callBack = (callBackFunction)XSWI_EnaCls_callback;
        extref->callBackParam = inst; // pass instance in param
      }

      extref = extref->sibling;
    }
  }

  return inst;
}

void XSWI_Opn(XSWI * inst)
{
  if(inst->XSWI_callback_ln == NULL)
    return;

  if(inst->BlkOpn == true) {
    printf("XSWI: Open command blocked by BlkOpn\n");
    return;
  }
  inst->XSWI_callback_ln(inst, false); // false means open (not conducting)    
}

void XSWI_Cls(XSWI * inst)
{
  if(inst->XSWI_callback_ln == NULL)
    return;

  if(inst->BlkCls == true) {
    printf("XSWI: Close command blocked by BlkCls\n");
    return;
  }
  inst->XSWI_callback_ln(inst, true);// true means closed (conducting)
}

void XSWI_change_switch(XSWI *inst, Dbpos value)
{
  //printf("*** XSWI_change_switch ***\n");
  uint64_t timestamp = Hal_getTimeInMs();
  IedServer_updateDbposValue(inst->server, inst->Pos_stVal, value);
  IedServer_updateUTCTimeAttributeValue(inst->server, inst->Pos_t, timestamp);
  InputValueHandleExtensionCallbacks(inst->Pos_stVal_callback); // update the associated callbacks with this Data Element
}
