#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "TVTR.h"

#include "iec61850_server.h"
#include "hal_thread.h"
#include <sys/socket.h> 

typedef void (*simulationFunction) (int sd, char * buffer, void* param);

typedef struct sTVTR
{
  simulationFunction call_simulation; //as long as we place the function on top, it can be recast into a generic struct(TODO: make this nicer)
  void *da;
  IedServer server;
  void * da_callback;
} TVTR;

void TVTR_updateValue(int sd, char * buffer, void* param)
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

void *TVTR_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues )
{
  TVTR* inst = (TVTR *) malloc(sizeof(TVTR));//create new instance with MALLOC
  inst->server = server;
  inst->da = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Vol.instMag.i");//the node to operate on
  inst->da_callback = _findAttributeValueEx(inst->da, allInputValues);

  //register callback for input
  inst->call_simulation = TVTR_updateValue;
  return inst;
}