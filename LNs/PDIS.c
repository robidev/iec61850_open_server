#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h>
// #include "../static_model.h"
#include "PDIS.h"
#include "dsp.h"
#include <time.h>


//
// PDIS : distance protection; measures current into a line, and out of the line. when it deviates, trip
//
typedef struct sPDIS
{
  IedServer server;
  DataAttribute *Op_general;
  void *Op_general_callback;
  Input *input;
  int tripTimer;
  bool trip;
  DSP *dspI;
  DSP *dspU;
} PDIS;

// callback when GOOSE is received
void PDIS_callback_GOOSE(InputEntry *extRef)
{
  PDIS *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {
    // char printBuf[1024];

    // MmsValue_printToBuffer(extRef->value, printBuf, 1024);
    // printf("PDIS: Received Breaker position: %s\n", printBuf);
  }
}

// callback when SMV is received
void PDIS_callback_SMV(void *pdis_inst)
{
  PDIS *inst = pdis_inst;
  int i = 0;

  while(i < 4)
  {
    double AmpValue  =  DSP_get_phs(inst->dspI, i); // get absolute current from dsp
    double VoltValue =  DSP_get_phs(inst->dspU, i); // get absolute current from dsp

    if(VoltValue != 0.0 && AmpValue != 0.0 && ( VoltValue / AmpValue) > 500 )
    {
      printf("PDIS: treshold reached\n");
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
    // printf("PDIS: treshold NOT reached\n");
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

void * PDIS_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  PDIS *inst = (PDIS *)malloc(sizeof(PDIS)); // create new instance with MALLOC
  inst->server = server;
  inst->tripTimer = 0;
  inst->trip = false;
  inst->Op_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Op.general"); // the node to operate on
  inst->Op_general_callback = _findAttributeValueEx(inst->Op_general, allInputValues);
  inst->input = input;
  inst->dspI = NULL;
  inst->dspU = NULL;

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "PDIS_Amp1") == 0)
      {
        inst->dspI = init_dsp_I(server, extRef);//this is to reference the first extref
        //we only call after voltage is processed(usually last)
      }
      if (strcmp(extRef->intAddr, "PDIS_Amp3") == 0) // find extref for the last SMV phase, using the intaddr, so that all values are updated, we ignore nutral in case we have 3 phase, and neutral is calculated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(inst->dspI);
        extRef->callBackParam = inst->dspI;
      }
      if (strcmp(extRef->intAddr, "PDIS_Vol1") == 0)
      {
        inst->dspU = init_dsp_U(server, extRef);//this is to reference the first extref
        DSP_add_callback_on_update(inst->dspU,PDIS_callback_SMV, inst);//called when DSP has processed data
      }
      if (strcmp(extRef->intAddr, "PDIS_Vol3") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(inst->dspU);
        extRef->callBackParam = inst->dspU;
      }
      if (strcmp(extRef->intAddr, "PDIS_xcbr_stval") == 0)
      {
        extRef->callBack = (callBackFunction)PDIS_callback_GOOSE; // TODO: replace GOOSE with status
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }
  return inst;
}
