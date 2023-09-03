#ifndef RDRE_H_
#define RDRE_H_

#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "LNParse.h"

#ifdef __cplusplus
extern "C" {
#endif

void RDRE_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues);

#ifdef __cplusplus
}
#endif


#endif /* RDRE_H_ */