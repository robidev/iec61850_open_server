#ifndef RBDR_H_
#define RBDR_H_

#include "iec61850_model_extensions.h"
#include "inputs_api.h"


#ifdef __cplusplus
extern "C" {
#endif

//4 seconds of recording
#define RBDR_MAX_SAMPLES 80*50*4

typedef struct sRBDR {
  IedServer server;
  Input *input;
  int32_t *buffer;
  int bufferIndex;
  int semaphore;
} RBDR;

void * RBDR_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues);

#ifdef __cplusplus
}
#endif


#endif /* RBDR_H_ */