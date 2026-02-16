#include "iec61850_model_extensions.h"
#include "inputs_api.h"

#define CILO_MAX_INPUT 16

typedef struct sCILO
{
  IedServer server;
  bool EnaOpn;
  bool EnaCls;
  DataAttribute *EnaOpn_DA;
  void *EnaOpn_callback;
  DataAttribute *EnaCls_DA;
  void *EnaCls_callback;


  bool and_values[CILO_MAX_INPUT];
  uint32_t and_values_count;
  bool or_values[CILO_MAX_INPUT];
  uint32_t or_values_count;
  bool nand_values[CILO_MAX_INPUT];
  uint32_t nand_values_count;
  bool nor_values[CILO_MAX_INPUT];
  uint32_t nor_values_count;

} CILO;

bool ParsePos(const MmsValue *pos)
{
  MmsType type = MmsValue_getType(pos);
  if(type == MMS_BOOLEAN){
    return MmsValue_getBoolean(pos);
  }
  if(type == MMS_BIT_STRING){
    Dbpos dbpos = Dbpos_fromMmsValue(pos);
    if (dbpos == DBPOS_OFF) // XCBR/XSWI is open, so its safe
    {
      return false;
    }
    else // If XCBR is moving, or closed, assumen its closed(i.e not safe)
    {
      return true;
    }
  }
  printf("ERROR: CILO Cannot parse position of type: %d, state set to 'false'\n", type);
  return false;
}

void SetEnaOpn(CILO * inst,bool state)
{
  printf("CILO.SetEnaOpn = %d\n", state);
  MmsValue *open = MmsValue_newBoolean(state);  // false = XSWI/XCBR cannot open, true = XSWI/XCBR can open

  IedServer_updateAttributeValue(inst->server, inst->EnaOpn_DA, open);
  InputValueHandleExtensionCallbacks(inst->EnaOpn_callback); // update the associated callbacks with this Data Element

  MmsValue_delete(open);
  inst->EnaOpn = state;
}

void SetEnaCls(CILO * inst,bool state)
{
  printf("CILO.SetEnaCls = %d\n", state);
  MmsValue *close = MmsValue_newBoolean(state); // fasle = XSWI/XCBR cannot open, true = XSWI/XCBR can open

  IedServer_updateAttributeValue(inst->server, inst->EnaCls_DA, close);
  InputValueHandleExtensionCallbacks(inst->EnaCls_callback); // update the associated callbacks with this Data Element

  MmsValue_delete(close);
  inst->EnaCls = state;
}

bool AND_inputs_all_true(CILO * inst) // all values are true means block operation, any value false means allow
{
  if(inst->and_values_count == 0) // ignore this logic if not used, by always returning false for blocking
    false;

  for(uint32_t i = 0; i < inst->and_values_count; i++) {
    if(inst->and_values[i] == false)
      return false; // not blocking
  }
  return true; // blocking
}

bool NAND_result(CILO * inst) // all values are true means allow operation, any value false means block
{
  if(inst->nand_values_count == 0) // ignore this logic if not used, by always returning false for blocking
    false;

  for(uint32_t i = 0; i < inst->nand_values_count; i++) {
    if(inst->nand_values[i] == false)
      return true; // blocking
  }
  return false; // not blocking
}

bool any_OR_input_true(CILO * inst) // any value true means block operation, all values false means allow
{
  if(inst->or_values_count == 0) // ignore this logic if not used, by always returning false for blocking
    false;

  for(uint32_t i = 0; i < inst->or_values_count; i++) {
    if(inst->or_values[i] == true)
      return true; // blocking
  }
  return false; // not blocking
}

bool NOR_result(CILO * inst) // any values are true means allow operation, all value false means block
{
  if(inst->nor_values_count == 0) // ignore this logic if not used, by always returning false for blocking
    false;

  for(uint32_t i = 0; i < inst->nor_values_count; i++) {
    if(inst->nor_values[i] == true)
      return false; // not blocking
  }
  return true; // blocking
}

void process_all_conditions(CILO * inst)
{
  bool Block = AND_inputs_all_true(inst) || any_OR_input_true(inst) || NAND_result(inst) || NOR_result(inst);
  bool Ena = !Block;
  if(Ena != inst->EnaOpn)
    SetEnaOpn(inst,Ena); // invert state, so an DBPOS_OFF switch(false) will set EnaOpn
  if(Ena != inst->EnaCls)
    SetEnaCls(inst,Ena); // invert state, so an DBPOS_OFF switch(false) will set EnaCls
}


