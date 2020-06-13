#ifndef CSWI_H_
#define CSWI_H_

#include "iec61850_model_extensions.h"
#include "inputs_api.h"


#ifdef __cplusplus
extern "C" {
#endif

void CSWI_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues);

#ifdef __cplusplus
}
#endif


#endif /* CSWI_H_ */