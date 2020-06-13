#include "iec61850_model_extensions.h"
#include "iec61850_server.h"
#include "inputs_api.h"
#include "hal_thread.h"
#include "simulation_config.h"
#include <sys/socket.h> 
#include "XCBR.h"


//process simulator
void XCBR_simulate_switch(Input* input);
typedef void (*simulationFunction) (int sd, char * buffer, void* param);

typedef struct sXCBR
{
  simulationFunction call_simulation; //as long as we place the function on top, it can be recast into a generic struct(TODO: make this nicer)
  IedServer server;
  DataAttribute* Pos_stVal;
  bool conducting;
} XCBR;

void XCBR_updateValue(int sd, char * buffer, void* param)
{
  //printf("XCBR buf= %s\n",buffer);

  XCBR* inst = (XCBR*) param;
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
void XCBR_open(XCBR * inst)
{
  inst->conducting = false;
}

//close the circuit breaker switch(i.e. make it conducting)
void XCBR_close(XCBR * inst)
{
  inst->conducting = true;
}

//callback for open/close signal from GOOSE-> will trigger process simulator threat
void XCBR_callback(InputEntry* extRef )
{
  //only one type of extref is expected: ctlVal
  printf("XCBR: input signal received\n");
  bool state = MmsValue_getBoolean(extRef->value);
  if(state == true)
    XCBR_open(extRef->callBackParam);
  else
    XCBR_close(extRef->callBackParam);
}

//initialise XCBR instance for process simulation, and publish/subscription of GOOSE
void *XCBR_init(IedServer server, LogicalNode* ln, Input* input)
{
  XCBR* inst = (XCBR *) malloc(sizeof(XCBR));//create new instance with MALLOC
  inst->server = server;
  inst->Pos_stVal = (DataAttribute*) ModelNode_getChild((ModelNode*) ln, "Pos.stVal");
  inst->conducting = true;
  inst->call_simulation = XCBR_updateValue;


  if(input != NULL)
  {
    InputEntry* extref = input->extRefs;
    while(extref != NULL)
    {
      if(strcmp(extref->intAddr,"Tr") == 0)
      {
        //register callbacks for GOOSE-subscription
        extref->callBack = (callBackFunction) XCBR_callback;
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
  Thread thread = Thread_create((ThreadExecutionFunction)XCBR_simulate_switch, input, true);
  Thread_start(thread);

  return inst;
}

void XCBR_change_switch(XCBR * inst, Dbpos value)
{
  IedServer_updateDbposValue(inst->server,inst->Pos_stVal,value);
}

//threath for process-simulation: open/close switch
void XCBR_simulate_switch(Input* input)
{
  int state = 3;//default state is closed
  int step = 0;

  XCBR* inst = input->extRefs->callBackParam;//take the initial callback, as they all contain the same object instance

  inst->conducting = true;//initial state
  XCBR_change_switch(inst,DBPOS_ON);//initial state
  while(1)
  {
    switch(state)
    {
      case 0:// opening
      {
        printf("XCBR: opening, BANG!\n");
        XCBR_change_switch(inst,DBPOS_INTERMEDIATE_STATE);

        Thread_sleep(20);
        XCBR_change_switch(inst,DBPOS_OFF);
        printf("XCBR: opened\n");
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
        printf("XCBR: closing\n");
        XCBR_change_switch(inst,DBPOS_INTERMEDIATE_STATE);

        Thread_sleep(2000);
        XCBR_change_switch(inst,DBPOS_ON);
        printf("XCBR: closed\n");
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
      Thread_sleep(10);
    }
          
  }
}