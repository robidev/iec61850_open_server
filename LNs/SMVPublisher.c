#include "iec61850_server.h"
#include "SMVPublisher.h"

#include "iec61850_model.h"
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "simulation_config.h"

#include "hal_thread.h"
#include <math.h>


typedef struct sSMVP {
    int svcbEnabled;
    SVPublisher_ASDU asdu;
    SVPublisher svPublisher;
    bool running;

    void * simulationHandler;
    LinkedList dataSetValues;

    IedServer server;
    LinkedList  da_el;
    LinkedList  da_el_callback;
} SMVP;

void SMV_Thread(SMVP* inst);

void sVCBEventHandler (SVControlBlock* svcb, int event, void* parameter)
{
    SMVP* inst = (SMVP*)parameter;
    if (event == IEC61850_SVCB_EVENT_ENABLE)
        inst->svcbEnabled = 1;
    else if (event == IEC61850_SVCB_EVENT_DISABLE)
        inst->svcbEnabled = 0;
}

void* SMVP_init(SVPublisher SMVPublisher, SVControlBlock* svcb, IedServer server, LinkedList allInputValues)
{
    SMVP* inst = (SMVP *) malloc(sizeof(SMVP));
    inst->running = false;

    inst->server = server;
    inst->svPublisher = SMVPublisher;

    if (inst->svPublisher == NULL) {
        printf("ERROR: could not create sampled value publisher");
        return NULL;
    }
    

    //SVControlBlock* svcb = IedModel_getSVControlBlock(model, logicalNode, svcbName);//todo merge with calling func.

    //TODO check if dataSet-arg is at the right pos.
    inst->asdu = SVPublisher_addASDU(inst->svPublisher, svcb->dataSetName, NULL, 1);

    SVPublisher_ASDU_addINT32(inst->asdu);
    SVPublisher_ASDU_addQuality(inst->asdu);
    SVPublisher_ASDU_addINT32(inst->asdu);
    SVPublisher_ASDU_addQuality(inst->asdu);
    SVPublisher_ASDU_addINT32(inst->asdu);
    SVPublisher_ASDU_addQuality(inst->asdu);
    SVPublisher_ASDU_addINT32(inst->asdu);
    SVPublisher_ASDU_addQuality(inst->asdu);

    SVPublisher_ASDU_addINT32(inst->asdu);
    SVPublisher_ASDU_addQuality(inst->asdu);
    SVPublisher_ASDU_addINT32(inst->asdu);
    SVPublisher_ASDU_addQuality(inst->asdu);
    SVPublisher_ASDU_addINT32(inst->asdu);
    SVPublisher_ASDU_addQuality(inst->asdu);
    SVPublisher_ASDU_addINT32(inst->asdu);
    SVPublisher_ASDU_addQuality(inst->asdu);

    SVPublisher_ASDU_setSmpCntWrap(inst->asdu, 4000);
    SVPublisher_ASDU_setRefrTm(inst->asdu, 0);

    SVPublisher_setupComplete(inst->svPublisher);

    IedServer_setSVCBHandler(server, svcb, sVCBEventHandler, inst);  
    inst->svcbEnabled = 1;

    inst->dataSetValues = NULL;
    
    //retrieve dataset for this svcb, and use it to store simulated values
    //if(IEC61850_server_simulation_type() == SIMULATION_TYPE_REMOTE)
    {
        //get domain
        char objectReference[130];
        ModelNode_getObjectReference((ModelNode*) svcb->parent, objectReference);
        char* separator = strchr(objectReference, '/');
        *separator = 0;

        //form dataset name
        char* lnName = svcb->parent->name;
        char* dataSetReference = StringUtils_createString(5, objectReference, "/", lnName, "$", svcb->dataSetName);

        /* prepare data set values */
        inst->dataSetValues = LinkedList_create();
        inst->da_el = LinkedList_create();//NEW
        inst->da_el_callback = LinkedList_create();//NEW

        IedModel* model = IedServer_getDataModel(server);
        DataSet* dataSet = IedModel_lookupDataSet(model, dataSetReference);
        DataSetEntry* dataSetEntry = dataSet->fcdas;
        while (dataSetEntry != NULL) {
            LinkedList_add(inst->dataSetValues, dataSetEntry->value);

            //NEW
            DataAttribute* da =  IedModel_lookupDataAttributeByMmsValue(model, MmsValue_getElement( MmsValue_getElement(dataSetEntry->value,0), 0) );
            LinkedList_add(inst->da_el, da );
            LinkedList_add(inst->da_el_callback, _findAttributeValueEx(da, allInputValues));

            dataSetEntry = dataSetEntry->sibling;
        }
    }

    Thread thread = Thread_create((ThreadExecutionFunction)SMV_Thread, inst, true);
    Thread_start(thread);

    return inst;  
}

void SMVP_destroy(SMVP* inst)
{
    SVPublisher_destroy(inst->svPublisher);
}

