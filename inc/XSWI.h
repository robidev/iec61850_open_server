#ifndef XSWI_H_
#define XSWI_H_

#include "iec61850_model_extensions.h"
#include "inputs_api.h"


#ifdef __cplusplus
extern "C" {
#endif

void *XSWI_init(IedServer server, LogicalNode* ln, Input* input);

#ifdef __cplusplus
}
#endif


#endif /* XSWI_H_ */