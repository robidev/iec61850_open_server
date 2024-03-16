#include <libiec61850/hal_thread.h>
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "RADR.h"



// callback when SMV is received
void RADR_callback(InputEntry *extRef)
{
  RADR *inst = extRef->callBackParam;
  if (extRef->value != NULL)
  {
    //This is to sync values between disturbance recorder thread and the main thread, and ruins real-time performance
    while(inst->value_read != 1)//wait until previous value has been stored
    {
      Thread_sleep(1);//force a context switch
    }
    inst->value = MmsValue_toInt32(extRef->value);
    inst->value_read = 0;
  }
}

void * RADR_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues)
{
  RADR *inst = (RADR *)malloc(sizeof(RADR)); // create new instance with MALLOC
  inst->server = server;
  inst->input = input;
  inst->value = 0;
 
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
