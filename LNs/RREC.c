#include <libiec61850/hal_thread.h>
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "RREC.h"
//Recloser
/*
OpCls ACT Operation ”close switch” issued to close the XCBR
AutoRecSt ENS Auto reclosing status
			<DO name="OpCls" type="ACT"/>
			<DO name="AutoRecSt" type="ENS_2"/>
*/

typedef struct sRREC
{
  IedServer server;
  DataAttribute *Op_general;
  void *Op_general_callback;
  int tripstate;
  int tripCount;
} RREC;


void RREC_reenable_timer(InputEntry *extRef)
{
  Thread_sleep(60000);
  RREC *inst = extRef->callBackParam;
  if (extRef->value != NULL)
  {
    if((inst->tripstate > 0 || inst->tripCount > 0) && Dbpos_fromMmsValue(extRef->value) == DBPOS_ON)
    {
      inst->tripstate = 0;
      inst->tripCount = 0;
    }
  }
}

void RREC_recloser_timer(InputEntry *extRef)
{
  Thread_sleep(3000);
  RREC *inst = extRef->callBackParam;
  if (extRef->value != NULL)
  {
    if(inst->tripstate == 2 && Dbpos_fromMmsValue(extRef->value) == DBPOS_OFF)
    {
      //operate 
      MmsValue *opValue = MmsValue_newBoolean(true);
      IedServer_updateAttributeValue(inst->server, inst->Op_general, opValue);
      InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element
      MmsValue_delete(opValue);
      inst->tripCount++;
      inst->tripstate = 0;
    }
  }  
}

// reveice status from circuit breaker
void RREC_xcbr_callback(InputEntry *extRef)
{
  RREC *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {
    if(inst->tripstate == 1 && Dbpos_fromMmsValue(extRef->value) == DBPOS_OFF)
    {
      inst->tripstate = 2;
      //check tripcount
      if(inst->tripCount < 4)
      {
        //set timer, if trip is not cleared by then, operate to close
        Thread thread = Thread_create((ThreadExecutionFunction)RREC_recloser_timer, extRef, true);
        Thread_start(thread);
      }
      else // lock state
      {
        printf("Recloser in locked state");
        inst->tripCount++;
        inst->tripstate = 0;
      }
    }

    // check for close state, if close stays on for 60 seconds, re-set/rearm recloser
    if((inst->tripstate > 0 || inst->tripCount > 0) && Dbpos_fromMmsValue(extRef->value) == DBPOS_ON)
    {
      //start threat to rearm recloser
      Thread thread = Thread_create((ThreadExecutionFunction)RREC_reenable_timer, extRef, true);
      Thread_start(thread);
    }
  }
}

void RREC_timeout(InputEntry *extRef)
{
  Thread_sleep(10000);
  RREC *inst = extRef->callBackParam;
  if(inst->tripstate == 1)
  {
    inst->tripstate = 0;
    printf("Recloser timeout during time between trip and switch response");
  }
}

void RREC_input_callback(InputEntry *extRef)
{
  RREC *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {
    bool state = MmsValue_getBoolean(extRef->value);
    if (state == true && inst->tripstate == 0)
    {
      printf("RREC: trip \n"); 
      inst->tripstate = 1;
      Thread thread = Thread_create((ThreadExecutionFunction)RREC_timeout, extRef, true);
      Thread_start(thread);
    }
  }
}

void RREC_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues)
{
  //input is trip and pos
  //if trip signal detect, and a set time is passed, check pos, and if still open, close switch, increment tripCount
  //   if trip is solved, go back to normal state
  //check timeout once more, if switch is still closed, reset tripCount.
  //if again a trip is found, do the same, until tripcount is too high. only re-arm after a timeout after switch closes (60seconsd)

  RREC *inst = (RREC *)malloc(sizeof(RREC)); // create new instance with MALLOC
  inst->server = server;
  inst->tripstate = 0;
  inst->Op_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Op.general"); // the node to operate on, to which the XCBR is subscribed
  inst->Op_general_callback = _findAttributeValueEx(inst->Op_general, allInputValues);

  // find extref for the input signals for this LN
  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      // subscribed to Op signal of Protection; Time Over Current
      if (strcmp(extRef->intAddr, "PTRC_Tr") == 0)
      {
        extRef->callBack = (callBackFunction)RREC_input_callback; // callback to trigger when PTOC.Op is set
        extRef->callBackParam = inst;
      }
      // subscribed to stVal of XCBR to check its position
      if (strcmp(extRef->intAddr, "xcbr_stval") == 0)
      {
        extRef->callBack = (callBackFunction)RREC_xcbr_callback;
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }

}