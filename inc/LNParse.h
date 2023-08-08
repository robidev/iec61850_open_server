#ifndef LNS_H_
#define LNS_H_

#include "iec61850_model_extensions.h"
#include <libiec61850/sv_publisher.h>

#ifdef __cplusplus
extern "C"
{
#endif

    // struct for sampled value control block instances
    typedef struct sSMVcB SMVcB;
    
    struct sSMVcB {
        SVControlBlock *svCBs;
        void *instance;
        SMVcB *sibling;
    };

    void attachLogicalNodes(IedServer server,IedModel_extensions *model, LinkedList allInputValues);

    SMVcB *attachSMV(IedServer server, IedModel *model, LinkedList allInputValues, char *ethernetIfcID);

    LogicalNodeClass *getLNClass(IedModel *model, IedModel_extensions *model_ex, const char *objectReference);

    SMVcB *getSMVInstance(IedModel *model, SMVcB *SMVControlInstances, const char *objectReference);

#ifdef __cplusplus
}
#endif

#endif /* LNS_H_ */
