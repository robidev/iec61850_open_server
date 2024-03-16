#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "RBDR.h"

// callback when GOOSE is received
void RBDR_callback(InputEntry *extRef)
{
  RBDR *inst = extRef->callBackParam;
  if (extRef->value != NULL)
  {
    inst->value = MmsValue_getBitStringAsInteger(extRef->value);
  }
}

//TODO, callback does not equal sample rate. We probably should launch a sampler thread or advance the bufferindex some other way
void * RBDR_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues)
{
  RBDR *inst = (RBDR *)malloc(sizeof(RBDR)); // create new instance with MALLOC
  inst->server = server;
  inst->input = input;
  inst->value = 0;
  //register callback for digital input
  // this should record the data in a buffer
  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "digital") == 0) 
      {
        extRef->callBack = (callBackFunction)RBDR_callback;
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }
  return inst;
}