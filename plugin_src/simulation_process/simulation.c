#include <stdio.h>
#include "inputs_api.h"
#include "iec61850_model_extensions.h"
#include "iec61850_dynamic_model_extensions.h"
#include "iec61850_config_file_parser_extensions.h"
#include "LNParse.h"
#include <libiec61850/sv_publisher.h>

#include <libiec61850/iec61850_server.h>
#include <libiec61850/hal_thread.h> /* for Thread_sleep() */

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

#include <dirent.h>
#include <sys/stat.h>
#include <dlfcn.h>

#include <libiec61850/hal_socket.h>
#include "timestep_config.h"

#define PORT 65000
#define SOCKETS 65

static IedModel* model;
static IedModel_extensions* model_ex;
static uint16_t port;

typedef void (*processFunction) (int sd, char * buffer, void* param);
typedef struct sLNStruct 
{
	processFunction call_process;
} LNStruct;

//TODO: move to includes
typedef struct sXCBR
{
  IedServer server;
  DataAttribute *Pos_stVal;
  DataAttribute *Pos_t;
  void *Pos_stVal_callback;
  bool conducting;
} XCBR;
//TODO: move to includes
typedef struct sXSWI
{
  IedServer server;
  DataAttribute* Pos_stVal;
  DataAttribute* Pos_t;
  void * Pos_stVal_callback;
  bool conducting;
} XSWI;
//TODO: move to includes
typedef struct sTCTR
{
  void *da;
  IedServer server;
  void * da_callback;
} TCTR;
//TODO: move to includes
typedef struct sTVTR
{
  void *da;
  IedServer server;
  void * da_callback;
} TVTR;


int simulation_thread(void);
//TODO: move to includes
int open_server_running(void);


int init(IedModel* Model, IedModel_extensions* Model_ex)
{
	printf("simulation module initialising\n");
	port = PORT;
	model = Model;
	model_ex = Model_ex;
	if(IEC61850_server_timestep_type() == TIMESTEP_TYPE_LOCAL) {
		printf("ERROR: timestep should be remote for simulation\n");
		return 1;
	}
		
	//spawn simulation thread
	Thread thread = Thread_create((ThreadExecutionFunction)simulation_thread, NULL, true);
	Thread_start(thread);
	printf("simulation module initialised\n");
	return 0; // 0 means success
}

void sim_XCBR_updateValue(int sd, char *buffer, void *param)
{
  // printf("XCBR buf= %s\n",buffer);

  XCBR *inst = (XCBR *)param;
  if (inst->conducting)
  {
    if (send(sd, "10.0\n", 5, 0) != 5)
    {
      perror("send");
    }
  }
  else
  {
    if (send(sd, "-10.0\n", 6, 0) != 6)
    {
      perror("send");
    }
  }
}

void sim_XSWI_updateValue(int sd, char * buffer, void* param)
{
  //printf("XSWI buf= %s\n",buffer);
  XSWI* inst = (XSWI*) param;
  if(inst->conducting == true)
  {
    if( send(sd, "10.0\n", 5, 0) != 5 ) { 
      perror("send"); 
    } 
  }
  else
  {
    if( send(sd, "-10.0\n", 6, 0) != 6 ) { 
      perror("send"); 
    }   
  }
}

void sim_TCTR_updateValue(int sd, char * buffer, void* param)
{
  TCTR* inst = (TCTR *)param;
  // TODO update datamodel value
  char ref[130];
  int i = 0;

  int matchedItems = sscanf( buffer, "s %s %d", ref, &i );
  //printf("TCTR buf= %s, val=%i\n",buffer, i);

  IedServer_updateInt32AttributeValue(inst->server,inst->da,i);
  InputValueHandleExtensionCallbacks(inst->da_callback); //update the associated callbacks with this Data Element (e.g. MMXU)

  if( send(sd, "OK\n", 3, 0) != 3 ) { 
		perror("send"); 
	} 
}

void sim_TVTR_updateValue(int sd, char * buffer, void* param)
{
  TVTR* inst = (TVTR *)param;
  // TODO update datamodel value
  char ref[130];
  int i = 0;
  
  int matchedItems = sscanf( buffer, "s %s %d", ref, &i );
  //printf("TCTR buf= %s, val=%i\n",buffer, i);

  IedServer_updateInt32AttributeValue(inst->server,inst->da,i);
  InputValueHandleExtensionCallbacks(inst->da_callback); //update the associated callbacks with this Data Element

  if( send(sd, "OK\n", 3, 0) != 3 ) { 
		perror("send"); 
	} 
}

int simulation_thread() 
{ 
	printf("simulation thread started\n");
	int opt = 1; 
	int master_socket;
	int addrlen;
	int new_socket;
	int client_socket[SOCKETS];
	int max_clients = SOCKETS;
	void * LNi[SOCKETS];
	void * callbacks[SOCKETS];
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
		callbacks[i] = 0;
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
		
	//bind the socket to a port
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

	while(open_server_running()) 
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
					callbacks[i] = 0;
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
								//register simulation get/set calls
								if(strcmp(ln->lnClass,"XCBR") == 0)
								{
									callbacks[i] = sim_XCBR_updateValue;
								}
								else if(strcmp(ln->lnClass,"XSWI") == 0)
								{
									callbacks[i] = sim_XSWI_updateValue;
								}
								else if(strcmp(ln->lnClass,"TCTR") == 0)
								{
									callbacks[i] = sim_TCTR_updateValue;
								}
								else if(strcmp(ln->lnClass,"TVTR") == 0)
								{
									callbacks[i] = sim_TVTR_updateValue;
								}
								// set instance to socket connection index
								void * inst = ln->instance;
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
							if(LNi[i] != 0 && callbacks[i] != 0) {
								processFunction call_process = callbacks[i];
								call_process(sd, buffer, LNi[i]); // process_command
							}
							break;
						}
						case 'n'://case next=perform next simulation step
						{
							IEC61850_server_timestep_next_step();
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
	printf("simulation thread stopped\n");	
	return 0; 
} 

