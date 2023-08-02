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

static IedModel *model;
static IedModel_extensions *model_ex;

void SMV_Thread();
void SMV_Callback(int samplecount, void *parameter);

int init(IedModel *Model, IedModel_extensions *Model_ex)
{
    printf("local_sample_simulation module initialising\n");
    model = Model;
    model_ex = Model_ex;
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    int read;

    fp = fopen("local_sample_simulator.config", "r");
    if (fp == NULL)
        return 0;

    // TODO: make this config sensible for mutliple TCTR/TVTR and smvcb
    while ((read = getline(&line, &len, fp)) != -1)
    {
        // printf("Retrieved line of length %zu:\n", read); printf("%s", line);
        if (line == NULL || *line == 0)
            continue;

        char logical_node[130];
        uint8_t type = 0;
        char svcb[130];
        int matchedItems = sscanf(line, "%130s %c %130s", logical_node, &type, svcb);
        if (matchedItems < 2)
            continue;

        LogicalNodeClass *ln = getLNClass(model, model_ex, logical_node);
        if (ln == NULL)
            continue;

        if (type == 'T' && matchedItems == 2) // use thread
        {
            // use same thread for all TCTR and TVTR
            //  ...
            //
            Thread thread = Thread_create((ThreadExecutionFunction)SMV_Thread, ln->instance, true);
            Thread_start(thread);
        }
        else if (type == 'C' && matchedItems == 3) // use callback
        {
            // use same callback to update all TCTR and TVTR
            //  ...
            //
            SMVcB *smv = getSMVInstance(Model, Model_ex, svcb);
            setSampleCallback(smv->instance, SMV_Callback, ln->instance);
        }
        else
            continue;
    }

    fclose(fp);
    if (line)
        free(line);

    printf("local_sample_simulation module initialised\n");
    return 0; // 0 means success
}

void SMV_Callback(int sampleCount, void *parameter)
{
    printf("smv callback called");
    int measurements[8];

    int vol = (int)(6350.f * sqrt(2)); // RMS to peak
    int amp = (int)(10.f * sqrt(2));   // RMS to peak
    float phaseAngle = 0.f;

    /* update measurement values */
    int samplePoint = sampleCount % 80;

    double angleA = (2 * M_PI / 80) * samplePoint;
    double angleB = (2 * M_PI / 80) * samplePoint - (2 * M_PI / 3);
    double angleC = (2 * M_PI / 80) * samplePoint - (4 * M_PI / 3);

    measurements[0] = (amp * sin(angleA - phaseAngle)) * 1000;
    measurements[1] = (amp * sin(angleB - phaseAngle)) * 1000;
    measurements[2] = (amp * sin(angleC - phaseAngle)) * 1000;
    measurements[3] = measurements[0] + measurements[1] + measurements[2]; // should be 0

    measurements[4] = (vol * sin(angleA)) * 100;
    measurements[5] = (vol * sin(angleB)) * 100;
    measurements[6] = (vol * sin(angleC)) * 100;
    measurements[7] = measurements[4] + measurements[5] + measurements[6]; // should be 0

    // for all refs
    // IedServer_updateInt32AttributeValue(inst->server,inst->da,i);
    // InputValueHandleExtensionCallbacks(inst->da_callback); //update the associated callbacks with this Data Element (e.g. MMXU)
}

void SMV_Thread(void *parameter)
{
    int measurements[8];

    int vol = (int)(6350.f * sqrt(2)); // RMS to peak
    int amp = (int)(10.f * sqrt(2));   // RMS to peak
    float phaseAngle = 0.f;

    int sampleCount = 0;

    uint64_t nextCycleStart = Hal_getTimeInMs() + 1000;
    while (open_server_running())
    {
        /* update measurement values */
        int samplePoint = sampleCount % 80;

        double angleA = (2 * M_PI / 80) * samplePoint;
        double angleB = (2 * M_PI / 80) * samplePoint - (2 * M_PI / 3);
        double angleC = (2 * M_PI / 80) * samplePoint - (4 * M_PI / 3);

        measurements[0] = (amp * sin(angleA - phaseAngle)) * 1000;
        measurements[1] = (amp * sin(angleB - phaseAngle)) * 1000;
        measurements[2] = (amp * sin(angleC - phaseAngle)) * 1000;
        measurements[3] = measurements[0] + measurements[1] + measurements[2]; // should be 0

        measurements[4] = (vol * sin(angleA)) * 100;
        measurements[5] = (vol * sin(angleB)) * 100;
        measurements[6] = (vol * sin(angleC)) * 100;
        measurements[7] = measurements[4] + measurements[5] + measurements[6]; // should be 0

        // for all refs
        // IedServer_updateInt32AttributeValue(inst->server,inst->da,i);
        // InputValueHandleExtensionCallbacks(inst->da_callback); //update the associated callbacks with this Data Element (e.g. MMXU)

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
