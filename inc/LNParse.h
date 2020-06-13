#ifndef LNS_H_
#define LNS_H_

#include "iec61850_model_extensions.h"
#include "sv_publisher.h"

#ifdef __cplusplus
extern "C" {
#endif

void attachLogicalNodes(IedServer server, IedModel_extensions* model, LinkedList allInputValues);

void attachSMV(IedServer server, IedModel* model, char* ethernetIfcID, LinkedList allInputValues);

LogicalNodeClass* getLNClass(IedModel* model, IedModel_extensions* model_ex, const char * objectReference);

#ifdef __cplusplus
}
#endif


#endif /* LNS_H_ */

