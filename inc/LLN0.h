#ifndef LLN0_H_
#define LLN0_H_

#include "iec61850_model_extensions.h"
#include "inputs_api.h"


#ifdef __cplusplus
extern "C" {
#endif

void LLN0_init(IedServer server, LogicalNode* logicalNode);

#ifdef __cplusplus
}
#endif


#endif /* LLN0_H_ */