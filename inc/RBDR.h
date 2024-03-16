#ifndef RBDR_H_
#define RBDR_H_

#include "iec61850_model_extensions.h"
#include "inputs_api.h"


#ifdef __cplusplus
extern "C" {
#endif


typedef struct sRBDR {
  IedServer server;
  Input *input;
  uint32_t value;
  int semaphore;
} RBDR;

void * RBDR_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues);

#ifdef __cplusplus
}
#endif


#endif /* RBDR_H_ */