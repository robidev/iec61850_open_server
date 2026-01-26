#include <libiec61850/iec61850_server.h>
#include <libiec61850/iec61850_model.h>
#include <libiec61850/hal_thread.h>

#include "open_server.h"
#include "iec61850_dynamic_model_extensions.h"
#include "iec61850_config_file_parser_extensions.h"
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "timestep_config.h"

#include "config_parser.h"
#include <stdio.h>
#include <string.h>

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
/*
ui_loop
	check_ui_requests:
		{"command": "open_breaker"}-> perform local operate
		{"command": "close_breaker"}-> perform local operate
		{"command": "reset_trip"} // maybe handled in UI logic instead

		{"command": "get_measurements"}
			Expected response format:
			{
			  "voltage_l1": 13.8, From MMXU
			  "voltage_l2": 13.7, From MMXU
			  "voltage_l3": 13.9, From MMXU
			  "current_l1": 125.5, From MMXU
			  "current_l2": 124.8, From MMXU
			  "current_l3": 126.2, From MMXU
			  "breaker_state": "CLOSED", From XCBR.Pos.stval
			  "trip_active": false -> need to be moddeled in PTRC or XCBR as cause of operate
			  "fault": false -> ncurrent Tr value (not moddeled in UI yet!)
			}
*/

// Socket stub
/*
 * IEC61850 Relay Simulator - Unix Socket Server
 * Compile: gcc -o relay_sim iec61850_stub.c -lm
 * Run: ./relay_sim /tmp/iec61850_relay_1.sock
 */

#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <errno.h>
#include <time.h>
#include <math.h>

#define BUFFER_SIZE 1024
#define SOCKET_PATH "/tmp/iec61850_relay_1.sock"

typedef enum {
    BREAKER_OPEN = 0,
    BREAKER_CLOSED = 1,
    BREAKER_UNKNOWN = 2
} BreakerState;

typedef struct {
    double voltage_l1;
    double voltage_l2;
    double voltage_l3;
    double current_l1;
    double current_l2;
    double current_l3;
    BreakerState breaker_state;
    int trip_active;
} RelayData;
//socket stub

int init(OpenServerInstance *srv)
{
    IedModel *model;
    IedModel_extensions *model_ex;

    printf(" ui_connector module initialising\n");
    model = srv->Model;
    model_ex = srv->Model_ex;
    
    config_t config;
    
    /* Parse the config file */
    if (config_parse_file("./plugin/ui_connector.config", &config) != 0) {
        printf("ERROR: Failed to parse config file\n");
        return 1;
    }
    
    /* Find a specific device section */
    config_section_t *section = config_find_section(&config, model->name);
    
    if (!section) {
        printf("ERROR: Device '%s' not found in config\n", model->name);
        config_free(&config);
        return 1;
    }

    printf(" Device: %s\n", section->section);
    const char *socket_path = config_get_value(section, "socket");

    /* Iterate through all key-value pairs */
    printf("\n === All settings for %s ===\n", model->name);
    for (int i = 0; i < section->entry_count; i++) {
        printf("  %s = ", section->entries[i].key);
        if (section->entries[i].value_count == 1) {
            printf("%s\n", section->entries[i].values[0]);
        } else {
            printf("[");
            for (int j = 0; j < section->entries[i].value_count; j++) {
                printf("%s%s", section->entries[i].values[j],
                       j < section->entries[i].value_count - 1 ? ", " : "");
            }
            printf("]\n");
        }
    }

    config_free(&config);

    printf("ui_connector module initialised\n");
    return 0; // 0 means success
}






/* Initialize relay with default values */
void init_relay(RelayData *relay) {
    relay->voltage_l1 = 110.0;
    relay->voltage_l2 = 110.0;
    relay->voltage_l3 = 110.0;
    relay->current_l1 = 0.0;
    relay->current_l2 = 0.0;
    relay->current_l3 = 0.0;
    relay->breaker_state = BREAKER_OPEN;
    relay->trip_active = 0;
}

/* Simulate realistic measurements */
void update_measurements(RelayData *relay) {
    static double phase = 0.0;
    phase += 0.1;
    if (phase > 2 * M_PI) phase -= 2 * M_PI;
    
    /* Add small variations to voltages */
    relay->voltage_l1 = 110.0 + sin(phase) * 2.0;
    relay->voltage_l2 = 110.0 + sin(phase + 2.094) * 2.0;  /* 120° phase shift */
    relay->voltage_l3 = 110.0 + sin(phase + 4.189) * 2.0;  /* 240° phase shift */
    
    /* Currents depend on breaker state */
    if (relay->breaker_state == BREAKER_CLOSED) {
        relay->current_l1 = 50.0 + sin(phase) * 5.0;
        relay->current_l2 = 50.0 + sin(phase + 2.094) * 5.0;
        relay->current_l3 = 50.0 + sin(phase + 4.189) * 5.0;
    } else {
        relay->current_l1 = 0.0;
        relay->current_l2 = 0.0;
        relay->current_l3 = 0.0;
    }
}

