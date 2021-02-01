/*
 *  server_example_inputs.c
 *
 *  This example demonstrates how to use inputs, GOOSE and SMV subscribing.
 *
 */

#include "inputs_api.h"
#include "iec61850_model_extensions.h"
#include "iec61850_dynamic_model_extensions.h"
#include "iec61850_config_file_parser_extensions.h"
#include "LNParse.h"
#include <libiec61850/sv_publisher.h>

#include <libiec61850/iec61850_server.h>
#include <libiec61850/hal_thread.h> /* for Thread_sleep() */
#include "simulation_config.h"

#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#include <string.h> //strlen 
#include <errno.h> 
#include <unistd.h> //close 
#include <arpa/inet.h> //close 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 
#include <sys/time.h> //FD_SET, FD_ISSET, FD_ZERO macros 

#include <libiec61850/hal_socket.h>

#define PORT 65000
#define SOCKETS 65

static int running = 0;
static IedServer iedServer = NULL;
static int global_step = 0;
static int global_simulation_type = SIMULATION_TYPE_LOCAL;


typedef void (*simulationFunction) (int sd, char * buffer, void* param);
typedef struct sLNStruct 
{
	simulationFunction call_simulation;
} LNStruct;


void sigint_handler(int signalId)
{
	running = 0;
}

void IEC61850_server_simulation_next_step()
{
	global_step++;
	//printf("step: %i\n",global_step);
}

void IEC61850_server_simulation_sync(int local)
{
    while(local == global_step)
		Thread_sleep(1);
}

int IEC61850_server_simulation_async(int local)
{
    if(local == global_step)
	{
		Thread_sleep(1);
		return 1;
	}
	else
	{
		return 0;
	}
	
}

int IEC61850_server_simulation_type()
{ 
	return global_simulation_type; 
}

int simulation_thread(IedModel* model, IedModel_extensions* model_ex, uint16_t port) 
{ 
	int opt = 1; 
	int master_socket;
	int addrlen;
	int new_socket;
	int client_socket[SOCKETS];
	int max_clients = SOCKETS;
	void * LNi[SOCKETS];
	int activity;
	int i;
	int valread;
	int sd; 
	int max_sd; 
	struct sockaddr_in address; 

	char * message = "init\n";
		
	char buffer[1025]; //data buffer of 1K 
		
	//set of socket descriptors 
	fd_set readfds; 

	
	for (i = 0; i < max_clients; i++) { //initialise all client_socket[] to 0
		client_socket[i] = 0; 
		LNi[i] = 0;
	} 
		
	//create a master socket 
	if( (master_socket = socket(AF_INET , SOCK_STREAM , 0)) == 0) { 
		perror("socket failed"); 
		return -1;
	} 
	
	//set master socket to allow multiple connections , 
	if( setsockopt(master_socket, SOL_SOCKET, SO_REUSEADDR, (char *)&opt, sizeof(opt)) < 0 ) { 
		perror("setsockopt"); 
		return -1; 
	} 
	
	//type of socket created 
	address.sin_family = AF_INET; 
	address.sin_addr.s_addr = INADDR_ANY; 
	address.sin_port = htons( port ); 
		
	//bind the socket to localhost port 8888 
	if (bind(master_socket, (struct sockaddr *)&address, sizeof(address))<0) { 
		perror("bind failed"); 
		return -1;  
	} 
		
	//try to specify maximum of 3 pending connections for the master socket 
	if (listen(master_socket, 3) < 0) { 
		perror("listen"); 
		return -1;
	} 
	addrlen = sizeof(address); 
		
	running = 1;

	signal(SIGINT, sigint_handler);

	while(running) 
	{ 
		Thread_sleep(1);
		//clear the socket set 
		FD_ZERO(&readfds); 
	
		//add master socket to set 
		FD_SET(master_socket, &readfds); 
		max_sd = master_socket; 
			
		//add child sockets to set 
		for ( i = 0 ; i < max_clients ; i++) { 
			sd = client_socket[i]; //socket descriptor 
			
			if(sd > 0) //if valid socket descriptor then add to read list 
				FD_SET( sd , &readfds); 
				
			//highest file descriptor number, need it for the select function 
			if(sd > max_sd) 
				max_sd = sd; 
		} 
		struct timeval y = {0,0};

		//wait for an activity on one of the sockets , timeout is NULL , so wait indefinitely 
		activity = select( max_sd + 1 , &readfds , NULL , NULL , &y); 
	
		if ((activity < 0) && (errno!=EINTR)) { 
			printf("select error"); 
		} 
			
		//If something happened on the master socket , then its an incoming connection 
		if (FD_ISSET(master_socket, &readfds)) 
		{ 
			if ((new_socket = accept(master_socket, 
					(struct sockaddr *)&address, (socklen_t*)&addrlen))<0) 
			{ 
				perror("accept"); 
				return -1;
			} 

			//add new socket to array of sockets 
			for (i = 0; i < max_clients; i++) { 
				if( client_socket[i] == 0 ) { //if position is empty 
					client_socket[i] = new_socket; 
					printf("new conn, sock:%i\n", i);
					break; 
				} 
			} 
		} 
		//else its some IO operation on some other socket 
		for (i = 0; i < max_clients; i++) 
		{ 
			sd = client_socket[i]; 
				
			if (FD_ISSET( sd , &readfds)) 
			{ 
				//Check if it was for closing , and also read the incoming message 
				if ((valread = read( sd , buffer, 1024)) == 0) 
				{  
					printf("Client disconnected\n"); 		
					//Close the socket and mark as 0 in list for reuse 
					close( sd ); 
					client_socket[i] = 0; 
					LNi[i] = 0;
				} 
				else //process the data
				{ 

					//process buf
					switch(buffer[0])
					{
						case 'i'://case init: relate sock to an LN inst
						{
							if(buffer[valread-1] != '\n')
								perror("send init NO trailing newline"); 
							buffer[valread-1] = 0;
							//find LN, extended LN inst,
							LogicalNodeClass* ln = getLNClass(model, model_ex, buffer+2); //based on LN in model, find LNinst(parent LN) in extension
							if(ln != NULL){
								void * inst = ln->instance;
								//register simulation get/set calls
								LNi[i] = inst;

								if( send(sd, "OK\n", 3, 0) != 3 ) { 
									perror("send init OK"); 
								} 
							}
							else {
								if( send(sd, "NOK\n", 4, 0) != 4 ) { 
									perror("send init NOK"); 
								} 
							}


							break;
						}
						case 'g':
						case 's'://case send set/get to respective ln inst.->set values, get values
						{
							if(buffer[valread-1] != '\n')
								perror("send value NO trailing newline"); 
							buffer[valread-1] = 0;//make string zero-terminated
							if(LNi[i] != 0) {
								simulationFunction call_simulation = ((LNStruct*)LNi[i])->call_simulation;
								if(call_simulation != NULL)
									call_simulation(sd, buffer, LNi[i]); // process_command
							}
							break;
						}
						case 'n'://case next=perform next simulation step
						{
							IEC61850_server_simulation_next_step();
							if( send(sd, "OK\n", 3, 0) != 3 ) { 
								perror("send next step"); 
							} 
							break;
						}
					}
				} 
			} 
		} 
	} 
		
	return 0; 
} 


