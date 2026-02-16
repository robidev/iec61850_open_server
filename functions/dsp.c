#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "dsp.h"
#include "mms_utilities.h"

const double INTERESTED_FREQ = 50;
const double SAMPLE_FREQ = 4000;
const uint32_t WINDOW_SIZE = 80; // amount of samples im the window-size

DSP *dsp_consumer_list_I;
DSP *dsp_consumer_list_U;

// assign default processing functions
DSP_ProcessFunc dsp_current_processor = CALC_DFT;
DSP_ProcessFunc dsp_voltage_processor = CALC_DFT;//CALC_RMS;
DSP_InitFunc dsp_current_init = init_dft;
DSP_InitFunc dsp_voltage_init = init_dft;//init_rms;

// FUNCTIONS CALLABLE BY PLUGINS TO OVERWRITE DSP PROCESSING
//overwrite the used callback
void set_I_DSP_processing_callback(void * DSP_processing_callback)
{
    if(DSP_processing_callback)
        dsp_current_processor = DSP_processing_callback;
}

void set_U_DSP_processing_callback(void * DSP_processing_callback)
{
    if(DSP_processing_callback)
        dsp_voltage_processor = DSP_processing_callback;
}
void set_I_DSP_init(void * DSP_init)
{
    if(DSP_init)
        dsp_current_init = DSP_init;
}

void set_U_DSP_init(void * DSP_init)
{
    if(DSP_init)
        dsp_voltage_init = DSP_init;
}

// FUNCTIONS FOR DURING LN INIT

//init a dsp
void * init_dsp_I(IedServer server, InputEntry *extRefs)//accuracy can be used in the future if differen sys need more/less accuracy
{
    DSP *dsp_consumer_entry = dsp_consumer_list_I;
    while(dsp_consumer_entry)
    {
        if(strcmp(dsp_consumer_entry->extRefs->Ref, extRefs->Ref) == 0)
        {
            return dsp_consumer_entry;//return an instance already processing this extref instead of initialising a new one
        }
        dsp_consumer_entry = dsp_consumer_entry->sibling;
    }

    DSP *inst = (DSP *)malloc(sizeof(DSP)); // create new instance with MALLOC
    if(inst == NULL) return NULL;
    //only add value updates and callbacks
    inst->server = server;
    inst->extRefs = extRefs;

    inst->da_phs_list = NULL;  // linked list of value references
    inst->da_phsAng_list = NULL;  // linked list of value references
    inst->da_Average_list = NULL;  // linked list of value references
    inst->cb_list = NULL;
    inst->callbackRefCounter = 0;

    inst->type = CURRENT;
    inst->sibling = dsp_consumer_list_I;// add new inst to head
    dsp_consumer_list_I = inst;

    if(strcmp(extRefs->serviceType,"SMV") == 0 ) // with sampled values(9-2LE) we have a special case, as the dataset is an MMS_STRUCTURE comprised of DO elements, but the value we need is a DA
    {
        inst->DORef = true;
    }
    else
    {
        inst->DORef = false;
    }

    return inst;
} 

void * init_dsp_U(IedServer server, InputEntry *extRefs)//type is DSP, RMS or a type index for a plugin
{
    DSP *dsp_consumer_entry = dsp_consumer_list_U;
    while(dsp_consumer_entry)
    {
        if(strcmp(dsp_consumer_entry->extRefs->Ref, extRefs->Ref) == 0)
        {
            return dsp_consumer_entry;//return an instance already processing this extref instead of initialising a new one
        }
        dsp_consumer_entry = dsp_consumer_entry->sibling;
    }

    DSP *inst = (DSP *)malloc(sizeof(DSP)); // create new instance with MALLOC
    if(inst == NULL) return NULL;
    //only add value updates and callbacks
    inst->server = server;
    inst->extRefs = extRefs;

    inst->da_phs_list = NULL;  // linked list of value references
    inst->da_phsAng_list = NULL;  // linked list of value references
    inst->da_Average_list = NULL;  // linked list of value references
    inst->cb_list = NULL;
    inst->callbackRefCounter = 0;

    inst->type = VOLTAGE;
    inst->sibling = dsp_consumer_list_U; // add new inst to head
    dsp_consumer_list_U = inst;

    if(strcmp(extRefs->serviceType,"SMV") == 0 ) // with sampled values(9-2LE) we have a special case, as the dataset is an MMS_STRUCTURE comprised of DO elements, but the value we need is a DA
    {
        inst->DORef = true;
    }
    else
    {
        inst->DORef = false;
    }

    return inst;
} 

//request callback-function, works only once per DSP to prevent multiple times processing the same values
callBackFunction get_DSP_processing_callback(DSP * dsp)
{
    if(dsp->callbackRefCounter == 0)
    {
        dsp->callbackRefCounter++;
        return (callBackFunction)DSP_processing_callback;
    }
    else{
        dsp->callbackRefCounter++;
        return NULL;
    }
}

// add items that should have their value updated after the DSP function is done
void DSP_add_value_update_Average(DSP *dsp, void * dataAttribute, void * callback)
{
    ValueUpdateEntry *newEntry = malloc(sizeof(ValueUpdateEntry));
    newEntry->dataAttribute = dataAttribute;
    newEntry->callback = callback;
    newEntry->next = dsp->da_Average_list;
    dsp->da_Average_list = newEntry;
}

void DSP_add_value_update_Phs(DSP *dsp, void ** dataAttributeArray, void ** callbackArray)
{
    ValueUpdateEntryArray *newEntry = malloc(sizeof(ValueUpdateEntryArray));
    int i;
    
    // Copy arrays into the new entry
    for(i = 0; i < 4; i++) {
        newEntry->dataAttributeArray[i] = dataAttributeArray[i];
        newEntry->callbackArray[i] = callbackArray[i];
    }
    
    // Insert at head of linked list
    newEntry->next = dsp->da_phs_list;
    dsp->da_phs_list = newEntry;
}

