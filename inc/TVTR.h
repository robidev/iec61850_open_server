#ifndef TVTR_H_
#define TVTR_H_

#include "iec61850_model_extensions.h"
#include "inputs_api.h"


#ifdef __cplusplus
extern "C" {
#endif

void *TVTR_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues );

#ifdef __cplusplus
}
#endif


#endif /* TVTR_H_ */