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

    printf(" hw_connector module initialising\n");
    model = srv->Model;
    model_ex = srv->Model_ex;
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    int read;
    char logical_node[130];

    fp = fopen("./plugin/hw_connector.config", "r");
    if (fp == NULL)
    {
        printf(" ERROR: could not open hw_connector.config\n");
        return 0;
    }
    printf(" opened hw_connector.config\n");

    // get lines with logical nodes, and the time needed for open, close, default-pos
    while ((read = getline(&line, &len, fp)) != -1)
    {
        int machtedItems = sscanf(line, "%130s", logical_node);
        if (machtedItems < 4)
            continue;

    }

    printf("hw_connector module initialised\n");
    return 0; // 0 means success
}

// check ied-name, for config-entry
// connect to socket based on config
// connect cbr callback to xcbr/xswi and io-index based on config
// receive switch-status events, and modify respective stval(ref in config)
// when an operate-signal is send, send set io command over socket, based on config
// receive transformer-data and write it into CTR/VTR elements
//
// possible timestep call from socket to all clients?(to pace and sync the ieds?)
// possible dsp-override: if so, when a dsp-processing call is made, we just provide the rms-value the sine was calced from in the first place
//
//config-layout:
// IED-name:NAME (to select right config)
// socket:SOCKET_NAME
//
// SWI-Refs: (routing events, and sending operates)
// - REF1 XSWI1,IO-index1 
// - REF2 XCBR1,IO-index10
// - REF3 XSWI3,IO-index3
// - REF4 XWSI4,IO-index4
//
// TR-refs: (subscribe to transformer-data)
// - REF1 CTR1, DATA-index1, generate sine-0, based on index1
// - REF1 CTR2, DATA-index2, generate sine-90, based on index2
// - REF1 CTR3, DATA-index3, generate sine-180, based on index3
// - REF1 CTR4, inferred
//end