void SMV_Thread(SMVP* inst)
{
    inst->running = true;
    int measurements[8];

    if(IEC61850_server_simulation_type() == SIMULATION_TYPE_LOCAL)
    {
        Quality q = QUALITY_VALIDITY_GOOD;

        int vol = (int) (6350.f * sqrt(2));//RMS to peak
        int amp = (int) (10.f * sqrt(2));//RMS to peak
        float phaseAngle = 0.f;

        int sampleCount = 0;

        uint64_t nextCycleStart = Hal_getTimeInMs() + 1000;
        while (inst->running) 
        {
                        /* update measurement values */
            int samplePoint = sampleCount % 80;

            double angleA = (2 * M_PI / 80) * samplePoint;
            double angleB = (2 * M_PI / 80) * samplePoint - ( 2 * M_PI / 3);
            double angleC = (2 * M_PI / 80) * samplePoint - ( 4 * M_PI / 3);

            measurements[0] = (amp * sin(angleA - phaseAngle)) * 1000;
            measurements[1] = (amp * sin(angleB - phaseAngle)) * 1000;
            measurements[2] = (amp * sin(angleC - phaseAngle)) * 1000;
            measurements[3] = measurements[0] + measurements[1] + measurements[2];

            measurements[4] = (vol * sin(angleA)) * 100;
            measurements[5] = (vol * sin(angleB)) * 100;
            measurements[6] = (vol * sin(angleC)) * 100;
            measurements[7] = measurements[4] + measurements[5] + measurements[6];

            //retrieve data from dataset, and update values
            /*LinkedList ds = inst->dataSetValues;
            int ds_index = 0;
            while((ds != NULL)//for each LN with an inputs/extref defined;
            {
                if((ds->data != NULL)
                {
                    MmsValue* datasetValue = ds->data;
                    MmsValue_setInt32( MmsValue_getElement( MmsValue_getElement(datasetValue,0), 0) , measurements[ds_index]);
                    ds_index += 1;
                }
                ds = LinkedList_getNext(ds);
            }*/

            LinkedList da_el = inst->da_el;
            LinkedList da_el_callback = inst->da_el_callback;
            int ds_index = 0;
            while(da_el != NULL)//for each LN with an inputs/extref defined;
            {
                if(da_el->data != NULL)
                {
                    IedServer_updateInt32AttributeValue(inst->server,da_el->data,measurements[ds_index]);
                    InputValueHandleExtensionCallbacks(da_el_callback->data); //update the associated input-extref items for this Data Element
                    ds_index += 1;
                }
                da_el = LinkedList_getNext(da_el);
                da_el_callback = LinkedList_getNext(da_el_callback);
            }
            
            
            if (inst->svcbEnabled) {
                //update all ASDU values
                int asdu_index = 0;
                while(asdu_index < (ds_index*8)){
                    SVPublisher_ASDU_setINT32(inst->asdu, asdu_index, measurements[asdu_index / 8]);
                    SVPublisher_ASDU_setQuality(inst->asdu, asdu_index + 4, q);
                    asdu_index += 8;
                }

                SVPublisher_ASDU_setRefrTm(inst->asdu, Hal_getTimeInMs());

                SVPublisher_ASDU_setSmpCnt(inst->asdu, (uint16_t) sampleCount);

                SVPublisher_publish(inst->svPublisher);
            }

            sampleCount = ((sampleCount + 1) % 4000);

            if ((sampleCount % 400) == 0) {
                uint64_t timeval = Hal_getTimeInMs();

                while (timeval < nextCycleStart + 100) {
                    Thread_sleep(1);

                    timeval = Hal_getTimeInMs();
                }

                nextCycleStart = nextCycleStart + 100;
            }
        }
    }
    else // if(IEC61850_server_simulation_type() == SIMULATION_TYPE_NONE || IEC61850_server_simulation_type() == SIMULATION_TYPE_REMOTE)
    {
        int sampleCount = 0;
        //Quality q = QUALITY_VALIDITY_GOOD;
        uint64_t nextCycleStart = Hal_getTimeInMs() + 1000;

        int step = 0;

        while (inst->running) 
        {
            int samplePoint = sampleCount % 80;
            if (inst->svcbEnabled) {
                
                //retrieve data from dataset
                LinkedList ds = inst->dataSetValues;
                int index = 0;
                while(ds != NULL)//for each LN with an inputs/extref defined;
                {
                    if(ds->data != NULL)
                    {
                        MmsValue* datasetValue = ds->data;
                        //char buf[255];
                        //MmsValue_printToBuffer(datasetValue,buf,255);
                        //printf("data: %s\n",buf);

                        SVPublisher_ASDU_setINT32(inst->asdu, index, MmsValue_toInt32( MmsValue_getElement( MmsValue_getElement(datasetValue,0), 0) ) );
                        SVPublisher_ASDU_setQuality(inst->asdu, index + 4, MmsValue_toUint32( MmsValue_getElement(datasetValue,1) ));
                        index += 8;
                    }
                    ds = LinkedList_getNext(ds);
                }

                SVPublisher_ASDU_setRefrTm(inst->asdu, Hal_getTimeInMs());

                SVPublisher_ASDU_setSmpCnt(inst->asdu, (uint16_t) sampleCount);

                SVPublisher_publish(inst->svPublisher);
            }

            sampleCount = ((sampleCount + 1) % 4000);

            if(IEC61850_server_simulation_type() == SIMULATION_TYPE_REMOTE)
            {
                IEC61850_server_simulation_sync(step++);
            }
            else
            {
                if ((sampleCount % 400) == 0) {
                    uint64_t timeval = Hal_getTimeInMs();

                    while (timeval < nextCycleStart + 100) {
                        Thread_sleep(1);

                        timeval = Hal_getTimeInMs();
                    }

                    nextCycleStart = nextCycleStart + 100;
                }
            }
        }
    }
}