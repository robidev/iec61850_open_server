/*
 *  open_server.c
 */

#include "inputs_api.h"
#include "iec61850_model_extensions.h"
#include "iec61850_dynamic_model_extensions.h"
#include "iec61850_config_file_parser_extensions.h"
#include "LNParse.h"
#include "timestep_config.h"
#include "open_server.h"

#include <libiec61850/sv_publisher.h>
#include <libiec61850/hal_thread.h> /* for Thread_sleep() */

#include <signal.h>
#include <stdlib.h>
#include <unistd.h> // for getopt
#include <stdio.h>
#include <time.h>

#include <dirent.h>
#include <sys/stat.h>
#include <dlfcn.h>

#include <libiec61850/hal_socket.h>

static int global_step = 0;
static int global_timestep_type = TIMESTEP_TYPE_LOCAL; // TIMESTEP_TYPE_REMOTE
static int running = 0;


void IEC61850_server_timestep_next_step()
{
	global_step++;
	// printf("step: %i\n",global_step);
}

void IEC61850_server_timestep_sync(int local)
{
	while (local >= global_step)
		Thread_sleep(1);
}

int IEC61850_server_timestep_async(int local)
{
	if (local == global_step)
	{
		Thread_sleep(1);
		return 1;
	}
	else
	{
		return 0;
	}
}

int IEC61850_server_timestep_type()
{
	return global_timestep_type;
}

void sigint_handler(int signalId)
{
	printf("--- stopping server due to SIGINT ---\n\n");
	running = 0;
}

int open_server_running()
{
	return running;
}


static MmsError
fileAccessHandler (void* parameter, MmsServerConnection connection, MmsFileServiceType service,
                                          const char* localFilename, const char* otherFilename)
{
    printf("fileAccessHandler: service = %i, local-file: %s other-file: %s\n", service, localFilename, otherFilename);

    /* Don't allow client to rename files */
    if (service == MMS_FILE_ACCESS_TYPE_RENAME)
        return MMS_ERROR_FILE_FILE_ACCESS_DENIED;

    /* Don't allow client to delete files */
    if (service == MMS_FILE_ACCESS_TYPE_DELETE) {
        //if (strcmp(localFilename, "IEDSERVER.BIN") == 0)
        return MMS_ERROR_FILE_FILE_ACCESS_DENIED;
    }

    /* allow all other accesses */
    return MMS_ERROR_NONE;
}

