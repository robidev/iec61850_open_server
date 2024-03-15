#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "RADR.h"



// callback when SMV is received
void RADR_callback(InputEntry *extRef)
{
  RADR *inst = extRef->callBackParam;
  if (extRef->value != NULL)
  {
    inst->buffer[inst->bufferIndex] = MmsValue_toInt32(extRef->value);
    inst->bufferIndex++;
    if(inst->bufferIndex >= RADR_MAX_SAMPLES)
    {
      inst->bufferIndex = 0;
    }
  }
}

void * RADR_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues)
{
  RADR *inst = (RADR *)malloc(sizeof(RADR)); // create new instance with MALLOC
  inst->server = server;
  inst->input = input;
  inst->buffer = malloc( sizeof(int32_t)*RADR_MAX_SAMPLES );
  if(inst->buffer == NULL)
  {
    printf("RADR: ERROR could not allocate buffer of size %ld", sizeof(int32_t)*RADR_MAX_SAMPLES );
    free(inst);
    return NULL;
  }
  inst->bufferIndex = 0;
  for(int i = 0; i < RADR_MAX_SAMPLES; i++)
  {
    inst->buffer[i] = 0;
  }
  //register callback for input from sampled values for an analog channel, and make available for fault-recorder
  // this should record the data in a buffer
  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "analog") == 0) 
      {
        extRef->callBack = (callBackFunction)RADR_callback;
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }
  return inst;
}
