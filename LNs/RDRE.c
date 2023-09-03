#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "RDRE.h"
#include "RADR.h"
#include "RBDR.h"

void RDRE_callback_trip()
{
  //start timer(timer_callback)
}

void timer_callback()
{
  //copy buffer to local data
  //write out local data to comtrade file format
  //RADR/RBDR should hold the circulair buffer
}


void RDRE_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues)
{
  //register callback for input
  //fault recorder, input is RADR/RBDR ln's current/voltage/digital, trigger is trip
  // continous record of circulair buffer in RADR/RBDR
  // when trip, collect few more samples, and then write comtrade file away with timestamp
  //collect analog samples from RADR(one per channel), and digital samples from RBDR(one per channel)
    // find extref for the last SMV, using the intaddr
  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      // receive status of associated XCBR
      if (strcmp(extRef->intAddr, "analog") == 0)
      {
          //this should work if the input ref is the logical node instance instead of a DA, is this allowed?
          LogicalNodeClass *ln = getLNClass(model, model_ex, extRef->Ref);
          if (ln != NULL){
            RADR *item = ln->instance;
          }
      }
      // receive status of associated XCBR
      if (strcmp(extRef->intAddr, "digital") == 0)
      {
          //this should work if the input ref is the logical node instance instead of a DA, is this allowed?
          LogicalNodeClass *ln = getLNClass(model, model_ex, extRef->Ref);
          if (ln != NULL){
            RBDR *item = ln->instance;
          }
      }
      extRef = extRef->sibling;
    }
  }
}