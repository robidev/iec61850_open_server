#ifndef XSWI_H_
#define XSWI_H_

#include "inputs_api.h"
#include <libiec61850/iec61850_server.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct sXSWI
{
  IedServer server;
  DataAttribute* Pos_stVal;
  DataAttribute* Pos_t;
  void * Pos_stVal_callback;
  bool conducting;
} XSWI;

void *XSWI_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues);

#ifdef __cplusplus
}
#endif


#endif /* XSWI_H_ */