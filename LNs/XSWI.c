#include "iec61850_model_extensions.h"
#include <libiec61850/iec61850_server.h>
#include "inputs_api.h"
#include <libiec61850/hal_thread.h>
#include "XSWI.h"
#include "simulation_config.h"
#include <sys/socket.h> 

//process simulator
void XSWI_simulate_switch(Input* input);
typedef void (*simulationFunction) (int sd, char * buffer, void* param);

typedef struct sXSWI
{
  simulationFunction call_simulation; //as long as we place the function on top, it can be recast into a generic struct(TODO: make this nicer)
  IedServer server;
  DataAttribute* Pos_stVal;
  DataAttribute* Pos_t;
  void * Pos_stVal_callback;
  bool conducting;
} XSWI;

void XSWI_updateValue(int sd, char * buffer, void* param)
{
  //printf("XSWI buf= %s\n",buffer);
  XSWI* inst = (XSWI*) param;
  if(inst->conducting)
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

//open the circuit breaker(i.e. make it isolating)
void XSWI_open(XSWI * inst)
{
  inst->conducting = false;
}

//close the circuit breaker switch(i.e. make it conducting)
void XSWI_close(XSWI * inst)
{
  inst->conducting = true;
}

//callback for open/close signal from GOOSE-> will trigger process simulator threat
void XSWI_callback(InputEntry* extRef )
{
  //only one type of extref is expected: ctlVal
  bool state = MmsValue_getBoolean(extRef->value);
  if(state == true)
    XSWI_open(extRef->callBackParam);
  else
    XSWI_close(extRef->callBackParam);
}

//initialise XSWI instance for process simulation, and publish/subscription of GOOSE
void *XSWI_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues)
{
  XSWI* inst = (XSWI *) malloc(sizeof(XSWI));//create new instance with MALLOC
  inst->server = server;
  inst->Pos_stVal = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Pos.stVal");
  inst->Pos_t = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Pos.t");//the node to operate on when a operate is triggered
  inst->Pos_stVal_callback = _findAttributeValueEx(inst->Pos_stVal, allInputValues);//find node that this element was subscribed to, so that it will be called during an update

  inst->conducting = true;
  inst->call_simulation = XSWI_updateValue;


  if(input != NULL)
  {
    InputEntry* extref = input->extRefs;
    while(extref != NULL)
    {
      if(strcmp(extref->intAddr,"Tr") == 0)
      {
        //register callbacks for GOOSE-subscription
        extref->callBack = (callBackFunction) XSWI_callback;
        extref->callBackParam = inst;//pass instance in param
      }
      extref = extref->sibling;
    }
  }
  else
  {
    printf("ERROR: no input element defined");
    return 0;
  }
  
  //start simulation threat
  Thread thread = Thread_create((ThreadExecutionFunction)XSWI_simulate_switch, input, true);
  Thread_start(thread);
  
  return inst;
}

void XSWI_change_switch(XSWI * inst, Dbpos value)
{
  uint64_t timestamp = Hal_getTimeInMs();
  IedServer_updateDbposValue(inst->server,inst->Pos_stVal,value);
  IedServer_updateUTCTimeAttributeValue(inst->server, inst->Pos_t, timestamp);
  InputValueHandleExtensionCallbacks(inst->Pos_stVal_callback); //update the associated callbacks with this Data Element
}

//threath for process-simulation: open/close switch
void XSWI_simulate_switch(Input* input)
{
  int state = 3;//default state is closed
  int step = 0;
  XSWI* inst = input->extRefs->callBackParam;//take the initial callback, as they all contain the same object instance

  inst->conducting = true;//initial state
  XSWI_change_switch(inst,DBPOS_ON);//initial state

  while(1)
  {
    switch(state)
    {
      case 0:// opening
      {
        printf("XSWI: opening, ZZZZT\n");
        XSWI_change_switch(inst,DBPOS_INTERMEDIATE_STATE);

        Thread_sleep(2000);
        XSWI_change_switch(inst,DBPOS_OFF);
        printf("XSWI: opened\n");
        state = 1;
        break;
      }

      case 1: // opened
      {
        if(inst->conducting == true)//switch is closed
          state = 2;
        break;
      }
      

      case 2: // closing
      {
        printf("XSWI: closing\n");
        XSWI_change_switch(inst,DBPOS_INTERMEDIATE_STATE);

        Thread_sleep(2000);
        printf("XSWI: closed\n");
        XSWI_change_switch(inst,DBPOS_ON);
        state = 3;
        break;
      }

      case 3: // closed
      {
        if(inst->conducting == false)
          state = 0;
        break;
      }
    }
    if(IEC61850_server_simulation_type() == SIMULATION_TYPE_REMOTE)
    {
        IEC61850_server_simulation_sync(step++);
    }
    else
    {
      Thread_sleep(100);
    }   
  }
}
