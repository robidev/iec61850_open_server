#ifndef RADR_H_
#define RADR_H_

#include "iec61850_model_extensions.h"
#include "inputs_api.h"


#ifdef __cplusplus
extern "C" {
#endif

//record 4 seconds
#define RADR_MAX_SAMPLES (80*50*4)

typedef struct sRADR {
  IedServer server;
  Input *input;
  int32_t *buffer;
  int bufferIndex;
  int semaphore;
} RADR;

void * RADR_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues);

#ifdef __cplusplus
}
#endif


#endif /* RADR_H_ */