#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h>
// #include "../static_model.h"
#include "PDIS.h"

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
void PDIS_callback_SMV(InputEntry *extRef)
{
  PDIS *inst = extRef->callBackParam;
  extRef = inst->input->extRefs; // start from the first extref, and check all values
  int i = 0;
  int64_t AmpValues[4];

  while (extRef != NULL)
  {
    if (strcmp(extRef->intAddr, "xcbr_stval") != 0 && extRef->value != NULL) // perform for all items except xcbr_stval (meaning: all SMV)
    {
      if (i < 4) // get the amps
      {
        MmsValue *stVal = MmsValue_getElement(extRef->value, 0);
        AmpValues[i] =  MmsValue_toInt64(stVal);
      }
      else if(i < 8) // get the volts
      {
        MmsValue *stVal = MmsValue_getElement(extRef->value, 0);
        // check if value is outside allowed band
        // TODO: get values from settings
        int64_t VoltValue =  MmsValue_toInt64(stVal);
        if(VoltValue != 0.0 && AmpValues[i % 4] != 0.0 && ( VoltValue / AmpValues[i % 4]) < 500 )
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
      }
      i++;
    }
    extRef = extRef->sibling;
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

void PDIS_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  PDIS *inst = (PDIS *)malloc(sizeof(PDIS)); // create new instance with MALLOC
  inst->server = server;
  inst->tripTimer = 0;
  inst->trip = false;
  inst->Op_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Op.general"); // the node to operate on
  inst->Op_general_callback = _findAttributeValueEx(inst->Op_general, allInputValues);
  inst->input = input;

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "Vol3") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)PDIS_callback_SMV; // TODO: replace smv with samples
        extRef->callBackParam = inst;
      }
      if (strcmp(extRef->intAddr, "xcbr_stval") == 0)
      {
        extRef->callBack = (callBackFunction)PDIS_callback_GOOSE; // TODO: replace GOOSE with status
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }
}
