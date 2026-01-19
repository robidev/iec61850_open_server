#include <libiec61850/iec61850_server.h>
#include <libiec61850/iec61850_model.h>
#include <libiec61850/hal_thread.h>

#include "open_server.h"
#include "iec61850_dynamic_model_extensions.h"
#include "iec61850_config_file_parser_extensions.h"
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "timestep_config.h"

int init(OpenServerInstance *srv)
{
    IedModel *model;
    IedModel_extensions *model_ex;

    printf(" ui_connector module initialising\n");
    model = srv->Model;
    model_ex = srv->Model_ex;
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    int read;
    char logical_node[130];

    fp = fopen("./plugin/ui_connector.config", "r");
    if (fp == NULL)
    {
        printf(" ERROR: could not open ui_connector.config\n");
        return 0;
    }
    printf(" opened ui_connector.config\n");

    // get lines with logical nodes, and the time needed for open, close, default-pos
    while ((read = getline(&line, &len, fp)) != -1)
    {
        int machtedItems = sscanf(line, "%130s", logical_node);
        if (machtedItems < 4)
            continue;

    }

    printf("ui_connector module initialised\n");
    return 0; // 0 means success
}

// check ied-name, for config-entry
// open listen socket based on config
// wait for connection from ui
// if connected, handle requests for data, to send status-info for display
// when an operate open/close is send, then act, also trip-reset(for latching trip)
// local-remote setting
// possible protection-settings(trip-current, trip-time)
//
//config-layout:
// IED-name:NAME (to select right config)
// socket:SOCKET_NAME
//
// connected elements:
// - REF XSWI1,swi1
// - REF XCBR,cbr1
// - REF XSWI3,swi2
// - REF XSWI4,swi3
// - REF MMXU,ct-vals
// - REF LLN0.Loc,loc/remote
// - REF PTOC, I>
// - REF PTOC, Tm
//end