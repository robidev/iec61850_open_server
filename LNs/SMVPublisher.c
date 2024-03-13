#include <libiec61850/hal_thread.h>
#include <libiec61850/iec61850_model.h>
#include "SMVPublisher.h"
#include "inputs_api.h"
#include "timestep_config.h"
#include "iec61850_model_extensions.h"

void SMV_Thread(SMVP *inst);

int setSampleCallback(SMVP *instance, SampleCallback callback, void *parameter)
{
    if (instance == NULL || instance->getSample != NULL)
    {
        printf("ERROR: could not assign callback");
        return 1;
    }
    instance->getSampleParameter = parameter;
    instance->getSample = callback;
    return 0;
}

void sVCBEventHandler(SVControlBlock *svcb, int event, void *parameter)
{
    SMVP *inst = (SMVP *)parameter;
    if (event == IEC61850_SVCB_EVENT_ENABLE)
        inst->svcbEnabled = 1;
    else if (event == IEC61850_SVCB_EVENT_DISABLE)
        inst->svcbEnabled = 0;
}

void *SMVP_init(SVPublisher SMVPublisher, SVControlBlock *svcb, IedServer server, LinkedList allInputValues)
{
    if (SMVPublisher == NULL)
    {
        printf("ERROR: could not create sampled value publisher, are you running as root?\n");
        return NULL;
    }

    SMVP *inst = (SMVP *)malloc(sizeof(SMVP));
    inst->running = false;

    inst->server = server;
    inst->getSample = NULL;

    inst->svPublisher = SMVPublisher;

    // TODO check if dataSet-arg is at the right pos.
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

    // retrieve dataset for this svcb, and use it to store simulated values

    // get domain
    char objectReference[130];
    ModelNode_getObjectReference((ModelNode *)svcb->parent, objectReference);
    char *separator = strchr(objectReference, '/');
    *separator = 0;

    // form dataset name
    char *lnName = svcb->parent->name;
    char *dataSetReference = StringUtils_createString(5, objectReference, "/", lnName, "$", svcb->dataSetName);

    /* prepare data set values */
    inst->dataSetValues = LinkedList_create();

    // read dataset, and register all values for updating
    IedModel *model = IedServer_getDataModel(server);
    DataSet *dataSet = IedModel_lookupDataSet(model, dataSetReference);
    DataSetEntry *dataSetEntry = dataSet->fcdas;
    while (dataSetEntry != NULL)
    {
        MmsValue * childEntry = NULL;
        MmsValue * entry =  dataSetEntry->value;
        if(entry == NULL)
        {
            printf("ERROR: dataset element '%s' is not initialised, dataset entry not used by SMV\n",
                dataSetEntry->variableName);
            dataSetEntry = dataSetEntry->sibling;
            continue;
        }
        childEntry = MmsValue_getElement(entry, 0);
        if(childEntry == NULL)
        {
            printf("ERROR: dataset element '%s' is not a Data Object, but a Data Attribute. this is not supported. Please define a Data Object instead\n",
                dataSetEntry->variableName);

            dataSetEntry = dataSetEntry->sibling;
            continue;
        }
        LinkedList_add(inst->dataSetValues, entry);
    
        DataAttribute *da = IedModel_lookupDataAttributeByMmsValue(model, childEntry);
        //TODO check for correct DA type 
        dataSetEntry = dataSetEntry->sibling;
    }

    Thread thread = Thread_create((ThreadExecutionFunction)SMV_Thread, inst, true);
    Thread_start(thread);
    return inst;
}

void SMVP_destroy(SMVP *inst)
{
    SVPublisher_destroy(inst->svPublisher);
}

void SMV_Thread(SMVP *inst)
{
    inst->running = true;

    int sampleCount = 0;
    uint64_t nextCycleStart = Hal_getTimeInMs() + 1000;

    int step = 0;

    while (inst->running)
    {
        if (inst->getSample != NULL)
            inst->getSample(sampleCount, inst->getSampleParameter); // update samples

        int samplePoint = sampleCount % 80;
        if (inst->svcbEnabled)
        {

            // retrieve data from dataset
            LinkedList ds = inst->dataSetValues;
            int index = 0;
            while (ds != NULL) // for each LN with an inputs/extref defined;
            {
                if (ds->data != NULL)
                {
                    MmsValue *datasetValue = ds->data;

                    SVPublisher_ASDU_setINT32(inst->asdu, index, MmsValue_toInt32(MmsValue_getElement(MmsValue_getElement(datasetValue, 0), 0)));
                    SVPublisher_ASDU_setQuality(inst->asdu, index + 4, MmsValue_toUint32(MmsValue_getElement(datasetValue, 1)));
                    index += 8;
                }
                ds = LinkedList_getNext(ds);
            }

            SVPublisher_ASDU_setRefrTm(inst->asdu, Hal_getTimeInMs());

            SVPublisher_ASDU_setSmpCnt(inst->asdu, (uint16_t)sampleCount);

            SVPublisher_publish(inst->svPublisher);
        }

        sampleCount = ((sampleCount + 1) % 4000);

        if (IEC61850_server_timestep_type() == TIMESTEP_TYPE_REMOTE) // if external source dictates jiffies
        {
            IEC61850_server_timestep_sync(step++);
        }
        else // if internal time dictates jiffies
        {
            if ((sampleCount % 400) == 0)
            { // check each 400 samples
                uint64_t timeval = Hal_getTimeInMs();
                while (timeval < nextCycleStart + 100)
                { // wait until 100 milliseconds have elapsed
                  // (i.e. when 400 samples should have been send)
                    Thread_sleep(1);
                    timeval = Hal_getTimeInMs();
                }
                nextCycleStart = nextCycleStart + 100; // set timer for nex 100 milliseconds
            }
        }
    }
}
