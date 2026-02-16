#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h>
// #include "../static_model.h"
#include "PDIF.h"
#include "dsp.h"
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#define PDIF_MAX_DSP_COUNT 8
//
// PDIF : differential current protection; will trip if difference in incoming current is too big in relation to outgoing current. result should be 0
//
typedef struct sPDIF
{
  IedServer server;
  DataAttribute *Op_general;
  void *Op_general_callback;
  Input *input;
  bool trip;

  // in current
  DSP *dspI1[PDIF_MAX_DSP_COUNT];
  bool dspI1_enabled[PDIF_MAX_DSP_COUNT];
  uint32_t dspI1_count;

  // out current
  DSP *dspI2[PDIF_MAX_DSP_COUNT];
  bool dspI2_enabled[PDIF_MAX_DSP_COUNT];
  uint32_t dspI2_count;

  float LoSet;        // Differential pickup
  float HiSet;        // Bias slope
  float MinOpTmms;    // Minimum operate time
  float operateTimer_ms;
  float samplePeriod_ms;

  /*
			MaxOpTmms
			RsDlTmms
			RstMod
			TmACrv
  */

} PDIF;



void PDIF_set_swi_in(InputEntry *extRef)
{
  PDIF * inst = extRef->callBackParam;
  if(inst != NULL)
  {
    int32_t index = extract_last_index(extRef->intAddr);// get index
    if(index != -1 && index < PDIF_MAX_DSP_COUNT)
      inst->dspI1_enabled[index] = MmsValue_getBoolean(extRef->value);
  }
}

void PDIF_set_swi_out(InputEntry *extRef)
{
  PDIF * inst = extRef->callBackParam;
  if(inst != NULL)
  {
    int32_t index = extract_last_index(extRef->intAddr);// get index
    if(index != -1 && index < PDIF_MAX_DSP_COUNT)
      inst->dspI2_enabled[index] = MmsValue_getBoolean(extRef->value);
    
  }
}

// callback when SMV is received
void PDIF_callback_SMV(void *pdif_inst)
{
  PDIF *inst = pdif_inst;
  uint32_t i = 0;
  bool operate = false;

  while (i < 4) // only trigger on amps.
  {
    float Idiff, Irest;
    float AmpValue1  =  0;
    for(uint32_t dsp1 = 0; dsp1 < inst->dspI1_count; dsp1++) {
      if(inst->dspI1_enabled[dsp1] == true && inst->dspI1[dsp1] != NULL) // check for enabled switch
        AmpValue1 += (float)DSP_get_phs(inst->dspI1[dsp1], i); // get absolute incoming current from dsp   
    }
 
    float AmpValue2 =  0;
    for(uint32_t dsp2 = 0; dsp2 < inst->dspI2_count; dsp2++){
      if(inst->dspI2_enabled[dsp2] == true && inst->dspI2[dsp2] != NULL) // check for enabled switch
        AmpValue2 +=  (float)DSP_get_phs(inst->dspI2[dsp2], i); // get absolute outgoing current from dsp
    }

    Idiff = fabsf(AmpValue1 - AmpValue2);
    Irest = 0.5f * (AmpValue1 + AmpValue2);

    float threshold = inst->LoSet + inst->HiSet * Irest;

    if (Idiff > threshold)
    {
      operate = true;
    }
    i++;
  }

    // Timing logic (MinOpTmms)
  if (operate) {
      inst->operateTimer_ms += inst->samplePeriod_ms;
      if (inst->operateTimer_ms >= inst->MinOpTmms && inst->trip == false)
      {
        printf("PDIF: treshold reached\n");
        MmsValue *tripValue = MmsValue_newBoolean(true);

        IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue);
        InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element

        MmsValue_delete(tripValue);
        inst->trip = true;
        // if so send to internal PTRC
      }
  } 
  else 
  {
    inst->operateTimer_ms = 0.0f;
    if (inst->trip == true){
      // printf("PDIF: treshold NOT reached\n");
      MmsValue *tripValue = MmsValue_newBoolean(false);

      IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue);
      InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element

      MmsValue_delete(tripValue);
      // if so send to internal PTRC
      inst->trip = false;
    }
  } 
}

