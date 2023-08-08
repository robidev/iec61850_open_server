#ifndef OPEN_SERVER_H_
#define OPEN_SERVER_H_

#include <libiec61850/iec61850_server.h>
#include "iec61850_model_extensions.h"
#include "LNParse.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct sOpenServerInstance {
    IedServer server;                   // server instance 
    IedModel *Model;
    IedModel_extensions *Model_ex;
    SMVcB* SMVControlInstances;         // describes the sampled value control block instances
    LinkedList allInputValues;          // describes all inputvalues in a large linked list(for callbacks)
} OpenServerInstance;

typedef int (*lib_init_func)(OpenServerInstance *srv);


int open_server_running();

#ifdef __cplusplus
}
#endif


#endif /* OPEN_SERVER_H_ */