void DSP_add_value_update_PhsAng(DSP *dsp, void ** dataAttributeArray)//no callback
{
    ValueUpdateEntryArray *newEntry = malloc(sizeof(ValueUpdateEntryArray));
    int i;
    
    // Copy arrays into the new entry
    for(i = 0; i < 4; i++) {
        newEntry->dataAttributeArray[i] = dataAttributeArray[i];
        newEntry->callbackArray[i] = NULL;
    }
    
    // Insert at head of linked list
    newEntry->next = dsp->da_phsAng_list;
    dsp->da_phsAng_list = newEntry;
}

// add callback, to be called when calculation returns
void DSP_add_callback_on_update(DSP * dsp, void * callBack, void * arg)
{
    CallBackEntry *newEntry = malloc(sizeof(CallBackEntry));
    newEntry->callback = callBack;
    newEntry->callbackArg = arg;
    newEntry->next = dsp->cb_list;
    dsp->cb_list = newEntry;
}


// FUNCTION CALLED TO PROCESS DATA 

//the actual callback-functions
void DSP_processing_callback(InputEntry *extRef)
{
    DSP * dsp = extRef->callBackParam;
    //delayed dsp init, so that plugin DSP can be initialised on first value update
    if(dsp->dsp_data == NULL)
    {
        void * data = NULL;
        if(dsp->type == CURRENT)
        {
            data = dsp_current_init();
        }
        else // VOLTAGE
        {
            data = dsp_voltage_init();
        }
        if(data == NULL) return;
        dsp->dsp_data = data;
    }

    //call right dsp processing function, I or U, decided on init, can be modified later later
    if(dsp->type == CURRENT)
    {
        dsp_current_processor(dsp);
    }
    else // VOLTAGE
    {
        dsp_voltage_processor(dsp);
    }
    // call any registered LN callbacks that rely on the processed dsp data
    CallBackEntry *current = dsp->cb_list;
    while (current != NULL) {
        if(current->callback)
            ((void (*)(void *))current->callback)(current->callbackArg);
        current = current->next;
    }  
}

// FUNCTIONS FOR THE DSP TO CALL DURING PROCESSING

void getDSPValueFromMMS(DSP * dsp, void * mmsval, void * ref, ctype reftype)
{
    if(dsp->DORef == true) //special case, we need to decode a structure
    {
        switch(reftype)
        {
            case DOUBLE:
            {
                int32_t tmp = -1;
                getValueFromMMS(mmsval, &tmp, SMV92_LE_Val_AS_INT32);
                *(double *)ref = (double)tmp;
                break;
            }
            case FLOAT:
            {
                int32_t tmp = -1;
                getValueFromMMS(mmsval, &tmp, SMV92_LE_Val_AS_INT32);
                *(float *)ref = (float)tmp;
                break;
            }
            case INT32:
                getValueFromMMS(mmsval, ref, SMV92_LE_Val_AS_INT32);
                break;
            default:
                printf("ERROR: unable to decode DO structure to requested reftype\n");
        }
    }
    else
    {
        getValueFromMMS(mmsval, ref, reftype);
    }
}

// update values and registered callbacks (called from DSP function)
void updateDataValues_Average(DSP * dsp, double amplitude)
{
    dsp->Average = amplitude;
    //printf("DSP: update Average reached: %f\n", amplitude);
    //printf("AVG: %f\n", amplitude);
    ValueUpdateEntry *current = dsp->da_Average_list;
    while (current != NULL) {
        IedServer_updateFloatAttributeValue(dsp->server, current->dataAttribute, (float)amplitude);
        InputValueHandleExtensionCallbacks(current->callback);
        current = current->next;
    }  
}

void updateDataValues_Amp(DSP * dsp, uint32_t i, double amplitude)
{
    if(i > 4) return;
    dsp->phs[i] = amplitude;
    //printf("phs%d: %f\n", i, amplitude);
    ValueUpdateEntryArray *current = dsp->da_phs_list;
    while (current != NULL) {
        IedServer_updateFloatAttributeValue(dsp->server, current->dataAttributeArray[i], (float)amplitude);
        if(current->callbackArray[i] != NULL)
            InputValueHandleExtensionCallbacks(current->callbackArray[i]);
        current = current->next;
    }
}

void updateDataValues_Angle(DSP * dsp, uint32_t i, double angle)
{
    if(i > 4) return;
    //printf("ang%d: %f\n", i, angle);
    dsp->phsAng[i] = angle;
    ValueUpdateEntryArray *current = dsp->da_phsAng_list;
    while (current != NULL) {
        IedServer_updateFloatAttributeValue(dsp->server, current->dataAttributeArray[i], (float)angle);
        if(current->callbackArray[i] != NULL)
            InputValueHandleExtensionCallbacks(current->callbackArray[i]);
        current = current->next;
    }    
}

// FUNTIONS FOR AFTER PROCESSING

// get current values
double DSP_get_phs(DSP *dsp, uint32_t index)
{
    if(dsp == NULL) return -1;
    return dsp->phs[index];
}

double DSP_get_phsAng(DSP *dsp, uint32_t index)
{
    if(dsp == NULL) return -1;
    return dsp->phsAng[index];
}

double DSP_get_Average(DSP *dsp)
{
    if(dsp == NULL) return -1;
    return dsp->Average;
}

void destroy_dsp()
{
  //TODO
}