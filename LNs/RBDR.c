#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "RBDR.h"



void RBDR_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues)
{
  //register callback for digital input
    // this should record the data in a buffer
}