/* Build JSON response for measurements */
int build_response(RelayData *relay, char *buffer, size_t size) {
    const char *state_str = "UNKNOWN";
    if (relay->breaker_state == BREAKER_OPEN) state_str = "OPEN";
    else if (relay->breaker_state == BREAKER_CLOSED) state_str = "CLOSED";
    
    return snprintf(buffer, size,
        "{\"voltage_l1\":%.2f,\"voltage_l2\":%.2f,\"voltage_l3\":%.2f,"
        "\"current_l1\":%.2f,\"current_l2\":%.2f,\"current_l3\":%.2f,"
        "\"breaker_state\"%s\",\"trip_active\":%s}\n",
        relay->voltage_l1, relay->voltage_l2, relay->voltage_l3,
        relay->current_l1, relay->current_l2, relay->current_l3,
        state_str, relay->trip_active ? "true" : "false");
}

/* Simple JSON command parser */
void process_command(const char *cmd, RelayData *relay, char *response, size_t resp_size) {
    if (strstr(cmd, "get_measurements")) {
        update_measurements(relay);
        build_response(relay, response, resp_size);
    }
    else if (strstr(cmd, "open_breaker")) {
        relay->breaker_state = BREAKER_OPEN;
        snprintf(response, resp_size, "{\"status\":\"ok\",\"action\":\"breaker_opened\"}\n");
    }
    else if (strstr(cmd, "close_breaker")) {
        if (relay->trip_active) {
            snprintf(response, resp_size, "{\"status\":\"error\",\"message\":\"trip_active\"}\n");
        } else {
            relay->breaker_state = BREAKER_CLOSED;
            snprintf(response, resp_size, "{\"status\":\"ok\",\"action\":\"breaker_closed\"}\n");
        }
    }
    else if (strstr(cmd, "reset_trip")) {
        relay->trip_active = 0;
        snprintf(response, resp_size, "{\"status\":\"ok\",\"action\":\"trip_reset\"}\n");
    }
    else {
        snprintf(response, resp_size, "{\"status\":\"error\",\"message\":\"unknown_command\"}\n");
    }
}

int main(int argc, char *argv[]) {
    int server_fd, client_fd;
    struct sockaddr_un addr;
    char buffer[BUFFER_SIZE];
    char response[BUFFER_SIZE];
    RelayData relay;
    const char *socket_path = SOCKET_PATH;
    
    /* Allow socket path as command line argument */
    if (argc > 1) {
        socket_path = argv[1];
    }
    
    printf("Starting IEC61850 Relay Simulator on %s\n", socket_path);
    
    /* Initialize relay */
    init_relay(&relay);
    
    /* Create socket */
    server_fd = socket(AF_UNIX, SOCK_STREAM, 0);
    if (server_fd < 0) {
        perror("socket");
        return 1;
    }
    
    /* Remove existing socket file */
    unlink(socket_path);
    
    /* Bind socket */
    memset(&addr, 0, sizeof(addr));
    addr.sun_family = AF_UNIX;
    strncpy(addr.sun_path, socket_path, sizeof(addr.sun_path) - 1);
    
    if (bind(server_fd, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("bind");
        close(server_fd);
        return 1;
    }
    
    /* Listen for connections */
    if (listen(server_fd, 1) < 0) {
        perror("listen");
        close(server_fd);
        unlink(socket_path);
        return 1;
    }
    
    printf("Waiting for client connection...\n");
    
    /* Accept connection (blocking) */
    client_fd = accept(server_fd, NULL, NULL);
    if (client_fd < 0) {
        perror("accept");
        close(server_fd);
        unlink(socket_path);
        return 1;
    }
    
    printf("Client connected!\n");
    
    /* Main command loop */
    while (1) {
        ssize_t bytes_read = read(client_fd, buffer, BUFFER_SIZE - 1);
        
        if (bytes_read <= 0) {
            if (bytes_read == 0) {
                printf("Client disconnected\n");
            } else {
                perror("read");
            }
            break;
        }
        
        buffer[bytes_read] = '\0';
        printf("Received: %s", buffer);
        
        /* Process command and build response */
        process_command(buffer, &relay, response, BUFFER_SIZE);
        
        /* Send response */
        ssize_t bytes_written = write(client_fd, response, strlen(response));
        if (bytes_written < 0) {
            perror("write");
            break;
        }
        
        printf("Sent: %s", response);
    }
    
    /* Cleanup */
    close(client_fd);
    close(server_fd);
    unlink(socket_path);
    
    printf("Server shutdown\n");
    return 0;
}