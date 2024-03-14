#include <libiec61850/iec61850_server.h>
#include <libiec61850/iec61850_model.h>
#include <libiec61850/hal_thread.h>
#include <math.h>

#include "open_server.h"
#include "iec61850_dynamic_model_extensions.h"
#include "iec61850_config_file_parser_extensions.h"
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "timestep_config.h"
#include "SMVPublisher.h"
#include "LNParse.h"
#include "TCTR.h"
#include "TVTR.h"

typedef struct sLSMS
{
    void *instance;
    double angle;
    double magnitude;
    double freq;
    void *sibling;
} LSMS;

static void local_SMV_Thread(void *parameter);
static void SMV_Callback(int samplecount, void *parameter);

static LSMS* lsms_list = NULL;

LSMS* get_sample_simulation_setting(int index)
{
    LSMS* item = lsms_list;
    int i=0;
    while (item)
    {
        if(index == i)
        {
            return item;
        }
        i++;
        item = item->sibling;
    }
    return NULL;
}

//TODO: not threat safe! add a semaphore
int update_sample_simulation_magnitude(int index, double magnitude)
{
    LSMS* item = lsms_list;
    int i=0;
    while (item)
    {
        if(index == i)
        {
            item->magnitude = magnitude;
            return 1;
        }
        i++;
        item = item->sibling;
    }
    return 0;
}

int init(OpenServerInstance *srv)
{
    IedModel *model;
    IedModel_extensions *model_ex;
    printf(" local_sample_simulation module initialising\n");
    model = srv->Model;
    model_ex = srv->Model_ex;
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    int read;

    fp = fopen("./plugin/local_sample_simulator.config", "r");
    if (fp == NULL)
    {
        printf(" ERROR: could not open local_sample_simulator.config\n");
        return 0;
    }
    printf(" opened local_sample_simulator.config\n");

    int state = 0;
    uint8_t type = 0;
    char svcb[130] = "";
    LSMS *head = NULL;
    LSMS *tail = NULL;
    // TODO: make this config sensible for mutliple TCTR/TVTR and smvcb
    while ((read = getline(&line, &len, fp)) != -1)
    {
        // printf("Retrieved line of length %zu:\n", read); printf("%s", line);
        if (line == NULL || *line == 0)
            continue;

        switch (state)
        {
        case 0:
            type = *line;
            state = 1;
            break;
        case 1:
        {
            // strncpy(svcb, line, 130);
            int machtedItems = sscanf(line, "%130s", svcb);
            if (machtedItems < 1)
                continue;
            state = 2;
        }
        break;
        case 2:
        {
            char logical_node[130];
            double angle;
            double magnitude;
            double freq;
            int machtedItems = sscanf(line, "%130s %lf %lf %lf", logical_node, &angle, &magnitude, &freq);
            if (machtedItems < 4)
                continue;

            LogicalNodeClass *ln = getLNClass(model, model_ex, logical_node);
            if (ln == NULL)
                continue;
            // make linked list of LSMS, head for first item
            //  provide head to inst
            LSMS *inst = (LSMS *)malloc(sizeof(LSMS));
            inst->instance = ln->instance;
            inst->angle = angle;
            inst->magnitude = magnitude;
            inst->freq = freq;
            inst->sibling = NULL;

            if (head == NULL)
            {
                head = inst;
                tail = inst;
                lsms_list = inst;
            }
            else
            {
                tail->sibling = inst;
                tail = inst;
            }
        }
        break;
        }
    }
    fclose(fp);
    if (line)
        free(line);

    if (state != 2)
    {
        printf(" ERROR: could not parse file\n");
        printf(" First line has to be T for Threat or C for Callback\n");
        printf(" Second line an smvref or 'none' \n");
        printf(" other lines should refer to TCTR or TVTR instances\n");
        return 1;
    }
    printf(" file parsed succesfully\n");

    if (type == 'T')
    {
        Thread thread = Thread_create((ThreadExecutionFunction)local_SMV_Thread, head, true);
        Thread_start(thread);
    }
    else if (type == 'C')
    {
        SMVcB *smv = getSMVInstance(model, srv->SMVControlInstances, svcb);
        if (smv == NULL)
        {
            printf(" ERROR: cannot find SMV instance: %s in model\n", svcb);
            return 1;
        }
        setSampleCallback(smv->instance, SMV_Callback, head);
    }
    else
    {
        printf(" ERROR: unrecognised option. First line has to be T or C\n");
        return 1;
    }

    printf(" local_sample_simulation module initialised\n");
    return 0; // 0 means success
}

static void SMV_Callback(int sampleCount, void *parameter)
{
    // printf("smv callback called\n");
    LSMS *item = (LSMS *)parameter;

    double samplePoint = sampleCount % 80;

    while (item)
    {
        int measurement = 0;
        if (item->magnitude > 0.001 && item->freq > 0.1)
        {
            double amp = item->magnitude * sqrt(2); // RMS to peak
            double angle = ((item->freq / 25) * M_PI / 80) * samplePoint - (item->angle * M_PI / 180.0);
            measurement = (int)((amp * sin(angle)) * 1000);
        }
        // for all refs
        TCTR *inst = item->instance;
        IedServer_updateInt32AttributeValue(inst->server, inst->da, measurement);
        InputValueHandleExtensionCallbacks(inst->da_callback); // update the associated callbacks with this Data Element (e.g. MMXU)

        item = item->sibling;
    }
}

static void local_SMV_Thread(void *parameter)
{
    printf(" smv thread started\n");
    int sampleCount = 0;

    uint64_t nextCycleStart = Hal_getTimeInMs() + 1000;
    while (open_server_running())
    {
        /* update measurement values */
        int samplePoint = sampleCount % 80;

        LSMS *item = (LSMS *)parameter;
        while (item)
        {
            int measurement = 0;
            if (item->magnitude > 0.001 && item->freq > 0.1)
            {
                double amp = item->magnitude * sqrt(2); // RMS to peak
                double angle = ((item->freq / 25) * M_PI / 80) * samplePoint - (item->angle * M_PI / 180.0);
                measurement = (int)((amp * sin(angle)) * 1000);
            }

            // for all refs
            TCTR *inst = item->instance;
            IedServer_updateInt32AttributeValue(inst->server, inst->da, measurement);
            InputValueHandleExtensionCallbacks(inst->da_callback); // update the associated callbacks with this Data Element (e.g. MMXU)

            item = item->sibling;
        }

        sampleCount = ((sampleCount + 1) % 4000);

        if ((sampleCount % 400) == 0)
        {
            uint64_t timeval = Hal_getTimeInMs();

            while (timeval < nextCycleStart + 100)
            {
                Thread_sleep(1);

                timeval = Hal_getTimeInMs();
            }

            nextCycleStart = nextCycleStart + 100;
        }
    }
}
