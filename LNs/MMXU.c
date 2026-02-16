#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "dsp.h"
#include "MMXU.h"

void *MMXU_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  MMXU *inst = (MMXU *)malloc(sizeof(MMXU)); // create new instance with MALLOC

  inst->server = server;
  inst->input = input;
  inst->da_A = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "AvAPhs.mag.f"); // the node to operate on
  inst->da_A_callback = _findAttributeValueEx(inst->da_A, allInputValues);
  inst->da_V = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "AvPhVPhs.mag.f"); // the node to operate on
  inst->da_V_callback = _findAttributeValueEx(inst->da_V, allInputValues);

  inst->da_A_phs[0] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsA.cVal.mag.f"); // the node to operate on
  inst->da_A_phs_callback[0] = _findAttributeValueEx(inst->da_A_phs[0], allInputValues);
  inst->da_A_phs[1] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsB.cVal.mag.f"); // the node to operate on
  inst->da_A_phs_callback[1] = _findAttributeValueEx(inst->da_A_phs[1], allInputValues);
  inst->da_A_phs[2] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsC.cVal.mag.f"); // the node to operate on
  inst->da_A_phs_callback[2] = _findAttributeValueEx(inst->da_A_phs[2], allInputValues);
  inst->da_A_phs[3] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.neut.cVal.mag.f"); // the node to operate on
  inst->da_A_phs_callback[3] = _findAttributeValueEx(inst->da_A_phs[3], allInputValues);

  inst->da_A_phsAng[0] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsA.cVal.ang.f"); // the node to operate on
  inst->da_A_phsAng[1] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsB.cVal.ang.f"); // the node to operate on
  inst->da_A_phsAng[2] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsC.cVal.ang.f"); // the node to operate on
  inst->da_A_phsAng[3] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.neut.cVal.ang.f"); // the node to operate on

  inst->da_V_phs[0] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.phsA.cVal.mag.f"); // the node to operate on
  inst->da_V_phs_callback[0] = _findAttributeValueEx(inst->da_V_phs[0], allInputValues);
  inst->da_V_phs[1] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.phsB.cVal.mag.f"); // the node to operate on
  inst->da_V_phs_callback[1] = _findAttributeValueEx(inst->da_V_phs[1], allInputValues);
  inst->da_V_phs[2] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.phsC.cVal.mag.f"); // the node to operate on
  inst->da_V_phs_callback[2] = _findAttributeValueEx(inst->da_V_phs[2], allInputValues);
  inst->da_V_phs[3] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.neut.cVal.mag.f"); // the node to operate on
  inst->da_V_phs_callback[3] = _findAttributeValueEx(inst->da_V_phs[3], allInputValues);

  inst->da_V_phsAng[0] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.phsA.cVal.ang.f"); // the node to operate on
  inst->da_V_phsAng[1] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.phsB.cVal.ang.f"); // the node to operate on
  inst->da_V_phsAng[2] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.phsC.cVal.ang.f"); // the node to operate on
  inst->da_V_phsAng[3] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.neut.cVal.ang.f"); // the node to operate on

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;
    DSP *dspI = NULL;
    DSP *dspU = NULL;
    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "MMXU_Amp1") == 0)
      {
        dspI = init_dsp_I(server, extRef);
        DSP_add_value_update_Average(dspI, inst->da_A, inst->da_A_callback);
        DSP_add_value_update_Phs(dspI, inst->da_A_phs, inst->da_A_phs_callback);
        DSP_add_value_update_PhsAng(dspI, inst->da_A_phsAng);//no callback
      }
      if (strcmp(extRef->intAddr, "MMXU_Amp3") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(dspI);
        extRef->callBackParam = dspI;
      }
      if (strcmp(extRef->intAddr, "MMXU_Vol1") == 0)
      {
        dspU = init_dsp_U(server, extRef);
        DSP_add_value_update_Average(dspU, inst->da_V, inst->da_V_callback);
        DSP_add_value_update_Phs(dspU, inst->da_V_phs, inst->da_V_phs_callback);
        DSP_add_value_update_PhsAng(dspU, inst->da_V_phsAng);//no callback
      }
      if (strcmp(extRef->intAddr, "MMXU_Vol3") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(dspU);
        extRef->callBackParam = dspU;
      }
      extRef = extRef->sibling;
    }
  }

  // printf("mmxu init\n");
  return inst;
}
