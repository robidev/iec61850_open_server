#ifndef DSP_H_
#define DSP_H_

#include "iec61850_model_extensions.h"
#include "mms_utilities.h"

#ifdef __cplusplus
extern "C"
{
#endif

typedef struct sValueUpdateEntry {
    void *dataAttribute;           // pointer to the IedServer data attribute
    void * callback;    // associated callback function
    struct sValueUpdateEntry *next;
} ValueUpdateEntry;

typedef struct sValueUpdateEntryArray {
    void *dataAttributeArray[4];           // pointer to the IedServer data attribute
    void * callbackArray[4];    // associated callback function
    struct sValueUpdateEntryArray *next;
} ValueUpdateEntryArray;

typedef struct sCallBackEntry {
    void* callback;    // associated callback function
    void * callbackArg;
    struct sCallBackEntry *next;
} CallBackEntry;

typedef enum {
    CURRENT,
    VOLTAGE
} dspType;

typedef struct sDSP
{
    IedServer server;
    InputEntry *extRefs;
    bool DORef;

    ValueUpdateEntryArray *da_phs_list;  // linked list of value references
    ValueUpdateEntryArray *da_phsAng_list;  // linked list of value references
    ValueUpdateEntry *da_Average_list;  // linked list of value references
    CallBackEntry *cb_list;

    double phs[4];
    double phsAng[4];
    double Average;

    dspType type;
    void * dsp_data;
    uint32_t callbackRefCounter; //count the times this DSP callback instance is referenced

    struct sDSP *sibling;
} DSP;


typedef void* (*DSP_InitFunc)(void);
typedef void (*DSP_ProcessFunc)(void *);
//register these default functions
extern void *init_dft();
extern void *init_rms();
extern void CALC_DFT(void * dsp);
extern void CALC_RMS(void * dsp);

// FUNCTIONS CALLABLE BY PLUGINS TO OVERWRITE DSP PROCESSING
//overwrite the used callback
void set_I_DSP_processing_callback(void * DSP_processing_callback);
void set_U_DSP_processing_callback(void * DSP_processing_callback);
void set_I_DSP_init(void * DSP_init);
void set_U_DSP_init(void * DSP_init);

// FUNCTIONS FOR DURING LN INIT
//init a dsp
void * init_dsp_I(IedServer server, InputEntry *extRefs);//
void * init_dsp_U(IedServer server, InputEntry *extRefs);//
//request callback-function, works only once per DSP to prevent multiple times processing the same values
callBackFunction get_DSP_processing_callback(DSP * dsp);
// add items that should have their value updated after the DSP function is done
void DSP_add_value_update_Average(DSP *dsp, void * dataAttribute, void * callback);
void DSP_add_value_update_Phs(DSP *dsp, void ** dataAttributeArray, void ** callbackArray);
void DSP_add_value_update_PhsAng(DSP *dsp, void ** dataAttributeArray);//no callback
// add callback, to be called when calculation returns
void DSP_add_callback_on_update(DSP * dsp, void * callBack, void * arg);


// FUNCTION CALLED TO PROCESS DATA 
//the actual callback-functions
void DSP_processing_callback(InputEntry *extRef);

// FUNCTIONS FOR THE DSP TO CALL DURING PROCESSING
// update values and registered callbacks (called from DSP function)
void getDSPValueFromMMS(DSP * dsp, void * mmsval, void * ref, ctype reftype); //to decode unique SMV-LE type DO structure and DA types based on extref type
void updateDataValues_Average(DSP * dsp, double amplitude);
void updateDataValues_Amp(DSP * dsp, uint32_t i, double amplitude);
void updateDataValues_Angle(DSP * dsp, uint32_t i, double angle);

// FUNTIONS FOR AFTER PROCESSING
// get current values
double DSP_get_phs(DSP *dsp, uint32_t index);
double DSP_get_phsAng(DSP *dsp, uint32_t index);
double DSP_get_Average(DSP *dsp);


#ifdef __cplusplus
}
#endif

#endif /* DSP_H_ */
