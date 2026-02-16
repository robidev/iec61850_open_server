#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <libiec61850/hal_thread.h>
// #include "../static_model.h"
#include "PDIS.h"
#include "dsp.h"
#include <time.h>
#include <math.h>

typedef enum {
    DIR_FORWARD,
    DIR_REVERSE,
    DIR_NON_DIR
} dir_mode_t;
//
// PDIS : distance protection; measures current into a line, and out of the line. when it deviates, trip
//
typedef struct sPDIS
{
  IedServer server;
  DataAttribute *Op_general;
  void *Op_general_callback;
  Input *input;
  int tripTimer;
  bool trip;
  DSP *dspI;
  DSP *dspU;

  float X1; 
  float LinAng;

  float PhStr;
  float GndStr;

  float K0Fact;
  float K0FactAng;

  dir_mode_t DirMod;
} PDIS;

typedef struct {
    float re;
    float im;
} complex_t;


complex_t polar_to_complex(float mag, float angle_deg)
{
    float a = angle_deg * (float)M_PI / 180.0f;
    complex_t z;
    z.re = mag * cosf(a);
    z.im = mag * sinf(a);
    return z;
}

complex_t c_div(complex_t a, complex_t b)
{
    float d = b.re*b.re + b.im*b.im;
    complex_t r;
    r.re = (a.re*b.re + a.im*b.im) / d;
    r.im = (a.im*b.re - a.re*b.im) / d;
    return r;
}

float c_mag(complex_t a)
{
    return sqrtf(a.re*a.re + a.im*a.im);
}

int directional_check(complex_t Z, float line_ang_deg)
{
    float Z_ang = atan2f(Z.im, Z.re) * 180.0f / (float)M_PI;
    float diff = Z_ang - line_ang_deg;

    while (diff > 180) diff -= 360;
    while (diff < -180) diff += 360;

    return fabsf(diff) <= 90.0f;  // forward hemisphere
}

int PDIS_Ground_step(PDIS *inst,
    float Va_mag, float Va_ang,
    float Ia_mag, float Ia_ang,
    float I0_mag, float I0_ang)   // residual current
{
    // 1. Ground start (GndStr(ASG))
    if (Ia_mag < inst->GndStr)
        return 0;

    // 2. Build phasors
    complex_t Va = polar_to_complex(Va_mag, Va_ang);
    complex_t Ia = polar_to_complex(Ia_mag, Ia_ang);
    complex_t I0 = polar_to_complex(I0_mag, I0_ang);

    // 3. K0 phasor
    complex_t K0 = polar_to_complex(inst->K0Fact, inst->K0FactAng);

    // 4. Compensated fault current
    complex_t I_comp;
    I_comp.re = Ia.re + 3.0f * (K0.re * I0.re - K0.im * I0.im);
    I_comp.im = Ia.im + 3.0f * (K0.re * I0.im + K0.im * I0.re);

    // 5. Apparent ground impedance
    complex_t Zg = c_div(Va, I_comp);

    // 6. Directional supervision (DirMod(ENG))
    if (inst->DirMod != DIR_NON_DIR)
    {
        int is_fwd = directional_check(Zg, inst->LinAng);

        if ((inst->DirMod == DIR_FORWARD && !is_fwd) ||
            (inst->DirMod == DIR_REVERSE && is_fwd))
            return 0;
    }

    // 7. Mho characteristic
    complex_t Zc;
    Zc.re = (inst->X1 / 2.0f) * cosf(inst->LinAng * (float)M_PI / 180.0f);
    Zc.im = (inst->X1  / 2.0f) * sinf(inst->LinAng * (float)M_PI / 180.0f);

    complex_t diff;
    diff.re = Zg.re - Zc.re;
    diff.im = Zg.im - Zc.im;

    if (c_mag(diff) <= inst->X1  / 2.0f)
        return 1;   // TRIP

    return 0;
}


int PDIS_Phase_step(PDIS *inst, float V_mag, float V_ang, float I_mag, float I_ang)
{
    // 1. Start condition (pickup)
    if (I_mag < inst->PhStr)
        return 0;   // no operation

    // 2. Build phasors
    complex_t V = polar_to_complex(V_mag, V_ang);
    complex_t I = polar_to_complex(I_mag, I_ang);

    // 3. Apparent impedance
    complex_t Z = c_div(V, I);

    // 4. Directional check 
    if (inst->DirMod != DIR_NON_DIR)
    {
        int is_fwd = directional_check(Z, inst->LinAng);

        if ((inst->DirMod == DIR_FORWARD && !is_fwd) ||
            (inst->DirMod == DIR_REVERSE && is_fwd))
            return 0;
    }

    // 5. Mho characteristic check
    // Circle centered at Z_reach/2 on line angle
    complex_t Zc;
    Zc.re = (inst->X1 / 2.0f) * cosf(inst->LinAng * (float)M_PI / 180.0f);
    Zc.im = (inst->X1 / 2.0f) * sinf(inst->LinAng * (float)M_PI / 180.0f);

    complex_t diff;
    diff.re = Z.re - Zc.re;
    diff.im = Z.im - Zc.im;

    if (c_mag(diff) <= inst->X1 / 2.0f)
        return 1;   // TRIP

    return 0;
}



