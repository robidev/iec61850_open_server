#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "dsp.h"
#include "mms_utilities.h"
#include <math.h>

extern const double INTERESTED_FREQ;
extern const double SAMPLE_FREQ;
extern const uint32_t WINDOW_SIZE;
const double const_dft_Rms = 0.7071;

typedef enum  {
    EVERY_WINDOW_SIZE,
    EVER_SAMPLE
} DFT_variant;

typedef struct sDFT
{
    DFT_variant variant;
    double **xn;
    double Xr[4];
    double Xi[4];
    int sample_index;  
} DFT;

void * init_dft()
{
    int i = 0;
    DFT *inst = (DFT *)malloc(sizeof(DFT)); // create new instance with MALLOC
    if(inst == NULL) return NULL;
    
    inst->variant = EVERY_WINDOW_SIZE;

    inst->xn = malloc(4*sizeof(double *));
    inst->sample_index=0;
    for(i=0; i<4; i++)
    { 
        inst->Xr[i] = 0;
        inst->Xi[i] = 0;
        inst->xn[i] = malloc(WINDOW_SIZE*sizeof(double));
        memset(inst->xn[i], 0, WINDOW_SIZE*sizeof(double));
    }
    return inst;
}


void CALC_DFT(void * dsp)
{
  DSP *dsp_inst = dsp;
  DFT * inst = dsp_inst->dsp_data;

  InputEntry *extRef = dsp_inst->extRefs; // start from the first extref, and check all values, we assume there are 8!
  int i = 0;
  double Ni=0, Nr=0;
  double AvgAmp=0;

  while (extRef != NULL)
  {
    if (extRef->value != NULL)
    {
      if (i < 4)// only 4 items
      {
        double k=INTERESTED_FREQ / (SAMPLE_FREQ / WINDOW_SIZE);

        if(inst->variant == EVERY_WINDOW_SIZE)//calculate dft every WINDOW_SIZE (e.g. 80) cycles. this means low latency, but the values are updated only once per cycle
        {
          double multiplier = 0.5 * (1 - cos( 2 * M_PI * inst->sample_index / WINDOW_SIZE));//Hanning window

          double vv = 0;
          getDSPValueFromMMS(dsp, extRef->value,&vv, DOUBLE);
          inst->Xr[i] = (inst->Xr[i] +  vv * multiplier * cos(2 * M_PI * k * (double)inst->sample_index / WINDOW_SIZE));
          inst->Xi[i] = (inst->Xi[i] -  vv * multiplier * sin(2 * M_PI * k * (double)inst->sample_index / WINDOW_SIZE));

          //k * (SAMPLE_FREQ / WINDOW_SIZE), Xr/WINDOW_SIZE, Xi/WINDOW_SIZE, amplitude/(WINDOW_SIZE)*4, angle);
          if ((inst->sample_index % WINDOW_SIZE) == WINDOW_SIZE-1) // we calculate the dft vector after WINDOW_SIZE samples
          {
            //printf("dft: %s= %d\n",extRef->Ref, MmsValue_toInt32(extRef->value));
            if(i < 3)
            {
              //calculate neutral by adding other vectors
              inst->Xi[3] += inst->Xi[i];
              inst->Xr[3] += inst->Xr[i];
            }
            double amplitude = sqrt((inst->Xr[i]*inst->Xr[i]) + (inst->Xi[i]*inst->Xi[i]))/(WINDOW_SIZE)*4;
            updateDataValues_Amp(dsp, i, amplitude * const_dft_Rms);//inst->da_A_phs[ i % 4 ]


            double quadrant = 0;
            if(inst->Xr[i] < 0.0 ) quadrant = 180;
            if(inst->Xr[i] > 0.0 && inst->Xi[i] < 0.0) quadrant = 360;
            double angle = (atan(inst->Xi[i]/inst->Xr[i]) * (180/M_PI)) + quadrant;
            updateDataValues_Angle(dsp, i, angle);//inst->da_A_phsAng[ i % 4 ]

            AvgAmp += amplitude;
            if (i == 3)
            {
              updateDataValues_Average(dsp, AvgAmp/3 * const_dft_Rms);//inst->da_A
            }
            inst->Xr[i] = 0;
            inst->Xi[i] = 0;
          }
        }
        else//calculate whole window every cycle
        {
          double Xr =0, Xi = 0;
            int n;
            double vv = 0;
            getValueFromMMS(extRef->value,&vv, DOUBLE);
            inst->xn[i][inst->sample_index] = vv;//MmsValue_toInt32(extRef->value);
        
            for (n = 0; n < WINDOW_SIZE; n++) { //calculate 1 cycle(WINDOW_SIZE samples)
            double multiplier = 0.5 * (1 - cos( 2 * M_PI *n / WINDOW_SIZE));//Hanning window
            Xr = (Xr + inst->xn[i][(n + inst->sample_index) % WINDOW_SIZE] * multiplier * cos(2 * M_PI * k * (double)n / WINDOW_SIZE));
            Xi = (Xi - inst->xn[i][(n + inst->sample_index) % WINDOW_SIZE] * multiplier * sin(2 * M_PI * k * (double)n / WINDOW_SIZE));
            }
            double amplitude = sqrt((Xr*Xr) + (Xi*Xi))/(WINDOW_SIZE)*4;
            /*if(Xr < 0.0 ) quadrant = 180;
            if(Xr > 0.0 && Xi < 0.0) quadrant = 360;
            double angle = (atan(Xi/Xr) * (180/M_PI)) + quadrant;*/
            updateDataValues_Amp(dsp, i, amplitude * const_dft_Rms);//inst->da_A_phs[ i % 4 ]

            double quadrant = 0;
            if(Xr < 0.0 ) quadrant = 180;
            if(Xr > 0.0 && Xi < 0.0) quadrant = 360;
            double angle = (atan(Xi / Xr) * (180/M_PI)) + quadrant;
            updateDataValues_Angle(dsp, i, angle);//inst->da_A_phsAng[ i % 4 ]

            //calculate neutral
            Ni += Xi;
            Nr += Xr;
            if (i == 3)
            {
                float a = sqrt((Nr*Nr) + (Ni*Ni))/(WINDOW_SIZE * 3)*4;
                updateDataValues_Average(dsp, a * const_dft_Rms);//inst->da_A
            }
        }
      }
      i++;
    }
    extRef = extRef->sibling;
  }
  inst->sample_index = (inst->sample_index + 1) % WINDOW_SIZE;
}