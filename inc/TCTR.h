#ifndef TCTR_H_
#define TCTR_H_

#include "inputs_api.h"
#include <libiec61850/iec61850_server.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct sTCTR
{
  void *da;
  IedServer server;
  void * da_callback;
} TCTR;

void *TCTR_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues );

#ifdef __cplusplus
}
#endif


#endif /* TCTR_H_ */