// callback when SMV is received
void PDIS_callback_SMV(void *pdis_inst)
{
  PDIS *inst = pdis_inst;
  uint32_t i = 0;
  float I0_mag = (float)DSP_get_phs(inst->dspI, 3);
  float I0_ang = (float)DSP_get_phsAng(inst->dspI, 3);

  while(i < 3)
  {
    float AmpValue  =  (float)DSP_get_phs(inst->dspI, i); // get absolute current from dsp
    float AmpAngle  =  (float)DSP_get_phsAng(inst->dspI, i); // get current angle from dsp
    float VoltValue =  (float)DSP_get_phs(inst->dspU, i); // get absolute voltage from dsp
    float VoltAngle =  (float)DSP_get_phsAng(inst->dspU, i); // get voltage angle from dsp

    bool trip_phase = PDIS_Phase_step(inst, VoltValue, VoltAngle, AmpValue, AmpAngle);
    bool trip_ground = PDIS_Ground_step(inst, VoltValue, VoltAngle, AmpValue, AmpAngle, I0_mag, I0_ang);   // residual current

    if(trip_phase || trip_ground)
    {
      printf("PDIS: treshold reached\n");
      MmsValue *tripValue = MmsValue_newBoolean(true);

      IedServer_updateAttributeValue(inst->server, inst->Op_general, tripValue);
      InputValueHandleExtensionCallbacks(inst->Op_general_callback); // update the associated callbacks with this Data Element

      MmsValue_delete(tripValue);
      inst->tripTimer = 0;
      inst->trip = true;
      // if so send to internal PTRC
    }
    i++;
  }

  if (inst->tripTimer > 200 && inst->trip == true)
  {
    // printf("PDIS: treshold NOT reached\n");
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

void * PDIS_init(IedServer server, LogicalNode *ln, Input *input, LinkedList allInputValues)
{
  PDIS *inst = (PDIS *)malloc(sizeof(PDIS)); // create new instance with MALLOC
  inst->server = server;
  inst->tripTimer = 0;
  inst->trip = false;
  inst->Op_general = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Op.general"); // the node to operate on
  inst->Op_general_callback = _findAttributeValueEx(inst->Op_general, allInputValues);
  inst->input = input;
  inst->dspI = NULL;
  inst->dspU = NULL;

  // (PctRch   Percent reach)
  inst->X1 = 5.0f;        // X1       float Z1_reach = 5.0f        ohms (Zone 1 reach)
  inst->LinAng = 75.0f;   // LinAng   float line_angle = 75.0f    degrees
  inst->PhStr = 0.5f;     // PhStr    float I_start_ph = 0.5f     pickup current (A)
  inst->GndStr = 0.1f;    // GndStr   float I_start_gnd = 0.1f
  inst->K0Fact = 0.8f;    // K0Fact   float K0_mag = 0.8f         Residual compensation factor K 0
  inst->K0FactAng = 0.0f; // K0FactAng float K0_ang = 0.0f        Residual compensation factor K 0
  inst->DirMod = DIR_FORWARD; // DirMod   dir_mode_t DirMod = DIR_FORWARD;

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      if (strcmp(extRef->intAddr, "PDIS_Amp1") == 0)
      {
        inst->dspI = init_dsp_I(server, extRef);//this is to reference the first extref
        //we only call after voltage is processed(usually last)
      }
      if (strcmp(extRef->intAddr, "PDIS_Amp3") == 0) // find extref for the last SMV phase, using the intaddr, so that all values are updated, we ignore nutral in case we have 3 phase, and neutral is calculated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(inst->dspI);
        extRef->callBackParam = inst->dspI;
      }
      if (strcmp(extRef->intAddr, "PDIS_Vol1") == 0)
      {
        inst->dspU = init_dsp_U(server, extRef);//this is to reference the first extref
        DSP_add_callback_on_update(inst->dspU,PDIS_callback_SMV, inst);//called when DSP has processed data
      }
      if (strcmp(extRef->intAddr, "PDIS_Vol3") == 0) // find extref for the last SMV, using the intaddr, so that all values are updated
      {
        extRef->callBack = (callBackFunction)get_DSP_processing_callback(inst->dspU);
        extRef->callBackParam = inst->dspU;
      }
      extRef = extRef->sibling;
    }
  }
  return inst;
}
