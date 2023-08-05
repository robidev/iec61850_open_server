#ifndef XCBR_H_
#define XCBR_H_

#include "inputs_api.h"
#include <libiec61850/iec61850_server.h>

#ifdef __cplusplus
extern "C" {
#endif

void *XCBR_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues);

#ifdef __cplusplus
}
#endif


#endif /* XCBR_H_ */