#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "TCTR.h"

#include "iec61850_server.h"
#include "hal_thread.h"
#include <sys/socket.h> 

typedef void (*simulationFunction) (int sd, char * buffer, void* param);

typedef struct sTCTR
{
  simulationFunction call_simulation; //as long as we place the function on top, it can be recast into a generic struct(TODO: make this nicer)
  void *da;
  IedServer server;
  void * da_callback;
} TCTR;

void TCTR_updateValue(int sd, char * buffer, void* param)
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

void *TCTR_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues )
{
  TCTR* inst = (TCTR *) malloc(sizeof(TCTR));//create new instance with MALLOC
  inst->server = server;
  inst->da = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Amp.instMag.i");//the node to operate on
  inst->da_callback = _findAttributeValueEx(inst->da, allInputValues);

  //register callback for input
  inst->call_simulation = TCTR_updateValue;
  return inst;
}