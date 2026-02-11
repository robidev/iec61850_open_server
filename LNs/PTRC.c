#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "PTRC.h"

typedef struct sPTRC
{
  IedServer server;
  DataAttribute *Tr_general;
  void *Tr_general_callback;//Trip command to breaker
  bool tripstate;
  bool Strstate;
  DataAttribute *Op_general;//operation, agregated from sources
  void *Op_general_callback;
  DataAttribute *Str_general;//Start(fault), agregated from sources
  void *Str_general_callback;
  InputEntry *extRefs;
} PTRC;

// receive trip command from input LN's
void PTRC_input_Tr_callback(InputEntry *extRef)
{
  PTRC *inst = extRef->callBackParam;

  InputEntry *firstExtRef = inst->extRefs;

  while (firstExtRef != NULL)
  {
    if (firstExtRef->intAddr != NULL && strncmp(firstExtRef->intAddr, "Op", 2) == 0)
    {
      if(firstExtRef->value == NULL){ // remote values may be uninitialised, so skip them
        firstExtRef = firstExtRef->sibling;
        continue;
      }

      if (MmsValue_getBoolean(firstExtRef->value) == true && inst->tripstate == false)  // if any of the registered Op values is true, and not yet tripped
      {
        printf("PTRC: trip from Op: %s\n", firstExtRef->Ref); //
        MmsValue *tripValue = MmsValue_newBoolean(true);
        IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue); // set the combined Op values
        InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element

        IedServer_updateAttributeValue(inst->server, inst->Tr_general, tripValue);
        InputValueHandleExtensionCallbacks(inst->Tr_general_callback); // update the associated callbacks with this Data Element
        MmsValue_delete(tripValue);
        inst->tripstate = true;
        return;
      }
    }
    firstExtRef = firstExtRef->sibling;
  }
  // we reach here if none of the Op values are currently True
  printf("PTRC: trip cleared from Op\n"); //
  MmsValue *tripValue = MmsValue_newBoolean(false);

  IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue); // set the combined Op values
  InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element

  IedServer_updateAttributeValue(inst->server, inst->Tr_general, tripValue);
  InputValueHandleExtensionCallbacks(inst->Tr_general_callback); // update the associated callbacks with this Data Element
  MmsValue_delete(tripValue);
  inst->tripstate = false;
}

// receive trip command from input LN's
void PTRC_input_Str_callback(InputEntry *extRef)
{
  PTRC *inst = extRef->callBackParam;

  InputEntry *firstExtRef = inst->extRefs;

  while (firstExtRef != NULL)
  {
    if (firstExtRef->intAddr != NULL && strncmp(firstExtRef->intAddr, "Str", 3) == 0)
    {
      if(firstExtRef->value == NULL){ // remote values may be uninitialised, so skip them
        firstExtRef = firstExtRef->sibling;
        continue;
      }

      if (MmsValue_getBoolean(firstExtRef->value) == true && inst->Strstate == false)  // if any of the registered Op values is true, and not yet tripped
      {
        printf("PTRC: fault from Str: %s\n", firstExtRef->Ref); //
        MmsValue *StrValue = MmsValue_newBoolean(true);
        IedServer_updateAttributeValue(inst->server, inst->Str_general, StrValue); // set the combined Op values
        InputValueHandleExtensionCallbacks(inst->Str_general_callback); // update the associated callbacks with this Data Element
        MmsValue_delete(StrValue);
        inst->Strstate = true;
        return;
      }
    }
    firstExtRef = firstExtRef->sibling;
  }
  // we reach here if none of the Op values are currently True
  printf("PTRC: fault cleared from Str\n"); //
  MmsValue *StrValue = MmsValue_newBoolean(false);

  IedServer_updateAttributeValue(inst->server, inst->Str_general, StrValue); // set the combined Op values
  InputValueHandleExtensionCallbacks(inst->Str_general_callback); // update the associated callbacks with this Data Element

  MmsValue_delete(StrValue);
  inst->Strstate = false;
}

void * PTRC_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  PTRC *inst = (PTRC *)malloc(sizeof(PTRC)); // create new instance with MALLOC
  inst->server = server;
  inst->tripstate = false;
  inst->Strstate = false;
  inst->extRefs = input->extRefs;

  inst->Tr_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Tr.general"); // the trip value, that is triggered via internal trip conditioning
  inst->Tr_general_callback = _findAttributeValueEx(inst->Tr_general, allInputValues);
  inst->Op_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Op.general"); // combined Op values connected to this PTRC
  inst->Op_general_callback = _findAttributeValueEx(inst->Op_general, allInputValues);
  inst->Str_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Str.general"); // combined Str values connected to this PTRC
  inst->Str_general_callback = _findAttributeValueEx(inst->Op_general, allInputValues);
  // find extref for the input signals for this LN
  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      // subscribed to Op signal of Protection;
      if (extRef->intAddr != NULL &&
              strncmp(extRef->intAddr, "Op", 2) == 0)
      {
        extRef->callBack = (callBackFunction)PTRC_input_Tr_callback; // callback to trigger when Op_x is set
        extRef->callBackParam = inst;
      }

      // subscribed to Op signal of Protection; Time Over Current
      if (extRef->intAddr != NULL &&
              strncmp(extRef->intAddr, "Str", 3) == 0)
      {
        extRef->callBack = (callBackFunction)PTRC_input_Str_callback; // callback to trigger when Op_x is set
        extRef->callBackParam = inst;
      }

      extRef = extRef->sibling;
    }
  }
  return inst;
}
