#include <libiec61850/hal_thread.h>
#include "iec61850_model_extensions.h"
#include "XCBR.h"
#include "XSWI.h"
#include "LLN0.h"

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
    inst->XSWI_callback_ln(inst, false); // false means open (not conducting)
  }
}

// callback for operate signal -> will trigger process
void XCBR_callback_OpOpn(InputEntry *extRef)
{
  XSWI * inst = extRef->callBackParam;
  bool state = MmsValue_getBoolean(extRef->value);

  if(inst->XSWI_callback_ln == NULL)
    return;

  if (state == true)
  {
    if(inst->BlkOpn == true){
      printf("XCBR: Open command blocked by BlkOpn\n");
      return;
    }
    inst->XSWI_callback_ln(inst, false);// false means open (not conducting)
  }
}

// callback for operate signal -> will trigger process to close the switch
void XCBR_callback_OpCls(InputEntry *extRef)
{
  XSWI * inst = extRef->callBackParam;
  bool state = MmsValue_getBoolean(extRef->value);

  if(inst->XSWI_callback_ln == NULL)
    return;

  if (state == true)
  {
    if(inst->BlkCls == true){
      printf("XCBR: Close command blocked by BlkCls\n");
      return;
    }
    inst->XSWI_callback_ln(inst, true);// true means closed (conducting)
  }
}

// initialise XCBR instance for process simulation, and publish/subscription of GOOSE
void *XCBR_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  XSWI *inst = (XSWI *)malloc(sizeof(XSWI)); // create new instance with MALLOC
  inst->server = server;
  inst->Pos_stVal = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Pos.stVal");
  inst->Pos_t = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Pos.t");       // the node to operate on when a operate is triggered
  inst->Pos_stVal_callback = _findAttributeValueEx(inst->Pos_stVal, allInputValues); // find node that this element was subscribed to, so that it will be called during an update

  inst->Loc_stVal = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Loc.stVal");
  inst->Loc_t = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Loc.t");       // the node to operate on when a operate is triggered
  inst->Loc_stVal_callback = _findAttributeValueEx(inst->Loc_stVal, allInputValues); // find node that this element was subscribed to, so that it will be called during an update
  inst->Loc = false;

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
      if (extref->intAddr != NULL && strncmp(extref->intAddr, "Tr", 2) == 0)  // Trip from multiple sources
      {
        extref->callBack = (callBackFunction)XCBR_callback_Tr;
        extref->callBackParam = inst; // pass instance in param
      }
      if (extref->intAddr != NULL && strncmp(extref->intAddr, "OpOpn", 5) == 0) // open from CSWI or RREC
      {
        extref->callBack = (callBackFunction)XCBR_callback_OpOpn;
        extref->callBackParam = inst; // pass instance in param
      }
      if (extref->intAddr != NULL && strncmp(extref->intAddr, "OpCls", 5) == 0) // close from CSWI or recloser
      {
        extref->callBack = (callBackFunction)XCBR_callback_OpCls;
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

      if (strcmp(extref->intAddr, "Loc") == 0)
      {
        // register callbacks for CILO subscription
        extref->callBack = (callBackFunction)XSWI_Loc_callback;
        extref->callBackParam = inst; // pass instance in param
      }

      extref = extref->sibling;
    }
  }

  return inst;
}

