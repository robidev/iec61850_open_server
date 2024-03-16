#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <math.h>

typedef struct sMMXU
{
  IedServer server;
  Input *input;

  void *da_A;
  void *da_V;

  void *da_A_callback;
  void *da_V_callback;

  void *da_A_phsAng[4];

  void *da_A_phs[4];
  void *da_A_phs_callback[4];
  void *da_V_phs[4];
  void *da_V_phs_callback[4];

  float RMS[8];
  int RMS_samplecountV;
  int RMS_samplecountI;

  double **xn;
  double Xr[4];
  double Xi[4];
	int sample_index;
} MMXU;

const double INTERESTED_FREQ = 50;
const double SAMPLE_FREQ = 4000;
const uint32_t WINDOW_SIZE = 80; // amount of samples im the window-size
const double const_Rms = 0.7071;

void MMXU_I_DFT(InputEntry *extRef)
{
  MMXU *inst = extRef->callBackParam;
  extRef = inst->input->extRefs; // start from the first extref, and check all values, we assume there are 8!
  int i = 0;
  double Ni=0, Nr=0;
  double AvgAmp=0;

  while (extRef != NULL)
  {
    if (extRef->value != NULL)
    {
      if (i < 4)
      {
        double k=INTERESTED_FREQ / (SAMPLE_FREQ / WINDOW_SIZE);

        if(1)//calculate dft every WINDOW_SIZE (e.g. 80) cycles. this means low latency, but the values are updated only once per cycle
        {
          double multiplier = 0.5 * (1 - cos( 2 * M_PI * inst->sample_index / WINDOW_SIZE));//Hanning window
          inst->Xr[i] = (inst->Xr[i] +  MmsValue_toInt32(extRef->value) * multiplier * cos(2 * M_PI * k * (double)inst->sample_index / WINDOW_SIZE));
          inst->Xi[i] = (inst->Xi[i] -  MmsValue_toInt32(extRef->value) * multiplier * sin(2 * M_PI * k * (double)inst->sample_index / WINDOW_SIZE));
          //k * (SAMPLE_FREQ / WINDOW_SIZE), Xr/WINDOW_SIZE, Xi/WINDOW_SIZE, amplitude/(WINDOW_SIZE)*4, angle);
          if ((inst->sample_index % WINDOW_SIZE) == WINDOW_SIZE-1) // we calculate the dft vector after WINDOW_SIZE samples
          {
            if(i < 3)
            {
              //calculate neutral by adding other vectors
              inst->Xi[3] += inst->Xi[i];
              inst->Xr[3] += inst->Xr[i];
            }
            double amplitude = sqrt((inst->Xr[i]*inst->Xr[i]) + (inst->Xi[i]*inst->Xi[i]))/(WINDOW_SIZE)*4;
            IedServer_updateFloatAttributeValue(inst->server, inst->da_A_phs[ i % 4 ],amplitude * const_Rms);
            InputValueHandleExtensionCallbacks(inst->da_A_phs_callback[i % 4]); // update the associated callbacks with this Data Element

            double quadrant = 0;
            if(inst->Xr[i] < 0.0 ) quadrant = 180;
            if(inst->Xr[i] > 0.0 && inst->Xi[i] < 0.0) quadrant = 360;
            double angle = (atan(inst->Xi[i]/inst->Xr[i]) * (180/M_PI)) + quadrant;
            IedServer_updateFloatAttributeValue(inst->server, inst->da_A_phsAng[ i % 4 ],angle);

            AvgAmp += amplitude;
            if (i == 3)
            {
              IedServer_updateFloatAttributeValue(inst->server, inst->da_A, AvgAmp/3 * const_Rms);
              InputValueHandleExtensionCallbacks(inst->da_A_callback); // update the associated callbacks with this Data Element
            }
            inst->Xr[i] = 0;
            inst->Xi[i] = 0;
          }
        }
        else//calculate whole window every cycle
        {
          double Xr =0, Xi = 0;
          int n;
          inst->xn[i][inst->sample_index] = MmsValue_toInt32(extRef->value);
        
          for (n = 0; n < WINDOW_SIZE; n++) { //calculate 1 cycle(WINDOW_SIZE samples)
            double multiplier = 0.5 * (1 - cos( 2 * M_PI *n / WINDOW_SIZE));//Hanning window
            Xr = (Xr + inst->xn[i][(n + inst->sample_index) % WINDOW_SIZE] * multiplier * cos(2 * M_PI * k * (double)n / WINDOW_SIZE));
            Xi = (Xi - inst->xn[i][(n + inst->sample_index) % WINDOW_SIZE] * multiplier * sin(2 * M_PI * k * (double)n / WINDOW_SIZE));
          }
          double amplitude = sqrt((Xr*Xr) + (Xi*Xi))/(WINDOW_SIZE)*4;
          /*if(Xr < 0.0 ) quadrant = 180;
          if(Xr > 0.0 && Xi < 0.0) quadrant = 360;
          double angle = (atan(Xi/Xr) * (180/M_PI)) + quadrant;*/
          IedServer_updateFloatAttributeValue(inst->server, inst->da_A_phs[ i % 4 ],amplitude * const_Rms);
          InputValueHandleExtensionCallbacks(inst->da_A_phs_callback[i % 4]); // update the associated callbacks with this Data Element

          //calculate neutral
          Ni += Xi;
          Nr += Xr;
          if (i == 3)
          {
            float a = sqrt((Nr*Nr) + (Ni*Ni))/(WINDOW_SIZE * 3)*4;
            IedServer_updateFloatAttributeValue(inst->server, inst->da_A, a * const_Rms);
            InputValueHandleExtensionCallbacks(inst->da_A_callback); // update the associated callbacks with this Data Element
          }
        }
      }
      i++;
    }
    extRef = extRef->sibling;
  }
  inst->sample_index = (inst->sample_index + 1) % WINDOW_SIZE;
}

