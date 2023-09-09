#include <libiec61850/hal_thread.h>
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "RDRE.h"
#include "RADR.h"
#include "RBDR.h"

typedef struct sRDRE {
  IedServer server;
  LinkedList analog;
  LinkedList digital;
} RDRE;

// http://sistemaselectricos.com/cpe_box/comtrade.htm

void timer_callback(RDRE *inst);

void RDRE_callback_trip(InputEntry *extRef)
{
  RDRE *inst = extRef->callBackParam;
  Thread thread = Thread_create((ThreadExecutionFunction)timer_callback, inst, true);
  Thread_start(thread);
}

void timer_callback(RDRE *inst)
{
  Thread_sleep(100);
  uint32_t time = 0;
  FILE *fp;
  fp = fopen("comtrade_data.dat", "w+");
  for(int i = 0; i < RADR_MAX_SAMPLES; i++)
  {
    fprintf(fp,"%d,%d",i,time);
    LinkedList temp = inst->analog;
    while(temp != NULL)
    {
      LogicalNodeClass *ln = LinkedList_getData(temp);
      if(ln != NULL)
      {
        RADR * radr = ln->instance;
        int32_t bufindex = (radr->bufferIndex +1) % RADR_MAX_SAMPLES;
        fprintf(fp,",%d", radr->buffer[(bufindex + i) % RADR_MAX_SAMPLES]);
      }
      temp = LinkedList_getNext(temp);
    }

    temp = inst->digital;
    while(temp != NULL)
    {
      LogicalNodeClass *ln = LinkedList_getData(temp);
      if(ln != NULL)
      {
        RBDR * rbdr = ln->instance;
        int32_t bufindex = (rbdr->bufferIndex +1) % RBDR_MAX_SAMPLES;
        fprintf(fp,",%d", rbdr->buffer[(bufindex + i) % RBDR_MAX_SAMPLES]);
      }
      temp = LinkedList_getNext(temp);
    }
    fprintf(fp,"\r\n");
    time += 100;
  }
  fclose(fp);
  
}


void * RDRE_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues)
{
  RDRE *inst = (RDRE *)malloc(sizeof(RDRE)); // create new instance with MALLOC
  inst->server = server;
  inst->analog = LinkedList_create();
  inst->digital = LinkedList_create();

  //register callback for input
  //fault recorder, input is RADR/RBDR ln's current/voltage/digital, trigger is trip
  // when trip, collect few more samples, and then write comtrade file away with timestamp

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      // receive status of associated XCBR
      if (strcmp(extRef->intAddr, "RDRE_analog") == 0)
      {
          //this should work if the input ref is the logical node instance instead of a DA, is this allowed?
          //this could be called before radr extension is initialised based on the order in the SCL file!!!!!!!!!!!!!!!!!!!!!!!!
          //CFG should ignore ., or SCL file should be fixed, and parent should be retrieved here....
          LogicalNodeClass *ln = getLNClass(model, model_ex, extRef->Ref);
          if (ln != NULL){
            LinkedList_add(inst->analog, ln);
          }
      }
      // receive status of associated XCBR
      if (strcmp(extRef->intAddr, "RDRE_digital") == 0)
      {
          //this should work if the input ref is the logical node instance instead of a DA, is this allowed?
          LogicalNodeClass *ln = getLNClass(model, model_ex, extRef->Ref);
          if (ln != NULL){
            LinkedList_add(inst->digital, ln);
          }
      }
      if (strcmp(extRef->intAddr, "RDRE_Trigger") == 0)
      {
        extRef->callBack = (callBackFunction)RDRE_callback_trip;
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }
  return inst;
}