int main(int argc, char **argv)
{
	OpenServerInstance openServer;
	openServer.server = NULL;
	openServer.Model = NULL;
	//IedModel *iedModel_local = NULL;			
	openServer.Model_ex = NULL;		
	//IedModel_extensions *iedExtendedModel_local = NULL; 
	openServer.allInputValues = NULL;
	openServer.SMVControlInstances = NULL;

    int port = 102;
    char *ethernetIfcID = NULL; // no default here
    char *ipAddress = NULL;
    char *cfgFile = NULL;
    char *extFile = NULL;
    char timestep_type = 0;

    // Flags to track if option is explicitly set
    int opt_e_set = 0, opt_p_set = 0, opt_c_set = 0, opt_x_set = 0, opt_t_set = 0;

    int opt;
    while ((opt = getopt(argc, argv, "e:p:i:c:x:t:")) != -1) {
        switch(opt) {
            case 'e': ethernetIfcID = optarg; opt_e_set = 1; break;
            case 'p': port = atoi(optarg); opt_p_set = 1; break;
            case 'i': ipAddress = optarg; break;
            case 'c': cfgFile = optarg; opt_c_set = 1; break;
            case 'x': extFile = optarg; opt_x_set = 1; break;
            case 't': timestep_type = optarg[0]; opt_t_set = 1; break;
            default:
                fprintf(stderr, "Usage: %s [-e ethernet] [-p port] [-i ip] [-c cfgfile] [-x extfile] [-t L|R]\n", argv[0]);
                exit(EXIT_FAILURE);
        }
    }

    // Backwards compatibility with positional arguments if options not set
    int pos_index = optind;
    if (!opt_e_set && argc > pos_index) ethernetIfcID = argv[pos_index++];
    if (!opt_p_set && argc > pos_index) port = atoi(argv[pos_index++]);
    if (!opt_c_set && argc > pos_index) cfgFile = argv[pos_index++];
    if (!opt_x_set && argc > pos_index) extFile = argv[pos_index++];
    if (!opt_t_set && argc > pos_index) timestep_type = argv[pos_index][0];

    // Use default for interface if still NULL
    if (!ethernetIfcID) ethernetIfcID = "lo";


    if (cfgFile && extFile) {
        openServer.Model = ConfigFileParser_createModelFromConfigFileEx(cfgFile);
        openServer.Model_ex = ConfigFileParser_createModelFromConfigFileEx_inputs(extFile, openServer.Model);

        if (openServer.Model == NULL || openServer.Model_ex == NULL) {
            printf("Parsing dynamic config failed! Exit.\n");
            exit(-1);
        }
    } else {
        printf("No valid model provided! Exit.\n");
        exit(-1);
    }

    if (timestep_type == 'L' || timestep_type == 0){
        global_timestep_type = TIMESTEP_TYPE_LOCAL;
		timestep_type = 'L';
	}
    else if (timestep_type == 'R')
        global_timestep_type = TIMESTEP_TYPE_REMOTE;
    else {
        printf("Invalid timestep type! Use 'L' or 'R'.\n");
        exit(-1);
    }


	openServer.server = IedServer_create(openServer.Model);

    printf("Using interface: %s\n", ethernetIfcID);
    if (ipAddress){
		printf("Using IP address: %s\n", ipAddress);
		IedServer_setLocalIpAddress(openServer.server,ipAddress);
	} 
    printf("Using port: %d\n", port);	
	

	// By default we deny writing to SP elements, unless we have explicitly installed a write handler inside the LN init. example: PTOC installs this for StrVal
	IedServer_setWriteAccessPolicy(openServer.server, IEC61850_FC_SP, ACCESS_POLICY_DENY);

	GooseReceiver GSEreceiver = GooseReceiver_create();
	SVReceiver SMVreceiver = SVReceiver_create();

	/* set GOOSE interface for all GOOSE publishers (GCBs) */
	IedServer_setGooseInterfaceId(openServer.server, ethernetIfcID);
	// goose subscriber
	GooseReceiver_setInterfaceId(GSEreceiver, ethernetIfcID);
	// smv subscriber
	SVReceiver_setInterfaceId(SMVreceiver, ethernetIfcID);

	// subscribe to datasets and local DA's based on iput/extRef, and generate one list with all inputValues
	openServer.allInputValues = subscribeToGOOSEInputs(openServer.Model_ex, GSEreceiver);
	LinkedList temp = LinkedList_getLastElement(openServer.allInputValues);
	temp->next = subscribeToSMVInputs(openServer.Model_ex, SMVreceiver);
	temp = LinkedList_getLastElement(temp);
	temp->next = subscribeToLocalDAInputs(openServer.server,openServer.Model_ex, openServer.Model);

	// start subscribers
	GooseReceiver_start(GSEreceiver);
	SVReceiver_start(SMVreceiver);

	if (GooseReceiver_isRunning(GSEreceiver) || SVReceiver_isRunning(SMVreceiver))
	{
		printf("receivers working...\n");
	}
	else
	{
		printf("WARNING: no receivers are running\n");
	}

	/* MMS server will be instructed to start listening to client connections. */
	IedServer_start(openServer.server, port);
	running = 1;

	if (!IedServer_isRunning(openServer.server))
	{
		printf("Starting server failed! Exit.\n");
		IedServer_destroy(openServer.server);
		exit(-1);
	}

	// call initializers for sampled value control blocks and start publishing
	openServer.SMVControlInstances = attachSMV(openServer.server, openServer.Model, openServer.allInputValues, ethernetIfcID);

	// call all initializers for logical nodes in the model
	attachLogicalNodes(openServer.server, openServer.Model, openServer.Model_ex, openServer.allInputValues);

	/* Start GOOSE publishing */
	IedServer_enableGoosePublishing(openServer.server);

	/* PLUGIN SYSTEM */
	// load all .so in plugin folder, and call init
	// plugins are allowed to call exported functions from main executable

	printf("\n--- loading plugins ---\n");
	DIR *d;
	struct dirent *dir;
	d = opendir("./plugin");
	if (d)
	{
		while ((dir = readdir(d)) != NULL)
		{
			void *so_handle = NULL;
			lib_init_func init_func = NULL;

			size_t namelen = strlen(dir->d_name);

			if (dir->d_type != DT_REG ||										   // only regular files
				strcmp(".", dir->d_name) == 0 || strcmp("..", dir->d_name) == 0 || // ignore . and ..
				namelen < 4 ||													   // ensure namelength is large enough to be calles ?.so
				strcmp(".so", dir->d_name + namelen - 3) != 0)					   // check if name ends with .so
			{
				continue;
			}
			printf("loading plugin: %s\n", dir->d_name);

			char *fullname = malloc(namelen + 10);
			strcpy(fullname, "./plugin/");
			strncat(fullname, dir->d_name, namelen + 10);
			so_handle = dlopen(fullname, RTLD_NOW | RTLD_GLOBAL);
			free(fullname);

			if (so_handle == NULL)
			{
				printf("ERROR: Unable to open lib: %s\n", dlerror());
				continue;
			}
			init_func = dlsym(so_handle, "init");

			if (init_func == NULL)
			{
				printf("ERROR: Unable to get symbol\n");
				continue;
			}
			if (init_func(&openServer) != 0)
			{
				printf("ERROR: could not succesfully run init of plugin: %s\n", dir->d_name);
			}
			printf("\n");
		}
		closedir(d);
	}
	printf("--- loading plugins finished ---\n\n");


	IedServer_setFilestoreBasepath(openServer.server, "./vmd-filestore/");
	/* Set a callback handler to control file accesses */
	MmsServer_installFileAccessHandler(IedServer_getMmsServer(openServer.server), fileAccessHandler, NULL);



	signal(SIGINT, sigint_handler);
	while (running)
	{
		Thread_sleep(1000);
		fflush(stdout); // ensure logging is flushed every second
	}


	GooseReceiver_stop(GSEreceiver);

	GooseReceiver_destroy(GSEreceiver);

	SVReceiver_stop(SMVreceiver);
	/* Cleanup and free resources */
	SVReceiver_destroy(SMVreceiver);
	/* stop MMS server - close TCP server socket and all client sockets */
	IedServer_stop(openServer.server);
	/* Cleanup - free all resources */
	IedServer_destroy(openServer.server);


} /* main() */