void MMXU_I_RMS(InputEntry *extRef)
{
  MMXU *inst = extRef->callBackParam;
  extRef = inst->input->extRefs; // start from the first extref, and check all values, we assume there are 8!
  int i = 0;
  float a;
  int peakval[8] = {0, 0, 0, 0, 0, 0, 0, 0};
  while (extRef != NULL)
  {
    if (extRef->value != NULL)
    {
      if (i < 4)
      {
        if ((inst->RMS_samplecountI % 80) == 0) // every 80 samples we start fresh
        {
          inst->RMS[i] = 0; // start over
        }
        // calculate RMS value TODO: check correct amount of elements instead of assuming 8, and offload this into a separate thread
        // currently, it is called each time a sampled-value is updated which might become slow
        peakval[i] = MmsValue_toInt32(extRef->value);
        float ff = (float)peakval[i];
        inst->RMS[i] += (ff * ff);

        if (i == 3)
        {
          if (peakval[i] == 0)
          {
            peakval[i] = peakval[0] + peakval[1] + peakval[2];
            inst->RMS[i] = (float)(peakval[i] * peakval[i]);
            // printf("+null: %i\n",peakval[i]);
          }
          // else
          // printf("_null: %i\n",peakval[i]);
        }

        if ((inst->RMS_samplecountI % 80) == 79) // we calculate the average after 80 samples
        {
          inst->RMS[i] /= 80;
          inst->RMS[i] = sqrt(inst->RMS[i]);

          IedServer_updateFloatAttributeValue(inst->server, inst->da_A_phs[ i % 4 ], inst->RMS[i]);
          InputValueHandleExtensionCallbacks(inst->da_A_phs_callback[i % 4]); // update the associated callbacks with this Data Element

          if (i == 3)
          {
            a = (inst->RMS[0] + inst->RMS[1] + inst->RMS[2]) / 3;
            IedServer_updateFloatAttributeValue(inst->server, inst->da_A, a);
            InputValueHandleExtensionCallbacks(inst->da_A_callback); // update the associated callbacks with this Data Element
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

// callback when SMV is received
void MMXU_callbackI(InputEntry *extRef)
{
  if(0)
    MMXU_I_RMS(extRef);
  else
    MMXU_I_DFT(extRef);
}

void MMXU_V_DFT(InputEntry *extRef)
{

}


void MMXU_V_RMS(InputEntry *extRef)
{
  MMXU *inst = extRef->callBackParam;
  extRef = inst->input->extRefs; // start from the first extref, and check all values, we assume there are 8!
  int i = 0;
  float v;
  while (extRef != NULL)
  {
    if (extRef->value != NULL)
    {
      if (i >= 4)
      {
        if ((inst->RMS_samplecountV % 80) == 0) // every 80 samples we start fresh
        {
          inst->RMS[i] = 0; // start over
        }
        // calculate RMS value TODO: check correct amount of elements instead of assuming 8, and offload this into a separate thread
        // currently, it is called each time a sampled-value is updated which might become slow
        float ff = (float)MmsValue_toInt32(extRef->value);
        inst->RMS[i] += (ff * ff);

        if ((inst->RMS_samplecountV % 80) == 79) // we calculate the average after 80 samples
        {
          inst->RMS[i] /= 80;
          inst->RMS[i] = sqrt(inst->RMS[i]);

          IedServer_updateFloatAttributeValue(inst->server, inst->da_V_phs[ i % 4 ], inst->RMS[i]);
          InputValueHandleExtensionCallbacks(inst->da_V_phs_callback[i % 4]); // update the associated callbacks with this Data Element

          if (i == 7)
          {
            v = (inst->RMS[4] + inst->RMS[5] + inst->RMS[6]) / 3;
            IedServer_updateFloatAttributeValue(inst->server, inst->da_V, v);
            InputValueHandleExtensionCallbacks(inst->da_V_callback); // update the associated callbacks with this Data Element
            // printf("mmxu updated: a= %f, v= %f\n",a,v);
          }
        }
      }
      i++;
    }
    extRef = extRef->sibling;
  }
  inst->RMS_samplecountV++;
}

// callback when SMV is received
void MMXU_callbackV(InputEntry *extRef)
{
  MMXU_V_RMS(extRef);
}

void *MMXU_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  int i = 0;
  MMXU *inst = (MMXU *)malloc(sizeof(MMXU)); // create new instance with MALLOC

  inst->RMS_samplecountI = 0;
  inst->RMS_samplecountV = 0;
  inst->server = server;
  inst->input = input;
  inst->da_A = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "AvAPhs.mag.f"); // the node to operate on
  inst->da_A_callback = _findAttributeValueEx(inst->da_A, allInputValues);
  inst->da_V = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "AvPhVPhs.mag.f"); // the node to operate on
  inst->da_V_callback = _findAttributeValueEx(inst->da_V, allInputValues);

  inst->da_A_phs[0] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsA.cVal.mag.f"); // the node to operate on
  inst->da_A_phs_callback[0] = _findAttributeValueEx(inst->da_A, allInputValues);
  inst->da_A_phs[1] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsB.cVal.mag.f"); // the node to operate on
  inst->da_A_phs_callback[1] = _findAttributeValueEx(inst->da_A, allInputValues);
  inst->da_A_phs[2] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsC.cVal.mag.f"); // the node to operate on
  inst->da_A_phs_callback[2] = _findAttributeValueEx(inst->da_A, allInputValues);
  inst->da_A_phs[3] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.neut.cVal.mag.f"); // the node to operate on
  inst->da_A_phs_callback[3] = _findAttributeValueEx(inst->da_A, allInputValues);

  inst->da_A_phsAng[0] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsA.cVal.ang.f"); // the node to operate on
  inst->da_A_phsAng[1] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsB.cVal.ang.f"); // the node to operate on
  inst->da_A_phsAng[2] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.phsC.cVal.ang.f"); // the node to operate on
  inst->da_A_phsAng[3] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "A.neut.cVal.ang.f"); // the node to operate on

  inst->da_V_phs[0] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.phsA.cVal.mag.f"); // the node to operate on
  inst->da_V_phs_callback[0] = _findAttributeValueEx(inst->da_V, allInputValues);
  inst->da_V_phs[1] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.phsB.cVal.mag.f"); // the node to operate on
  inst->da_V_phs_callback[1] = _findAttributeValueEx(inst->da_V, allInputValues);
  inst->da_V_phs[2] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.phsC.cVal.mag.f"); // the node to operate on
  inst->da_V_phs_callback[2] = _findAttributeValueEx(inst->da_V, allInputValues);
  inst->da_V_phs[3] = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "PhV.neut.cVal.mag.f"); // the node to operate on
  inst->da_V_phs_callback[3] = _findAttributeValueEx(inst->da_V, allInputValues);

  inst->xn = malloc(4*sizeof(double *));
  inst->sample_index=0;
  for(i=0; i<4; i++)
  { 
    inst->Xr[i] = 0;
    inst->Xi[i] = 0;
    inst->xn[i] = malloc(WINDOW_SIZE*sizeof(double));
    memset(inst->xn[i], 0, WINDOW_SIZE*sizeof(double));
  }

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "MMXU_Amp3") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)MMXU_callbackI;
        extRef->callBackParam = inst;
      }
      if (strcmp(extRef->intAddr, "MMXU_Vol3") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)MMXU_callbackV;
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }

  // printf("mmxu init\n");
  return inst;
}
