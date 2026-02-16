#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "dsp.h"
#include "mms_utilities.h"
#include <math.h>

extern const double INTERESTED_FREQ;
extern const double SAMPLE_FREQ;
extern const uint32_t WINDOW_SIZE;
const double const_Rms = 0.7071;

typedef struct sRMS
{
    float RMS[4];
    int RMS_samplecount;

} RMS;

void *init_rms()
{
    RMS *inst = (RMS *)malloc(sizeof(RMS)); // create new instance with MALLOC
    if(inst == NULL) return NULL;

    inst->RMS_samplecount = 0;
    return inst;
}

void destroy_rms()
{
  //TODO
}

void CALC_RMS(void * dsp)
{
  DSP *dsp_inst = dsp;
  RMS * inst = dsp_inst->dsp_data;

  InputEntry *extRef = dsp_inst->extRefs; // start from the first extref, and check all values, we assume there are 8!
  uint32_t i = 0;
  float a;
  int peakval[4] = {0, 0, 0, 0};
  while (extRef != NULL)
  {
    if (extRef->value != NULL)
    {
      if (i < 4)
      {
        if ((inst->RMS_samplecount % 80) == 0) // every 80 samples we start fresh
        {
          inst->RMS[i] = 0; // start over
        }
        // calculate RMS value
        // currently, it is called each time a sampled-value is updated which might become slow
        int32_t pp = 0;//(float)MmsValue_toInt32(extRef->value);
        getDSPValueFromMMS(dsp, extRef->value,&pp, INT32);
        peakval[i] = pp;//MmsValue_toInt32(extRef->value);
        float ff = (float)peakval[i];
        inst->RMS[i] += (ff * ff);

        if (i == 3)
        {
          if (peakval[i] == 0)
          {
            peakval[i] = peakval[0] + peakval[1] + peakval[2];
            inst->RMS[i] = (float)(peakval[i] * peakval[i]);
          }
        }

        if ((inst->RMS_samplecount % 80) == 79) // we calculate the average after 80 samples
        {
          inst->RMS[i] /= 80;
          inst->RMS[i] = (float)sqrt(inst->RMS[i]);

          updateDataValues_Amp(dsp, i, (double)inst->RMS[i]);

          if (i == 3)
          {
            a = (inst->RMS[0] + inst->RMS[1] + inst->RMS[2]) / 3;
            updateDataValues_Average(dsp,a);
            break;
          }
        }
      }
      i++;
    }
    extRef = extRef->sibling;
  }
  inst->RMS_samplecount++;
}