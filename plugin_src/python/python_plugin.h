
#ifndef PYTHON_PLUGIN_H_
#define PYTHON_PLUGIN_H_

#include <libiec61850/iec61850_model.h>
#include "open_server.h"

#ifdef __cplusplus
extern "C"
{
#endif


MmsValue * getDataRefFromModel(OpenServerInstance *srv, char *ref);
void updateDataRef(OpenServerInstance *srv, char *ref, int value);
OpenServerInstance *castOpenServerInstance(void * srv);

#ifdef __cplusplus
}
#endif

#endif /* PYTHON_PLUGIN_H_ */
