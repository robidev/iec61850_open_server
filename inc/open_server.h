#ifndef OPEN_SERVER_H_
#define OPEN_SERVER_H_

#include <libiec61850/iec61850_server.h>
#include "iec61850_model_extensions.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef int (*lib_init_func)(IedModel* model, IedModel_extensions* model_ex);

int open_server_running();

#ifdef __cplusplus
}
#endif


#endif /* OPEN_SERVER_H_ */