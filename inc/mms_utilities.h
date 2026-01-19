#ifndef MMS_UTILITIES_H_
#define MMS_UTILITIES_H_

#ifdef __cplusplus
extern "C"
{
#endif


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


void getValueFromMMS(void * mmsval, void * ref, ctype reftype);

#ifdef __cplusplus
}
#endif

#endif /* LNS_H_ */