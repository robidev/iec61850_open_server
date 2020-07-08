#include "iec61850_model_extensions.h"
#include "inputs_api.h"

typedef struct sCILO
{
  IedServer server;
  Dbpos currentValue;

  DataAttribute* EnaOpn;
  void * EnaOpn_callback;
  DataAttribute* EnaCls;
  void * EnaCls_callback;
} CILO;

//receive status from circuit breaker
void CILO_currentValue_callback(InputEntry* extRef)
{
  CILO* inst = extRef->callBackParam;

  if(extRef->value != NULL)
  {
    inst->currentValue = Dbpos_fromMmsValue(extRef->value);
    //MmsValue_printToBuffer(extRef->value, printBuf, 1024);
    //printf("CSWI: Received Breaker position: %s\n", printBuf);
      MmsValue* open;
      MmsValue* close;

      if(inst->currentValue == DBPOS_ON)//XCBR is closed
      {
	      open = MmsValue_newBoolean(false);//XSWI cannot open
	      close = MmsValue_newBoolean(false);//XSWI cannot open
      }
      else //XCBR is open
      {
	      open = MmsValue_newBoolean(true);//XSWI can open
	      close = MmsValue_newBoolean(true);//XSWI can close
      }

      IedServer_updateAttributeValue(inst->server, inst->EnaOpn, open);
      InputValueHandleExtensionCallbacks(inst->EnaOpn_callback); //update the associated callbacks with this Data Element

      IedServer_updateAttributeValue(inst->server, inst->EnaCls, close);
      InputValueHandleExtensionCallbacks(inst->EnaCls_callback); //update the associated callbacks with this Data Element

      MmsValue_delete(open);
      MmsValue_delete(close);
  }
}

void CILO_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues)
{
  CILO* inst = (CILO *) malloc(sizeof(CILO));//create new instance with MALLOC

  inst->server = server;
  inst->currentValue = 0;
  inst->EnaOpn = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "EnaOpn.stVal");
  inst->EnaOpn_callback = _findAttributeValueEx(inst->EnaOpn, allInputValues);
  inst->EnaCls = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "EnaCls.stVal");
  inst->EnaCls_callback = _findAttributeValueEx(inst->EnaCls, allInputValues);

  //find extref for the last SMV, using the intaddr
  if(input != NULL)
  {
    InputEntry* extRef = input->extRefs;

    while(extRef != NULL)
    {
      //receive status of associated XCBR
      if(strcmp(extRef->intAddr,"stval") == 0)
      {
        extRef->callBack = (callBackFunction) CILO_currentValue_callback;
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }
}
