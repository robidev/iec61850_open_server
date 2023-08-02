#ifndef LN_EXTENSIONS_H_
#define LN_EXTENSIONS_H_

#include <libiec61850/iec61850_model.h>
#include "iec61850_model_extensions.h"

#ifdef __cplusplus
extern "C" {
#endif

void attachLogicalNodes(IedModel_extensions* model);


#ifdef __cplusplus
}
#endif


#endif /* LN_EXTENSIONS_H_ */