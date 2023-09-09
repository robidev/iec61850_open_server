#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h>
// #include "../static_model.h"
#include "PDIF.h"

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
} PDIF;



// callback when GOOSE is received
void PDIF_callback_GOOSE(InputEntry *extRef)
{
  PDIF *inst = extRef->callBackParam;

  if (extRef->value != NULL)
  {
    // char printBuf[1024];

    // MmsValue_printToBuffer(extRef->value, printBuf, 1024);
    // printf("PDIF: Received Breaker position: %s\n", printBuf);
  }
}

// callback when SMV is received
void PDIF_callback_SMV(InputEntry *extRef)
{
  PDIF *inst = extRef->callBackParam;
  extRef = inst->input->extRefs; // start from the first extref, and check all values
  int i = 0;
  int64_t values[4];
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
        if(stVal != NULL)
        {
          values[i] =  MmsValue_toInt64(stVal);
        } 
        else 
        {
          printf("could not read %s value\n", extRef->Ref);
          values[i] = 0;
        }
        
      }
      else if(i < 8)
      {
        MmsValue *stVal = MmsValue_getElement(extRef->value, 0);// for datasets?
        if(stVal == NULL)
        {
          stVal = extRef->value;
        }
        int64_t local_values = 0;
        if(stVal != NULL)
        {
          local_values =  MmsValue_toInt64(stVal);
        } 
        else 
        {
          printf("could not read %s value\n", extRef->Ref);
        }
        // check if value is outside allowed band
        // TODO: get values from settings
        if( (local_values - values[i % 4]) > 5000 || (local_values - values[i % 4]) < -5000 )
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
      }
      i++;
    }
    extRef = extRef->sibling;
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

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "PDIF_Amp3_2") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)PDIF_callback_SMV; // TODO: replace smv with samples
        extRef->callBackParam = inst;
      }
      if (strcmp(extRef->intAddr, "PDIF_xcbr_stval") == 0)
      {
        extRef->callBack = (callBackFunction)PDIF_callback_GOOSE; // TODO: replace GOOSE with status
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }
  return inst;
}
