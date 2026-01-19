#include "mms_utilities.h"
#include <libiec61850/mms_value.h>
#include <stdio.h>

void getValueFromMMS(void * mmsval, void * ref, ctype reftype)
{
  MmsType mmstype = MmsValue_getType(mmsval);
  switch(mmstype)
  {
    case MMS_INTEGER:
      switch(reftype)
      {
        case INT32:  *(int32_t *)ref = MmsValue_toInt32(mmsval); break;
        case UINT32: *(uint32_t *)ref = (uint32_t)MmsValue_toInt32(mmsval); break;
        case FLOAT:  *(float *)ref = (float)MmsValue_toInt32(mmsval); break;
        case DOUBLE: *(double *)ref = (double)MmsValue_toInt32(mmsval); break;
        case INT64:  *(int64_t *)ref = MmsValue_toInt64(mmsval); break;
        default:
          printf("ERROR: could not convert mmstype (%d) to reftype (%d)\n",mmstype, reftype);
      }
    break;
    case MMS_UNSIGNED:
      switch(reftype)
      {
        case INT32:  *(int32_t *)ref = (int32_t)MmsValue_toUint32(mmsval); break;
        case UINT32: *(uint32_t *)ref = MmsValue_toUint32(mmsval); break;
        case FLOAT:  *(float *)ref = (float)MmsValue_toUint32(mmsval); break;
        case DOUBLE: *(double *)ref = (double)MmsValue_toUint32(mmsval); break;
        case INT64:  *(int64_t *)ref = (int64_t)MmsValue_toUint32(mmsval); break;
        default:
          printf("ERROR: could not convert mmstype (%d) to reftype (%d)\n",mmstype, reftype);
      }
    break;
    case MMS_FLOAT:
      switch(reftype)
      {
        case INT32:  *(int32_t *)ref = (int32_t)MmsValue_toFloat(mmsval); break;
        case UINT32: *(uint32_t *)ref = (uint32_t)MmsValue_toFloat(mmsval); break;
        case FLOAT:  *(float *)ref = MmsValue_toFloat(mmsval); break;
        case DOUBLE: *(double *)ref = MmsValue_toDouble(mmsval); break;
        case INT64:  *(int64_t *)ref = (int64_t)MmsValue_toFloat(mmsval); break;
        default:
          printf("ERROR: could not convert mmstype (%d) to reftype (%d)\n",mmstype, reftype);
      }
    break;
    case MMS_BOOLEAN:
      switch(reftype)
      {
        case INT32:  *(int32_t *)ref = (int32_t)MmsValue_getBoolean(mmsval); break;
        case UINT32: *(uint32_t *)ref = (uint32_t)MmsValue_getBoolean(mmsval); break;
        case INT64:  *(int64_t *)ref = (int64_t)MmsValue_getBoolean(mmsval); break;
        case BOOL:  *(bool *)ref = (bool)MmsValue_getBoolean(mmsval); break;
        case UINT8:  *(uint8_t *)ref = (uint8_t)MmsValue_getBoolean(mmsval); break;
        default:
          printf("ERROR: could not convert mmstype (%d) to reftype (%d)\n",mmstype, reftype);
      }
    break;
    case MMS_STRUCTURE:
      switch(reftype)
      {
        case SMV92_LE_Val_AS_INT32:  *(int32_t *)ref = (int32_t)MmsValue_toInt32(MmsValue_getElement(mmsval, 0)); break;
        case SMV92_LE_Q_AS_UINT:     *(uint32_t *)ref = (uint32_t)MmsValue_toUint32(MmsValue_getElement(mmsval, 1)); break;
        case SMV92_LE_TIME_AS_UINT:  *(int64_t *)ref = (int64_t)MmsValue_getUtcTimeInMs(MmsValue_getElement(mmsval, 2)); break;
        default:
          printf("ERROR: could not convert STRUCTURE mmstype (%d) to reftype (%d)\n",mmstype, reftype);
      }
    break;
    case MMS_OCTET_STRING:
    case MMS_VISIBLE_STRING:
    case MMS_STRING:
      //MmsValue_toString(MmsValue* self);//MmsValue_getStringSize; visible string or mms string
      printf("ERROR: could not convert STRING mmstype (%d) to reftype (%d); UNSUPPORTED MMS TYPE\n",mmstype, reftype);
    break;
    case MMS_GENERALIZED_TIME:
    case MMS_BINARY_TIME:
    case MMS_UTC_TIME:  //MmsValue_toUnixTimestamp
      printf("ERROR: could not convert TIME mmstype (%d) to reftype (%d); UNSUPPORTED MMS TYPE\n",mmstype, reftype);
    break;
    case MMS_BIT_STRING:
      //MmsValue_getBitStringBit//MmsValue_getBitStringSize, MmsValue_getBitStringByteSize, MmsValue_getBitStringAsInteger
      printf("ERROR: could not convert BIT-STRING mmstype (%d) to reftype (%d); UNSUPPORTED MMS TYPE\n",mmstype, reftype);
    break;
    case MMS_ARRAY:
    case MMS_BCD:
    case MMS_OBJ_ID:
    case MMS_DATA_ACCESS_ERROR:
    default:
      printf("ERROR: could not convert mmstype (%d) to reftype (%d); UNSUPPORTED MMS TYPE\n",mmstype, reftype);
  }
  //printf("REQ: convert mmstype (%d) to reftype (%d), val: %i %f %f\n",mmstype, reftype, *(int32_t *)ref, *(float *)ref, *(double *)ref);
}