void * PDIF_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  PDIF *inst = (PDIF *)malloc(sizeof(PDIF)); // create new instance with MALLOC
  inst->server = server;
  inst->operateTimer_ms = 0.0f;
  inst->samplePeriod_ms = 20.0f; // hardcoded for every cycle of 50hz(80 samples), but should be actually measured
  inst->trip = false;
  inst->Op_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Op.general"); // the node to operate on
  inst->Op_general_callback = _findAttributeValueEx(inst->Op_general, allInputValues);
  inst->input = input;

  for(int i = 0; i < PDIF_MAX_DSP_COUNT; i++)
  {
    inst->dspI1[i] = NULL;
    inst->dspI1_enabled[i] = true; //default is true, in case we do not receive any GOOSE, assume its connected
    inst->dspI2[i] = NULL;
    inst->dspI2_enabled[i] = true; //default is true, in case we do not receive any GOOSE, assume its connected
  }
  inst->dspI1_count = 0;
  inst->dspI2_count = 0;

  inst->LoSet = 0.20f * 1000.0f; // 0.2 pu of 1000 Amps = 200 Amp
  inst->HiSet = 0.30f;
  inst->MinOpTmms = 40.0f; // 40 milliseconds, 10ms is better

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;
    while (extRef != NULL)
    {
      if (strncmp(extRef->intAddr, "PDIF_in_Amp1",12) == 0)
      {
        inst->dspI1[inst->dspI1_count] = init_dsp_I(server, extRef);//this is to reference the first extref
        if(inst->dspI1[inst->dspI1_count] != NULL)
        {
          inst->dspI1_count++;
        }
      }
      if (strncmp(extRef->intAddr, "PDIF_in_Amp3",12) == 0 && inst->dspI1[inst->dspI1_count -1] != NULL) // find extref for the last SMV phase, using the intaddr, so that all values are updated, we ignore nutral in case we have 3 phase, and neutral is calculated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(inst->dspI1[inst->dspI1_count -1]);
        extRef->callBackParam = inst->dspI1[inst->dspI1_count -1];
      }

      if (strncmp(extRef->intAddr, "PDIF_out_Amp1",13) == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        inst->dspI2[inst->dspI2_count] = init_dsp_I(server, extRef);//this is to reference the first extref
        if(inst->dspI2[inst->dspI2_count] != NULL)
        {
          inst->dspI2_count++;
        }       
      }
      if (strncmp(extRef->intAddr, "PDIF_out_Amp3",13) == 0 && inst->dspI2[inst->dspI2_count -1] != NULL) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(inst->dspI2[inst->dspI2_count -1]);
        extRef->callBackParam = inst->dspI2[inst->dspI2_count -1];
      }

      if (strncmp(extRef->intAddr, "PDIF_in_swi_",12) == 0 ) // find extref for the swi associted by index(last value) with a dspI[index]
      {
        extRef->callBack = (callBackFunction)PDIF_set_swi_in;
        extRef->callBackParam = inst;
        int32_t index = extract_last_index(extRef->intAddr);// get index
        if(index != -1 && index < PDIF_MAX_DSP_COUNT)
          inst->dspI1_enabled[index] = false; // if subscribed to a swi value, then default is off
      }
      if (strncmp(extRef->intAddr, "PDIF_out_swi_",13) == 0 ) // find extref for the swi associted by index(last value) with a dspI[index]
      {
        extRef->callBack = (callBackFunction)PDIF_set_swi_out;
        extRef->callBackParam = inst;
        int32_t index = extract_last_index(extRef->intAddr);// get index
        if(index != -1 && index < PDIF_MAX_DSP_COUNT)
          inst->dspI2_enabled[index] = false; // if subscribed to a swi value, then default is off
      }


      extRef = extRef->sibling;
    }
  }

  //ensure the processing callback is called once per cycle, after all values are received
  if(inst->dspI2_count > 0 && inst->dspI2[inst->dspI2_count -1] != NULL) {
    DSP_add_callback_on_update(inst->dspI2[inst->dspI2_count -1],PDIF_callback_SMV, inst);//called when DSP has processed data
  }

  return inst;
}
