#ifndef TCTR_H_
#define TCTR_H_

#include "iec61850_model_extensions.h"
#include "inputs_api.h"


#ifdef __cplusplus
extern "C" {
#endif

void *TCTR_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues );

#ifdef __cplusplus
}
#endif


#endif /* TCTR_H_ */