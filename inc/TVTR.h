#ifndef TVTR_H_
#define TVTR_H_

#include "inputs_api.h"
#include <libiec61850/iec61850_server.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct sTVTR
{
  void *da;
  IedServer server;
  void * da_callback;
} TVTR;

void *TVTR_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues );

#ifdef __cplusplus
}
#endif


#endif /* TVTR_H_ */