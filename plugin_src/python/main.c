#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <libiec61850/iec61850_server.h>
#include <libiec61850/iec61850_model.h>
#include <libiec61850/hal_thread.h>

#include "open_server.h"
#include "iec61850_dynamic_model_extensions.h"
#include "iec61850_config_file_parser_extensions.h"
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "timestep_config.h"
#include "LNParse.h"
#include "python_plugin.h"


extern InputValue *create_InputValue(int index, DataAttribute *da, Input *input, InputEntry *extRef);

OpenServerInstance *castOpenServerInstance(void * srv)
{
    return (OpenServerInstance * )srv;
}


void Python_threat(void * srv);

MmsValue * getDataRefFromModel(OpenServerInstance *srv, char *ref)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || ref == NULL)
        return NULL;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return NULL;
    return IedServer_getAttributeValue(srv->server, Pos_stVal);
}


void updateDataRef(OpenServerInstance *srv, char *ref, MmsValue* value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateAttributeValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefFloat(OpenServerInstance *srv, char *ref, float value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateFloatAttributeValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefInt32(OpenServerInstance *srv, char *ref, int value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateInt32AttributeValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefDbpos(OpenServerInstance *srv, char *ref, uint8_t value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateDbposValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefInt64(OpenServerInstance *srv, char *ref, int64_t value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateInt64AttributeValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefUnsignedInt32(OpenServerInstance *srv, char *ref, uint32_t value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateUnsignedAttributeValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefBitString(OpenServerInstance *srv, char *ref, uint32_t value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateBitStringAttributeValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefBool(OpenServerInstance *srv, char *ref, bool value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateBooleanAttributeValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefVisString(OpenServerInstance *srv, char *ref, char* value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateVisibleStringAttributeValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefUTCTime(OpenServerInstance *srv, char *ref, uint32_t value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateUTCTimeAttributeValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefTimestamp(OpenServerInstance *srv, char *ref, uint8_t *value)//uint8_t timestamp[8]
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateTimestampAttributeValue(srv->server, Pos_stVal, (Timestamp *)value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void updateDataRefQuality(OpenServerInstance *srv, char *ref, uint16_t value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateQuality(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
}

void registerDaCallback(OpenServerInstance *srv, const char* ref, callBackFunction handler, void* handlerParameter)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| 
      ref == NULL || srv->Model_ex == NULL )
    {
        printf("ERROR: could not register callback\n");
        return;
    }
        
    //find data reference in datamodel
    DataAttribute* da = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(da == NULL)
    {
        printf("ERROR: could not register callback. No DA\n");
        return;
    }
    if(srv->Model_ex->inputs == NULL)
    {
        printf("ERROR: could not register callback. inputs list missing. did you load an .ext model with inputs?\n");
        return;            
    }
    //create a new callback entry at the end of the list
    InputEntry * entry = InputEntry_create(srv->Model_ex->inputs,"pycallback", ref, "intPyRef", "python", "srcPy");
    entry->value = da->mmsValue;
    entry->callBack = handler;
    entry->callBackParam = handlerParameter;
        
    //check if a callback for inputvalues is already registered for this DA
    InputValue * callback_list =  _findAttributeValueEx(da, srv->allInputValues);
    if(callback_list != NULL)
    {
        // we have a callback list for this DA, so add the callback and parameter to the data reference,
        // so it gets called when the DA value is updated
        InputValue *inputValue_local = NULL;
        inputValue_local = callback_list;
        while (inputValue_local->sibling != NULL) // find the last entry in the list
        {
            inputValue_local = inputValue_local->sibling;
        }
        inputValue_local->sibling = create_InputValue(0,da,srv->Model_ex->inputs,entry);
        if(inputValue_local->sibling == NULL)
        {
            printf("ERROR: could not register callback. could not allocate memory\n");
            return;
        }
    }
    else // no callback list defined, so create one
    {
        callback_list = create_InputValue(0,da,srv->Model_ex->inputs,entry);
        if(callback_list == NULL)
        {
            printf("ERROR: could not register callback. could not allocate memory\n");
            return;
        }
        LinkedList_add(srv->allInputValues, callback_list);
    }
}

int init(OpenServerInstance *srv)
{
    Thread thread = Thread_create((ThreadExecutionFunction)Python_threat, srv, true);
    if(thread == NULL)
    {
        printf(" ERROR: could not create thread\n");
        return 1;
    }
    Thread_start(thread);
    printf(" Python thread started\n");
    return 0;
}

PyObject* structToPyObject(void *srv)
{
    PyObject* ctypes_mod = PyImport_ImportModule("ctypes");
    PyObject* c_void_p = PyObject_GetAttrString(ctypes_mod, "c_void_p");
    return PyObject_CallFunction(c_void_p, "O", PyLong_FromVoidPtr(srv));
}

void Python_threat(void * srv)
{
    PyObject *pName, *pModule, *pFunc;
    PyObject *pValue, *pArgs;
    int i;

    Py_Initialize();

    PyObject *sys_path = PySys_GetObject("path");
    PyList_Append(sys_path, PyUnicode_FromString("./plugin/python_app/"));

    pName = PyUnicode_DecodeFSDefault("app");
    /* Error checking of pName left out */

    pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != NULL) {
        pFunc = PyObject_GetAttrString(pModule, "main");
        /* pFunc is a new reference */

        if (pFunc && PyCallable_Check(pFunc)) {

            pArgs = PyTuple_New(1); //1 new tuple

            pValue = structToPyObject(srv);
            if (!pValue) {
                    Py_DECREF(pArgs); Py_DECREF(pModule);
                    printf(" ERROR: Cannot convert argument\n");
                    return;
            }
            PyTuple_SetItem(pArgs, 0, pValue);
      
            ////
            pValue = PyObject_CallObject(pFunc, pArgs);
            ////

            Py_DECREF(pArgs);
            if (pValue != NULL) {
                //printf(" Result of call: %ld\n", PyLong_AsLong(pValue));
                Py_DECREF(pValue);
            }
            else {
                Py_DECREF(pFunc);
                Py_DECREF(pModule);
                PyErr_Print();
                printf(" ERROR: Call failed\n");
                return;
            }
        }
        else {
            if (PyErr_Occurred())
                PyErr_Print();
            printf(" ERROR: Cannot find function main\n");
        }
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    }
    else {
        PyErr_Print();
        printf(" ERROR: Failed to load app.py\n");
        return;
    }
    printf(" Python thread ended normally\n");
    if (Py_FinalizeEx() < 0) {
        return;
    }
}