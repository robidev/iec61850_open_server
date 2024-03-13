
#ifndef PYTHON_PLUGIN_H_
#define PYTHON_PLUGIN_H_

#include <libiec61850/iec61850_model.h>
#include "open_server.h"

#ifdef __cplusplus
extern "C"
{
#endif


MmsValue * getDataRefFromModel(OpenServerInstance *srv, char *ref);

void updateDataRef(OpenServerInstance *srv, char *ref, MmsValue* value);
void updateDataRefFloat(OpenServerInstance *srv, char *ref, float value);
void updateDataRefInt32(OpenServerInstance *srv, char *ref, int value);
void updateDataRefDbpos(OpenServerInstance *srv, char *ref, uint8_t value);
void updateDataRefInt64(OpenServerInstance *srv, char *ref, int64_t value);
void updateDataRefUnsignedInt32(OpenServerInstance *srv, char *ref, uint32_t value);
void updateDataRefBitString(OpenServerInstance *srv, char *ref, uint32_t value);
void updateDataRefBool(OpenServerInstance *srv, char *ref, bool value);
void updateDataRefVisString(OpenServerInstance *srv, char *ref, char* value);
void updateDataRefUTCTime(OpenServerInstance *srv, char *ref, uint32_t value);
void updateDataRefTimestamp(OpenServerInstance *srv, char *ref, uint8_t *value);//uint8_t timestamp[8]
void updateDataRefQuality(OpenServerInstance *srv, char *ref, uint16_t value);

OpenServerInstance *castOpenServerInstance(void * srv);

#ifdef __cplusplus
}
#endif

#endif /* PYTHON_PLUGIN_H_ */
