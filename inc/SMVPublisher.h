#ifndef SMVPUBLISHER_H_
#define SMVPUBLISHER_H_

#include <libiec61850/sv_publisher.h>
#include <libiec61850/iec61850_server.h>


#ifdef __cplusplus
extern "C" {
#endif

typedef void (*SampleCallback)(int,void *);

typedef struct sSMVP {
    int svcbEnabled;
    SVPublisher_ASDU asdu;
    SVPublisher svPublisher;
    bool running;

    LinkedList dataSetValues;

    IedServer server;
    //LinkedList  da_el;
    //LinkedList  da_el_callback;
    SampleCallback getSample;
    void * getSampleParameter;
} SMVP;

void* SMVP_init(SVPublisher SMVPublisher, SVControlBlock* svcb, IedServer server, LinkedList allInputValues);
int setSampleCallback(SMVP *instance, SampleCallback callback, void *parameter);

#ifdef __cplusplus
}
#endif


#endif /* SMVPUBLISHER_H_ */
