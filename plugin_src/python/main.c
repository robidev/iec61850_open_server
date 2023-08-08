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

void updateDataRef(OpenServerInstance *srv, char *ref, int value)
{
    if(srv == NULL || srv->Model == NULL || srv->server == NULL || srv->allInputValues == NULL|| ref == NULL)
        return;

    DataAttribute* Pos_stVal = (DataAttribute *)IedModel_getModelNodeByObjectReference(srv->Model,ref);
    if(Pos_stVal == NULL)
        return;
    IedServer_updateInt32AttributeValue(srv->server, Pos_stVal, value);
    AttributeValueHandleExtensionCallbacks(Pos_stVal, srv->allInputValues); // update the associated callbacks with this Data Element
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