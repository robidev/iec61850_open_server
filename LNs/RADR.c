#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "RADR.h"



void RADR_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues)
{
  //register callback for input from sampled values for an analog channel, and make available for fault-recorder
  // this should record the data in a buffer
}