#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h>
// #include "../static_model.h"
#include "PDIF.h"
#include "dsp.h"
#include <time.h>

//
// PDIF : differential current protection; will trip if difference in incoming current is too big in relation to outgoing current. result should be 0
//
typedef struct sPDIF
{
  IedServer server;
  DataAttribute *Op_general;
  void *Op_general_callback;
  Input *input;
  int tripTimer;
  bool trip;
  DSP *dspI1;
  DSP *dspI2;
} PDIF;


// callback when SMV is received
void PDIF_callback_SMV(void *pdif_inst)
{
  PDIF *inst = pdif_inst;
  int i = 0;
  while (i < 4) // only trigger on amps.
  {
    double AmpValue1  =  DSP_get_phs(inst->dspI1, i); // get absolute current from dsp
    double AmpValue2 =  DSP_get_phs(inst->dspI2, i); // get absolute current from dsp
        // check if value is outside allowed band
        // TODO: get values from settings
    if( (AmpValue1 - AmpValue2) > 5000 || (AmpValue1 - AmpValue2) < -5000 )
    {
      printf("PDIF: treshold reached\n");
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
    // printf("PDIF: treshold NOT reached\n");
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

void * PDIF_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  PDIF *inst = (PDIF *)malloc(sizeof(PDIF)); // create new instance with MALLOC
  inst->server = server;
  inst->tripTimer = 0;
  inst->trip = false;
  inst->Op_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Op.general"); // the node to operate on
  inst->Op_general_callback = _findAttributeValueEx(inst->Op_general, allInputValues);
  inst->input = input;
  inst->dspI1 = NULL;
  inst->dspI2 = NULL;

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {

      if (strcmp(extRef->intAddr, "PDIF_Amp1_1") == 0)
      {
        inst->dspI1 = init_dsp_I(server, extRef);//this is to reference the first extref
      }
      if (strcmp(extRef->intAddr, "PDIF_Amp3_1") == 0) // find extref for the last SMV phase, using the intaddr, so that all values are updated, we ignore nutral in case we have 3 phase, and neutral is calculated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(inst->dspI1);
        extRef->callBackParam = inst->dspI1;
      }

      if (strcmp(extRef->intAddr, "PDIF_Amp1_2") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        inst->dspI2 = init_dsp_I(server, extRef);//this is to reference the first extref
        DSP_add_callback_on_update(inst->dspI2,PDIF_callback_SMV, inst);//called when DSP has processed data
      }
      if (strcmp(extRef->intAddr, "PDIF_Amp3_2") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(inst->dspI2);
        extRef->callBackParam = inst->dspI2;
      }
      extRef = extRef->sibling;
    }
  }
  return inst;
}
