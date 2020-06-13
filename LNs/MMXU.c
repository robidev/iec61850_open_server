#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <math.h>

typedef struct sMMXU
{
  IedServer server;
  Input* input;

  void *da_A;
  void *da_V;

  void * da_A_callback;
  void * da_V_callback;

  float RMS[8];
  int RMS_samplecount;

} MMXU;

//callback when SMV is received
void MMXU_callback(InputEntry* extRef)
{
  MMXU* inst = extRef->callBackParam;
  extRef = inst->input->extRefs;//start from the first extref, and check all values, we assume there are 8!
  int i = 0;
  while(extRef != NULL )
  {
    if(extRef->value != NULL)
    {
      if( (inst->RMS_samplecount % 80) == 0)//every 80 samples we start fresh
      {
        inst->RMS[i] = 0;//start over
      }
      //calculate RMS value TODO: check correct amount of elements instead of assuming 8, and offload this into a separate thread
      //currently, it is called each time a sampled-value is updated which might become slow
      float ff = (float)MmsValue_toInt32(extRef->value);
      inst->RMS[i] += (ff * ff);

      if( (inst->RMS_samplecount % 80) == 79)//we calculate the average after 80 samples
      {
        inst->RMS[i] /= 80;
        inst->RMS[i] = sqrt(inst->RMS[i]);

        if(i==3){
          float a = (inst->RMS[0] + inst->RMS[1] + inst->RMS[2]) / 3;
          IedServer_updateFloatAttributeValue(inst->server,inst->da_A, a/1000 );
          InputValueHandleExtensionCallbacks(inst->da_A_callback); //update the associated callbacks with this Data Element 
        }
        if(i==7){
          float v = (inst->RMS[4] + inst->RMS[5] + inst->RMS[6]) / 3;
          IedServer_updateFloatAttributeValue(inst->server,inst->da_V, v/100 );
          InputValueHandleExtensionCallbacks(inst->da_V_callback); //update the associated callbacks with this Data Element 
        }
        
      }
      i++;
    }
    extRef = extRef->sibling;
  }
  inst->RMS_samplecount++;
}

void *MMXU_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues )
{
  MMXU* inst = (MMXU *) malloc(sizeof(MMXU));//create new instance with MALLOC

  inst->RMS_samplecount = 0;
  inst->server = server;
  inst->input = input;
  inst->da_A = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "AvAPhs.mag.f");//the node to operate on
  inst->da_A_callback = _findAttributeValueEx(inst->da_A, allInputValues);
  inst->da_V = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "AvPhVPhs.mag.f");//the node to operate on
  inst->da_V_callback = _findAttributeValueEx(inst->da_V, allInputValues);

  if(input != NULL)
  {
    InputEntry* extRef = input->extRefs;

    while(extRef != NULL)
    {
      if(strcmp(extRef->intAddr,"Vol4") == 0)//find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction) MMXU_callback;
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }

  return inst;
}