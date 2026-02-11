#ifndef MMS_UTILITIES_H_
#define MMS_UTILITIES_H_

#include <stdint.h>
#include <stdbool.h>
#include <libiec61850/iec61850_server.h>

#ifdef __cplusplus
extern "C"
{
#endif

// Enum for c-types to convert IEC values to
typedef enum {
  INT32,
  UINT32,
  FLOAT,
  DOUBLE,
  INT64,
  BOOL,
  UINT8,
  SMV92_LE_Val_AS_INT32,
  SMV92_LE_Q_AS_UINT,
  SMV92_LE_TIME_AS_UINT
} ctype;

// Enum to specify the expected data type
typedef enum {
    IEC_TYPE_BOOL,
    IEC_TYPE_INT32,
    IEC_TYPE_INT64,
    IEC_TYPE_UINT32,
    IEC_TYPE_FLOAT,
    IEC_TYPE_DOUBLE,
    IEC_TYPE_STRING
} IecDataType;

// Structure to hold reference and retrieved value
typedef struct {
    const char* reference;      // e.g., "StrVal.setMag.f"
    IecDataType type;
    union {
        bool boolVal;
        int32_t int32Val;
        int64_t int64Val;
        uint32_t uint32Val;
        float floatVal;
        double doubleVal;
        const char* stringVal;  // Points to MmsValue internal string
    } value;
    bool success;               // Indicates if retrieval was successful
} IecDataPoint;



void getValueFromMMS(void * mmsval, void * ref, ctype reftype);
int IecServer_getDataPoints(IedServer server, LogicalNode* ln, IecDataPoint* dataPoints, int count);
bool IecServer_setDataPoint(IedServer server, DataAttribute* attr, const void* valuePtr);
bool IecServer_setDataPointFromString(IedServer server, DataAttribute *da, const char *value);

#ifdef __cplusplus
}
#endif

#endif /* LNS_H_ */