// receive status from any circuit breaker
void CILO_not_callback(InputEntry *extRef)
{
  CILO *inst = extRef->callBackParam;

  if (extRef->value != NULL && inst != NULL)
  { 
    bool desired_state = !ParsePos(extRef->value); // processing of state, in this case only NOT
    if(desired_state != inst->EnaOpn)
      SetEnaOpn(inst,desired_state); // invert state, so an DBPOS_OFF switch(false) will set EnaOpn
    if(desired_state != inst->EnaCls)
      SetEnaCls(inst,desired_state); // invert state, so an DBPOS_OFF switch(false) will set EnaCls
  }
}

void CILO_and_callback(InputEntry *extRef) // all switch = true, will result in EnaOpn+EnaCls = false, 
                                           // any switch = false, will result in EnaOpn+EnaCls = true
{
  CILO *inst = extRef->callBackParam;
  if (extRef->value != NULL && inst != NULL) {
    int32_t index = extract_last_index(extRef->intAddr);// get index
    if(index != -1)
    {
      inst->and_values[index] = ParsePos(extRef->value);
      process_all_conditions(inst);
    }
  }
}

void CILO_nand_callback(InputEntry *extRef) // all switch = true, will result in EnaOpn+EnaCls = true,
                                            // any switch false, will result in EnaOpn+EnaCls = false
{
  CILO *inst = extRef->callBackParam;
  if (extRef->value != NULL && inst != NULL) {
    int32_t index = extract_last_index(extRef->intAddr);// get index
    if(index != -1)
    {
      inst->nand_values[index] = ParsePos(extRef->value);
      process_all_conditions(inst);
    }
  }
}

void CILO_or_callback(InputEntry *extRef) // any switch = true will result in EnaOpn+EnaCls = false, 
                                          // all switch = false, will result in EnaOpn+EnaCls = true
{
  CILO *inst = extRef->callBackParam;
  if (extRef->value != NULL && inst != NULL) {
    int32_t index = extract_last_index(extRef->intAddr);// get index
    if(index != -1)
    {
      inst->or_values[index] = ParsePos(extRef->value);
      process_all_conditions(inst);
    }
  }
}

void CILO_nor_callback(InputEntry *extRef) // any switch = true will result in EnaOpn+EnaCls = true
                                           // all switch = false, will result in EnaOpn+EnaCls = false
{
  CILO *inst = extRef->callBackParam;
  if (extRef->value != NULL && inst != NULL) {
    int32_t index = extract_last_index(extRef->intAddr);// get index
    if(index != -1)
    {
      inst->nor_values[index] = ParsePos(extRef->value);
      process_all_conditions(inst);
    }
  }
}


void * CILO_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  CILO *inst = (CILO *)malloc(sizeof(CILO)); // create new instance with MALLOC

  inst->server = server;
  inst->EnaOpn = true;
  inst->EnaCls = true;
  inst->EnaOpn_DA = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "EnaOpn.stVal");
  inst->EnaOpn_callback = _findAttributeValueEx(inst->EnaOpn_DA, allInputValues);
  inst->EnaCls_DA = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "EnaCls.stVal");
  inst->EnaCls_callback = _findAttributeValueEx(inst->EnaCls_DA, allInputValues);

  for(uint32_t i = 0; i < CILO_MAX_INPUT; i++) {
    inst->and_values[i] = false;
    inst->or_values[i] = false;
    inst->nand_values[i] = false;
    inst->nor_values[i] = false;
  }
  inst->and_values_count = 0;
  inst->or_values_count = 0;
  inst->nand_values_count = 0;
  inst->nor_values_count = 0;

  // find extref for the last SMV, using the intaddr
  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      // receive status of associated XCBR
      if (strcmp(extRef->intAddr, "stval") == 0) // direct logic, inverse of value is output
      {
        extRef->callBack = (callBackFunction)CILO_not_callback;
        extRef->callBackParam = inst;
      }

      if (strncmp(extRef->intAddr, "in_or_",6) == 0)
      {
        extRef->callBack = (callBackFunction)CILO_or_callback;
        extRef->callBackParam = inst;
        inst->or_values_count++;
      }
      if (strncmp(extRef->intAddr, "in_nor_",7) == 0)
      {
        extRef->callBack = (callBackFunction)CILO_nor_callback;
        extRef->callBackParam = inst;
        inst->nor_values_count++;
      }
      if (strncmp(extRef->intAddr, "in_and_",7) == 0)
      {
        extRef->callBack = (callBackFunction)CILO_and_callback;
        extRef->callBackParam = inst;
        inst->and_values_count++;
      }
      if (strncmp(extRef->intAddr, "in_nand_",8) == 0)
      {
        extRef->callBack = (callBackFunction)CILO_nand_callback;
        extRef->callBackParam = inst;
        inst->nand_values_count++;
      }

      extRef = extRef->sibling;
    }
  }
  return inst;
}
