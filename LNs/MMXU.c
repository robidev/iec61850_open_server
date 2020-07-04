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
  int RMS_samplecountV;
  int RMS_samplecountI;

} MMXU;

//callback when SMV is received
void MMXU_callbackI(InputEntry* extRef)
{
  MMXU* inst = extRef->callBackParam;
  extRef = inst->input->extRefs;//start from the first extref, and check all values, we assume there are 8!
  int i = 0;
  float a;
  int peakval [8] = {0,0,0,0,0,0,0,0};
  while(extRef != NULL )
  {
    if(extRef->value != NULL)
    {
      if(i < 4 )
      {
	      if( (inst->RMS_samplecountI % 80) == 0)//every 80 samples we start fresh
	      {
		inst->RMS[i] = 0;//start over
	      }
	      //calculate RMS value TODO: check correct amount of elements instead of assuming 8, and offload this into a separate thread
	      //currently, it is called each time a sampled-value is updated which might become slow
              peakval[i] = MmsValue_toInt32(extRef->value);
	      float ff = (float)peakval[i];
	      inst->RMS[i] += (ff * ff);
              
              if(i == 3 ){
		if( peakval[i] == 0){
                  peakval[i] = peakval[0] + peakval[1] + peakval[2];
                  inst->RMS[i] = (float)(peakval[i] * peakval[i]);
                  //printf("+null: %i\n",peakval[i]);
		}
		//else
		   //printf("_null: %i\n",peakval[i]);
              }
	      

	      if( (inst->RMS_samplecountI % 80) == 79)//we calculate the average after 80 samples
	      {
		inst->RMS[i] /= 80;
		inst->RMS[i] = sqrt(inst->RMS[i]);
		
		if(i==3){
		  a = (inst->RMS[0] + inst->RMS[1] + inst->RMS[2]) / 3;
		  IedServer_updateFloatAttributeValue(inst->server,inst->da_A, a );
		  InputValueHandleExtensionCallbacks(inst->da_A_callback); //update the associated callbacks with this Data Element 
		  break;
		}       
	      }
      }
      i++;
    }
    extRef = extRef->sibling;
  }
  inst->RMS_samplecountI++;
}

//callback when SMV is received
void MMXU_callbackV(InputEntry* extRef)
{
  MMXU* inst = extRef->callBackParam;
  extRef = inst->input->extRefs;//start from the first extref, and check all values, we assume there are 8!
  int i = 0;
  float v;
  while(extRef != NULL )
  {
    if(extRef->value != NULL)
    {
      if(i >= 4 )
      {
	      if( (inst->RMS_samplecountV % 80) == 0)//every 80 samples we start fresh
	      {
		inst->RMS[i] = 0;//start over
	      }
	      //calculate RMS value TODO: check correct amount of elements instead of assuming 8, and offload this into a separate thread
	      //currently, it is called each time a sampled-value is updated which might become slow
	      float ff = (float)MmsValue_toInt32(extRef->value);
	      inst->RMS[i] += (ff * ff);

	      if( (inst->RMS_samplecountV % 80) == 79)//we calculate the average after 80 samples
	      {
		inst->RMS[i] /= 80;
		inst->RMS[i] = sqrt(inst->RMS[i]);
		
		if(i==7){
		  v = (inst->RMS[4] + inst->RMS[5] + inst->RMS[6]) / 3;
		  IedServer_updateFloatAttributeValue(inst->server,inst->da_V, v );
		  InputValueHandleExtensionCallbacks(inst->da_V_callback); //update the associated callbacks with this Data Element 
		  //printf("mmxu updated: a= %f, v= %f\n",a,v);
		}
		
	      }
      }
      i++;
    }
    extRef = extRef->sibling;
  }
  inst->RMS_samplecountV++;
}

void *MMXU_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues )
{
  MMXU* inst = (MMXU *) malloc(sizeof(MMXU));//create new instance with MALLOC

  inst->RMS_samplecountI = 0;
  inst->RMS_samplecountV = 0;
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
      if(strcmp(extRef->intAddr,"Amp3") == 0)//find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction) MMXU_callbackI;
        extRef->callBackParam = inst;
      }
      if(strcmp(extRef->intAddr,"Vol3") == 0)//find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction) MMXU_callbackV;
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }
  //printf("mmxu init\n");
  return inst;
}
