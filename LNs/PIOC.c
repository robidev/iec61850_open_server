#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h>
// #include "../static_model.h"
#include "PIOC.h"
#include "dsp.h"
#include <time.h>

//
// PIOC : instantanious over current protection; will trip immediately when current is too high
//
typedef struct sPIOC
{
  IedServer server;
  DataAttribute *Op_general;
  void *Op_general_callback;
  Input *input;
  int tripTimer;
  bool trip;
  DSP *dspI;
  double StrVal;
} PIOC;



// callback when SMV is received
void PIOC_callback_SMV(void *pioc_inst)
{
  PIOC *inst = pioc_inst;
  int i = 0;
  while (i < 4) // only trigger on amps. TODO: ensure it only triggers on Amps lnrefs, instead of relying on the order in the SCD file
  {
    double current =  DSP_get_phs(inst->dspI, i); // get absolute current from dsp
    // check if value is outside allowed band
    // TODO: get values from settings
    if (current > inst->StrVal )
    {
      printf("PIOC: treshold reached\n");
      MmsValue *tripValue = MmsValue_newBoolean(true);

      IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue);
      InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element

      MmsValue_delete(tripValue);
      inst->tripTimer = 0;
      inst->trip = true;
      // if so send to internal PTRC
    }
    i++;
  }

  if (inst->tripTimer > 200 && inst->trip == true)
  {
    // printf("PIOC: treshold NOT reached\n");
    MmsValue *tripValue = MmsValue_newBoolean(false);

    IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue);
    InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element

    MmsValue_delete(tripValue);
    // if so send to internal PTRC
    inst->tripTimer = 0;
    inst->trip = false;
  }
  inst->tripTimer++;
}

static void getPIOCSettings(IedServer server, LogicalNode *ln)
{
  DataAttribute * StrVal = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "StrVal.setMag.f"); // the node to operate on
  MmsValue* StrValValue = IedServer_getAttributeValue(server,  StrVal);
  float val = MmsValue_toFloat(StrValValue);
  printf("PIOC Setting StrVal: %f\n",val);
}

void * PIOC_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  PIOC *inst = (PIOC *)malloc(sizeof(PIOC)); // create new instance with MALLOC
  inst->server = server;
  inst->tripTimer = 0;
  inst->trip = false;
  inst->Op_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Op.general"); // the node to operate on
  inst->Op_general_callback = _findAttributeValueEx(inst->Op_general, allInputValues);
  inst->input = input;
  inst->dspI = NULL;
  inst->StrVal = 600; // 600 Amps, sane default in relation to a PTOC StrVal of 100 A

  IecDataPoint dataPoints[1] = {
      {"StrVal.setMag.f", IEC_TYPE_DOUBLE},
  };
  // Retrieve settings from datamodel
  int retrieved = IecServer_getDataPoints(server, ln, dataPoints, 1);
  // if found, assign them
  if (dataPoints[0].success) {
      inst->StrVal = dataPoints[0].value.floatVal;
  }

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "PIOC_Amp1") == 0)
      {
        inst->dspI = init_dsp_I(server, extRef);//this is to reference the first extref
        DSP_add_callback_on_update(inst->dspI,PIOC_callback_SMV, inst);//called when DSP has processed data
      }
      if (strcmp(extRef->intAddr, "PIOC_Amp3") == 0) // find extref for the last SMV phase, using the intaddr, so that all values are updated, we ignore nutral in case we have 3 phase, and neutral is calculated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(inst->dspI);
        extRef->callBackParam = inst->dspI;
      }
      extRef = extRef->sibling;
    }
  }

  //getPIOCSettings(server, ln);

  return inst;
}


