#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h>
// #include "../static_model.h"
#include "PTOC.h"
#include "dsp.h"
#include <time.h>

//
// PTOC : time over current protection; will trip after set time-curve when current is too high
//
typedef struct sPTOC
{
  IedServer server;
  DataAttribute *Op_general;
  void *Op_general_callback;
  Input *input;
  int tripTimer;
  bool trip;
  uint64_t overCurrent;
  msSinceEpoch prevTime;
  DSP *dspI;
} PTOC;


// callback when SMV is received
void PTOC_callback_SMV(void *ptoc_inst)
{
  PTOC *inst = ptoc_inst;
  int i = 0;
  while (i < 4) // only read on amps.
  {
    double current =  DSP_get_phs(inst->dspI, i); // get absolute current from dsp
    msSinceEpoch time = Hal_getTimeInMs();
    msSinceEpoch delta_t = time - inst->prevTime;
    inst->prevTime = time;

    // check if value is outside allowed band
    // TODO: get values from settings
    if (current > 500)
    {
      if(inst->trip != true)
      {
        printf("PTOC: treshold reached by immediate overcurrent\n");
        MmsValue *tripValue = MmsValue_newBoolean(true);
        IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue);
        InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element
        MmsValue_delete(tripValue);
        inst->trip = true;
      }
      inst->tripTimer = 0;// trip ongoing
    }
    else if (current> 400 )// lineair time overcurrent
    {
      inst->overCurrent += (current - 400) * delta_t;
      if( inst->overCurrent > 100 )
      {
        if(inst->trip != true)
        {
          printf("PTOC: treshold reached by time overcurrent\n");
          MmsValue *tripValue = MmsValue_newBoolean(true);
          IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue);
          InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element
          MmsValue_delete(tripValue);
          inst->trip = true;
        }
        inst->tripTimer = 0; // trip ongoing
      }
    }
    else if(inst->overCurrent > 0)//cooldown
    {
      inst->overCurrent += (current - 400) * delta_t;
      if(inst->overCurrent < 0)
        inst->overCurrent = 0;
    }
    i++;
  }

  if (inst->tripTimer > 200 && inst->trip == true)
  {
    // printf("PTOC: treshold NOT reached\n");
    MmsValue *tripValue = MmsValue_newBoolean(false);

    IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue);
    InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element

    MmsValue_delete(tripValue);
    // if so send to internal PTRC
    inst->tripTimer = 0;
    inst->trip = false;
    inst->overCurrent = 0;
  }
  inst->tripTimer++;
}

void * PTOC_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  PTOC *inst = (PTOC *)malloc(sizeof(PTOC)); // create new instance with MALLOC
  inst->server = server;
  inst->tripTimer = 0;
  inst->trip = false;
  inst->Op_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Op.general"); // the node to operate on
  inst->Op_general_callback = _findAttributeValueEx(inst->Op_general, allInputValues);
  inst->input = input;
  inst->dspI = NULL;

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "PTOC_Amp1") == 0)
      {
        inst->dspI = init_dsp_I(server, extRef);//this is to reference the first extref
        DSP_add_callback_on_update(inst->dspI,PTOC_callback_SMV, inst);//called when DSP has processed data
      }
      if (strcmp(extRef->intAddr, "PTOC_Amp3") == 0) // find extref for the last SMV phase, using the intaddr, so that all values are updated, we ignore nutral in case we have 3 phase, and neutral is calculated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(inst->dspI);
        extRef->callBackParam = inst->dspI;
      }
      extRef = extRef->sibling;
    }
  }
  return inst;
}
