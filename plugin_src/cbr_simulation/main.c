#include <libiec61850/iec61850_server.h>
#include <libiec61850/iec61850_model.h>
#include <libiec61850/hal_thread.h>

#include "open_server.h"
#include "iec61850_dynamic_model_extensions.h"
#include "iec61850_config_file_parser_extensions.h"
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "timestep_config.h"
#include "LNParse.h"
#include "XSWI.h"

typedef struct sSwConfig
{
    int open_time;
    int close_time;
    int default_pos;
} SwConfig;

// process simulator
void simulate_switch_close(void *inst);
void simulate_switch_open(void *inst);

void callback_from_LN(void *inst, bool state)
{;
    // trigger for simulated servo/relay move
    Thread thread;
    if (state == true)
        thread = Thread_create((ThreadExecutionFunction)simulate_switch_close, inst, true);
    else
        thread = Thread_create((ThreadExecutionFunction)simulate_switch_open, inst, true);
    Thread_start(thread);
}

int init(IedModel *Model, IedModel_extensions *Model_ex)
{
    IedModel *model;
    IedModel_extensions *model_ex;

    printf("cbr simulation module initialising\n");
    model = Model;
    model_ex = Model_ex;
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    int read;
    char logical_node[130];

    fp = fopen("cbr_simulator.config", "r");
    if (fp == NULL)
    {
        printf("ERROR: could not open cbr_simulator.config\n");
        return 0;
    }
    printf("opened cbr_simulator.config\n");

    // get lines with logical nodes, and the time needed for open, close, default-pos
    while ((read = getline(&line, &len, fp)) != -1)
    {
        int open_time = 0;
        int close_time = 0;
        int default_pos = 0;
        int machtedItems = sscanf(line, "%130s %d %d %d", logical_node, &open_time, &close_time, &default_pos);
        if (machtedItems < 4)
            continue;

        LogicalNodeClass *ln = getLNClass(model, model_ex, logical_node);
        if (ln == NULL)
            continue;
        XSWI *item = ln->instance;

        SwConfig *conf = (SwConfig *)malloc(sizeof(SwConfig));
        conf->open_time = open_time;
        conf->close_time = close_time;
        conf->default_pos = default_pos;
        item->config = conf;
        setXSWI_Callback(item, callback_from_LN);

        if(default_pos == 1)
            XSWI_change_switch(item, DBPOS_ON);
        else
            XSWI_change_switch(item, DBPOS_OFF);

        printf("* logical node: %s initialised with open_time: %d, close_time: %d, default position: %d\n",
               logical_node, open_time, close_time, default_pos);
    }

    printf("cbr_simulation module initialised\n");
    return 0; // 0 means success
}

// threath for process-simulation: open/close switch
void simulate_switch_close(void *inst)
{
    XSWI *instance = inst;
    Semaphore_wait(instance->sem);

    SwConfig *conf = instance->config;
    Dbpos stval = Dbpos_fromMmsValue(IedServer_getAttributeValue(instance->server, instance->Pos_stVal));

    if (stval != DBPOS_ON) // position is not closed/on and we issue a command to close
    {
        printf("SWI: closing\n");
        XSWI_change_switch(instance, DBPOS_INTERMEDIATE_STATE);

        Thread_sleep(conf->close_time);
        printf("SWI: closed\n");
        XSWI_change_switch(instance, DBPOS_ON);
    }
    Semaphore_post(instance->sem);
}
void simulate_switch_open(void *inst)
{
    XSWI *instance = inst;
    Semaphore_wait(instance->sem);

    SwConfig *conf = instance->config;
    Dbpos stval = Dbpos_fromMmsValue(IedServer_getAttributeValue(instance->server, instance->Pos_stVal));

    if (stval != DBPOS_OFF) // position is not open/off and we issue a command to open
    {
        printf("SWI: opening\n");
        XSWI_change_switch(instance, DBPOS_INTERMEDIATE_STATE);

        Thread_sleep(conf->open_time);
        XSWI_change_switch(instance, DBPOS_OFF);
        printf("SWI: opened\n");
    }
    Semaphore_post(instance->sem);
}
