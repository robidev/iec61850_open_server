#include "mms_utilities.h"
#include <stdio.h>
#include <libiec61850/mms_value.h>


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


/**
 * Retrieve multiple data points from an IEC61850 server
 * 
 * @param server    The IEC61850 server instance
 * @param ln        The logical node to retrieve data from
 * @param dataPoints Array of data points to retrieve
 * @param count     Number of data points in the array
 * @return          Number of successfully retrieved values
 */
int IecServer_getDataPoints(IedServer server, LogicalNode* ln, IecDataPoint* dataPoints, int count)
{
    int successCount = 0;
    
    for (int i = 0; i < count; i++) {
        dataPoints[i].success = false;
        
        // Get the data attribute
        DataAttribute* attr = (DataAttribute*)ModelNode_getChild((ModelNode*)ln, dataPoints[i].reference);
        
        if (attr == NULL) {
            continue;  // Reference not found
        }
        
        // Get the value
        MmsValue* mmsValue = IedServer_getAttributeValue(server, attr);
        
        if (mmsValue == NULL) {
            continue;  // Failed to get value
        }
        MmsType mmsType = MmsValue_getType(mmsValue);
        
        // Extract value based on type
        switch (dataPoints[i].type) {
            case IEC_TYPE_BOOL:
                if(mmsType != MMS_BOOLEAN) continue;
                dataPoints[i].value.boolVal = MmsValue_getBoolean(mmsValue);
                dataPoints[i].success = true;
                break;
                
            case IEC_TYPE_INT32:
                if(mmsType != MMS_UNSIGNED && mmsType != MMS_INTEGER) continue;
                dataPoints[i].value.int32Val = MmsValue_toInt32(mmsValue);
                dataPoints[i].success = true;
                break;
                
            case IEC_TYPE_INT64:
                if(mmsType != MMS_UNSIGNED && mmsType != MMS_INTEGER) continue;
                dataPoints[i].value.int64Val = MmsValue_toInt64(mmsValue);
                dataPoints[i].success = true;
                break;
                
            case IEC_TYPE_UINT32:
                if(mmsType != MMS_UNSIGNED && mmsType != MMS_INTEGER) continue;
                dataPoints[i].value.uint32Val = MmsValue_toUint32(mmsValue);
                dataPoints[i].success = true;
                break;
                
            case IEC_TYPE_FLOAT:
                if(mmsType != MMS_FLOAT) continue;
                dataPoints[i].value.floatVal = MmsValue_toFloat(mmsValue);
                dataPoints[i].success = true;
                break;
                
            case IEC_TYPE_DOUBLE:
                if(mmsType != MMS_FLOAT) continue;
                dataPoints[i].value.doubleVal = MmsValue_toDouble(mmsValue);
                dataPoints[i].success = true;
                break;
                
            case IEC_TYPE_STRING:
                if(mmsType != MMS_STRING && mmsType != MMS_VISIBLE_STRING) continue;
                dataPoints[i].value.stringVal = MmsValue_toString(mmsValue);
                dataPoints[i].success = true;
                break;
                
            default:
                break;
        }
        
        if (dataPoints[i].success) {
            successCount++;
        }
    }
    
    return successCount;
}

/**
 * Set a data point value with automatic type detection
 * 
 * @param server    The IEC61850 server instance
 * @param attr      The data attribute to set
 * @param valuePtr  Pointer to the value to set
 * @return          true if successful, false otherwise
 */
bool IecServer_setDataPoint(IedServer server, DataAttribute* attr, const void* valuePtr)
{
    if (attr == NULL || valuePtr == NULL) {
        return false;
    }
    
    MmsValue* mmsValue = IedServer_getAttributeValue(server, attr);
    
    if (mmsValue == NULL) {
        return false;
    }
    
    // Detect type from MmsValue
    MmsType mmsType = MmsValue_getType(mmsValue);
    
    switch (mmsType) {
        case MMS_BOOLEAN:
            MmsValue_setBoolean(mmsValue, *(const bool*)valuePtr);
            break;
            
        case MMS_INTEGER:
            MmsValue_setInt32(mmsValue, *(const int32_t*)valuePtr);
            break;
            
        case MMS_UNSIGNED:
            MmsValue_setUint32(mmsValue, *(const uint32_t*)valuePtr);
            break;
            
        case MMS_FLOAT:
            MmsValue_setFloat(mmsValue, *(const float*)valuePtr);
            break;
            
        case MMS_STRING:
        case MMS_VISIBLE_STRING:
            MmsValue_setMmsString(mmsValue, *(const char* const*)valuePtr);
            break;
            
        default:
            return false;
    }
    
    IedServer_updateAttributeValue(server, attr, mmsValue);
    
    return true;
}

bool IecServer_setDataPointFromString(IedServer server, DataAttribute *da, const char *value)
{
    if (!server || !da || !value) {
        return false;
    }

    MmsValue* mmsValue = IedServer_getAttributeValue(server, da);
    if (!mmsValue) {
        return false;
    }

    MmsType mmsType = MmsValue_getType(mmsValue);
    bool success = false;

    switch (mmsType) {
        case MMS_BOOLEAN: {
            bool boolValue;
            if (strcasecmp(value, "true") == 0 || strcmp(value, "1") == 0) {
                boolValue = true;
            } else if (strcasecmp(value, "false") == 0 || strcmp(value, "0") == 0) {
                boolValue = false;
            } else {
                return false;
            }
            MmsValue_setBoolean(mmsValue, boolValue);
            success = true;
            break;
        }

        case MMS_INTEGER: {
            char *endptr;
            long intValue = strtol(value, &endptr, 10);
            if (*endptr != '\0') {
                return false;
            }
            MmsValue_setInt32(mmsValue, (int32_t)intValue);
            success = true;
            break;
        }

        case MMS_UNSIGNED: {
            char *endptr;
            unsigned long uintValue = strtoul(value, &endptr, 10);
            if (*endptr != '\0') {
                return false;
            }
            MmsValue_setUint32(mmsValue, (uint32_t)uintValue);
            success = true;
            break;
        }

        case MMS_FLOAT: {
            char *endptr;
            double floatValue = strtod(value, &endptr);
            if (*endptr != '\0') {
                return false;
            }
            MmsValue_setDouble(mmsValue, floatValue);
            success = true;
            break;
        }

        case MMS_VISIBLE_STRING:
        case MMS_STRING: {
            MmsValue_setVisibleString(mmsValue, value);
            success = true;
            break;
        }

        case MMS_BIT_STRING: {
            int bitStringSize = MmsValue_getBitStringSize(mmsValue);
            int valueLen = strlen(value);
            
            if (valueLen != bitStringSize) {
                return false;
            }
            
            for (int i = 0; i < bitStringSize; i++) {
                if (value[i] == '1') {
                    MmsValue_setBitStringBit(mmsValue, i, true);
                } else if (value[i] == '0') {
                    MmsValue_setBitStringBit(mmsValue, i, false);
                } else {
                    return false;
                }
            }
            success = true;
            break;
        }

        default:
            return false;
    }

    if (success) {
        IedServer_updateAttributeValue(server, da, mmsValue);
    }

    return success;
}
