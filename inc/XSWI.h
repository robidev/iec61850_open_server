#ifndef XSWI_H_
#define XSWI_H_

#include "inputs_api.h"
#include <libiec61850/iec61850_server.h>
#include <libiec61850/hal_thread.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef void (*XSWICallback)(void *, bool);

typedef struct sXSWI
{
  IedServer server;
  DataAttribute* Pos_stVal;
  DataAttribute* Pos_t;
  void * Pos_stVal_callback;
  XSWICallback XSWI_callback_ln;
  void * config;
  Semaphore sem;
} XSWI;

void *XSWI_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues);
void XSWI_change_switch(XSWI *inst, Dbpos value);
int setXSWI_Callback(XSWI *instance, XSWICallback callback);

#ifdef __cplusplus
}
#endif


#endif /* XSWI_H_ */