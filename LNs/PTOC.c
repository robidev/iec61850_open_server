#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h>
// #include "../static_model.h"
#include "PTOC.h"

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
} PTOC;

// callback when GOOSE is received
void PTOC_callback_GOOSE(InputEntry *extRef)
{
  PTOC *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {
    // char printBuf[1024];

    // MmsValue_printToBuffer(extRef->value, printBuf, 1024);
    // printf("PTOC: Received Breaker position: %s\n", printBuf);
  }
}

// callback when SMV is received
void PTOC_callback_SMV(InputEntry *extRef)
{
  PTOC *inst = extRef->callBackParam;
  extRef = inst->input->extRefs; // start from the first extref, and check all values
  int i = 0;
  while (extRef != NULL)
  {
    if (strcmp(extRef->intAddr, "xcbr_stval") != 0 && extRef->value != NULL) // perform for all items except xcbr_stval (meaning: all SMV)
    {
      if (i < 4) // only trigger on amps. TODO: ensure it only triggers on Amps lnrefs, instead of relying on the order in the SCD file
      {
        MmsValue *stVal = MmsValue_getElement(extRef->value, 0);// for datasets?
        if(stVal == NULL)
        {
          stVal = extRef->value;
        }
        int64_t current = llabs( MmsValue_toInt64(stVal) );

        msSinceEpoch time = Hal_getTimeInMs();
        msSinceEpoch delta_t = time - inst->prevTime;
        inst->prevTime = time;

        // check if value is outside allowed band
        // TODO: get values from settings
        if (current > 500)
        {
          printf("PTOC: treshold reached by immediate overcurrent\n");
          MmsValue *tripValue = MmsValue_newBoolean(true);

          IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue);
          InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element

          MmsValue_delete(tripValue);
          inst->tripTimer = 0;
          inst->trip = true;
          // if so send to internal PTRC
        }
        else if (current> 400 )// lineair time overcurrent
        {
          inst->overCurrent += (current - 400) * delta_t;
          if( inst->overCurrent > 100 )
          {
            printf("PTOC: treshold reached by time overcurrent\n");
            MmsValue *tripValue = MmsValue_newBoolean(true);

            IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue);
            InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element

            MmsValue_delete(tripValue);
            inst->tripTimer = 0;
            inst->trip = true;
          }
        }
        else if(inst->overCurrent > 0)
        {
          inst->overCurrent += (current - 400) * delta_t;
          if(inst->overCurrent < 0)
            inst->overCurrent = 0;
        }
      }
      i++;
    }
    extRef = extRef->sibling;
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

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "PTOC_Amp3") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)PTOC_callback_SMV; // TODO: replace smv with samples
        extRef->callBackParam = inst;
      }
      if (strcmp(extRef->intAddr, "PTOC_xcbr_stval") == 0)
      {
        extRef->callBack = (callBackFunction)PTOC_callback_GOOSE; // TODO: replace GOOSE with status
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }
  return inst;
}