int main(int argc, char** argv) {

	IedModel* iedModel_local = NULL;//&iedModel;
	IedModel_extensions* iedExtendedModel_local = NULL;//&iedExtendedModel;

	int port = 102;
	uint16_t sim_port = PORT;
	char* ethernetIfcID = "lo";

	if (argc > 1) {
		ethernetIfcID = argv[1];

		printf("Using interface: %s\n", ethernetIfcID);
	}

	if(argc > 2 )
	{
		port = atoi(argv[2]);
	}

	if(argc > 3 )
	{
		iedModel_local = ConfigFileParser_createModelFromConfigFileEx(argv[3]);
		iedExtendedModel_local = ConfigFileParser_createModelFromConfigFileEx_inputs(argv[4],iedModel_local);

		if(iedModel_local == NULL|| iedExtendedModel_local == NULL)
		{
			printf("Parsing dynamic config failed! Exit.\n");
			exit(-1);
		}
	}
	if(argc > 5 )
	{
		if(argv[5][0] == 'N')
			global_simulation_type = SIMULATION_TYPE_NONE;
		if(argv[5][0] == 'L')
			global_simulation_type = SIMULATION_TYPE_LOCAL;
		if(argv[5][0] == 'R')
			global_simulation_type = SIMULATION_TYPE_REMOTE;
	}
	if(argc > 6 )
	{
		sim_port = atoi(argv[6]);
	}
	else
	{
		if(iedModel_local == NULL|| iedExtendedModel_local == NULL)
		{
			printf("No valid model provided! Exit.\n");
			exit(-1);
		}
	}
	

	iedServer = IedServer_create(iedModel_local);

	GooseReceiver GSEreceiver = GooseReceiver_create();
	SVReceiver SMVreceiver = SVReceiver_create();

	/* set GOOSE interface for all GOOSE publishers (GCBs) */
	IedServer_setGooseInterfaceId(iedServer, ethernetIfcID);
	//goose subscriber
	GooseReceiver_setInterfaceId(GSEreceiver, ethernetIfcID);
	//smv subscriber
	SVReceiver_setInterfaceId(SMVreceiver, ethernetIfcID);


	//subscribe to datasets and local DA's based on iput/extRef, and generate one list with all inputValues
	LinkedList allInputValues = subscribeToGOOSEInputs(iedExtendedModel_local, GSEreceiver);
	LinkedList temp = allInputValues;
	temp = LinkedList_getLastElement(temp);
	temp->next = subscribeToSMVInputs(iedExtendedModel_local, SMVreceiver);
	temp = LinkedList_getLastElement(temp);
	temp->next = subscribeToLocalDAInputs(iedExtendedModel_local, iedModel_local,iedServer);

	//start subscribers
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
	IedServer_start(iedServer, port);

	if (!IedServer_isRunning(iedServer)) {
		printf("Starting server failed! Exit.\n");
		IedServer_destroy(iedServer);
		exit(-1);
	}
	
	//call initializers for sampled value control blocks and start publishing
	attachSMV(iedServer, iedModel_local, ethernetIfcID, allInputValues);

	//call all initializers for logical nodes in the model
	attachLogicalNodes(iedServer, iedExtendedModel_local, allInputValues);

	/* Start GOOSE publishing */
	IedServer_enableGoosePublishing(iedServer);

	if(global_simulation_type == SIMULATION_TYPE_REMOTE) {
		simulation_thread(iedModel_local, iedExtendedModel_local, sim_port);
	}
	else {
		running = 1;
		signal(SIGINT, sigint_handler);
		while (running) {
			Thread_sleep(1000);
		}
	}


	/* stop MMS server - close TCP server socket and all client sockets */
	IedServer_stop(iedServer);

	/* Cleanup - free all resources */
	IedServer_destroy(iedServer);

	GooseReceiver_stop(GSEreceiver);

    GooseReceiver_destroy(GSEreceiver);

	SVReceiver_stop(SMVreceiver);
     /* Cleanup and free resources */
    SVReceiver_destroy(SMVreceiver);
} /* main() */
