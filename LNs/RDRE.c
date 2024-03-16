#include <libiec61850/hal_thread.h>
#include <time.h>
#include "open_server.h"
#include "iec61850_model_extensions.h"
#include "inputs_api.h"

#include "RDRE.h"
#include "RADR.h"
#include "RBDR.h"

#define TRIP_RECORD_DELAY_MS 1500
#define RDRE_MAX_SAMPLES (2*50*80)
#define RDRE_SAMPLE_RATE 4000
#define COMTRADE_DAT_FILE_NAME "vmd-filestore/comtrade_data.dat"
#define COMTRADE_CFG_FILE_NAME "vmd-filestore/comtrade_data.cfg"

typedef struct sRDRE {
  IedServer server;
  LinkedList analog;
  LinkedList digital;
  int32_t **analogbuffers;
  uint32_t analogbuffer_size;
  uint32_t **digitalbuffers;
  uint32_t digitalbuffer_size;
  uint32_t sample_index;
  int recording;
  struct timespec tripTime;
} RDRE;

typedef struct sComtradeTimestamp
{
    time_t seconds;
    long milliseconds;
    char timestring[60];
} ComtradeTimestamp;


void recorder_delay(RDRE *inst)
{
  Thread_sleep(TRIP_RECORD_DELAY_MS);//record a little after the trip
  if(inst->recording != 1)// we are already recording, or were just finished
  {
    return;
  }
  inst->recording = 2;
}

void RDRE_callback_trip(InputEntry *extRef)
{
  RDRE *inst = extRef->callBackParam;
  // Get trip time
  if(inst->recording == 0)
  {
    inst->recording = 1;
    clock_gettime(CLOCK_REALTIME, &inst->tripTime);
    Thread thread = Thread_create((ThreadExecutionFunction)recorder_delay, inst, true);
    Thread_start(thread);//start wait threat, before triggering recording
  }
}

void getTimestamp(ComtradeTimestamp * timestamp)
{
  struct tm *tmval = NULL;
  char timebuffer[32] = "";
  struct tm gmtval;
  if((tmval = gmtime_r(&timestamp->seconds, &gmtval)) != NULL)
  {
      strftime(timebuffer, sizeof timebuffer, "%Y-%m-%d,%H:%M:%S", &gmtval);// Build the first part of the time
      // Add the milliseconds part and build the time string
      snprintf(timestamp->timestring, sizeof timestamp->timestring, "%s.%03ld", timebuffer, timestamp->milliseconds); 
  }
}

void write_comtrade(RDRE *inst)
{
  ComtradeTimestamp triptime;
  triptime.seconds = inst->tripTime.tv_sec;
  triptime.milliseconds = inst->tripTime.tv_nsec / 1000000;
  getTimestamp(&triptime); //get string

  ComtradeTimestamp starttime;
  int delta_ms = ((RDRE_MAX_SAMPLES/RDRE_SAMPLE_RATE)*1000)-TRIP_RECORD_DELAY_MS;
  starttime.seconds      = triptime.seconds - (delta_ms / 1000);
  long millis = triptime.milliseconds - (delta_ms % 1000);
  if(millis < 0)
  {
    starttime.seconds -=1;
    millis += 1000;
  }
  starttime.milliseconds = millis;
  getTimestamp(&starttime); //get string

  uint32_t time = 0;//
  FILE *fp, *cfgfp;

  fp = fopen(COMTRADE_DAT_FILE_NAME, "w+");
  if(fp == NULL)
  {
    printf("RDRE: ERROR could not open %s", COMTRADE_DAT_FILE_NAME);
    inst->recording = 0;
    return;
  }
  int32_t bufindex = (inst->sample_index +1) % RDRE_MAX_SAMPLES; //start at the oldest sample
  for(int i = 0; i < RDRE_MAX_SAMPLES; i++)
  {
    fprintf(fp,"%d,%d",i,time);
    uint32_t radr_index = 0;
    while(radr_index < inst->analogbuffer_size)
    {
      fprintf(fp,",%d", inst->analogbuffers[radr_index][(bufindex + i) % RDRE_MAX_SAMPLES]);
      radr_index++;
    }

    uint32_t rbdr_index = 0;
    while(rbdr_index < inst->digitalbuffer_size)
    {
      fprintf(fp,",%d", inst->digitalbuffers[rbdr_index][(bufindex + i) % RDRE_MAX_SAMPLES]);
      rbdr_index++;
    }
    fprintf(fp,"\r\n");
    time += 250;
  }
  fclose(fp);
  
  
  // Comtrade CFG file format
  // title, recording device, revision year (we use 2013 version)
  // total streams, total analog, total digital
  // analog values: nr, title, phase, circuit, unit ,multiplier, offset, time-skew, minimal value, maximal value, primary,secondary,pors
  // digital values: nr, title, phase, circuit, initial value
  // line frequency
  // amount of sample rates {
  //    sample rate per second, total samples
  // }
  // first sample (12/01/2011,05:55:30.075011)
  // time of trip (12/01/2011,05:55:30.075011)
  // file format  
  // timestamp multiply factor
  // time code and local code
  // time quality code and leap second

  cfgfp = fopen(COMTRADE_CFG_FILE_NAME, "w+");  
  if(cfgfp == NULL)
  {
    printf("RDRE: ERROR could not open %s", COMTRADE_CFG_FILE_NAME);
    inst->recording = 0;
    return;
  }
  fprintf(cfgfp, "EXAMPLE STATION,IED1,2013\r\n"\
"2,1A,1D\r\n"\
"1,analog value,,,A, 1.0,0.0,0.0,-32768,32767,933,1,s\r\n"\
"1,binary value,,,1\r\n"\
"50\r\n"\
"1\r\n");
  fprintf(cfgfp,"%d,%d \r\n",RDRE_SAMPLE_RATE,RDRE_MAX_SAMPLES);
  fprintf(cfgfp,"%s\r\n",starttime.timestring);
  fprintf(cfgfp,"%s\r\n",triptime.timestring);
  fprintf(cfgfp,"ASCII\r\n"\
"1\r\n"\
"+1h,+1h\r\n"\
"B,3");
  fclose(cfgfp);
  inst->recording = 0;
}

void recorder_callback(RDRE *inst)
{
  struct timespec begintime;
  struct timespec curtime;
  uint64_t timediff_ns=0;
  uint32_t rdr_index=0;
  inst->sample_index=0;

  if(inst == NULL || inst->analogbuffers == NULL || inst->digitalbuffers == NULL)
  {
    printf("RDRE: ERROR could not allocate recording buffers");
    return;
  }

  while(open_server_running())
  {
    LinkedList temp = inst->analog;
    rdr_index=0;
    while(temp != NULL)
    {
      LogicalNodeClass *ln = LinkedList_getData(temp);
      if(ln != NULL)
      {
        RADR * radr = ln->instance;
        inst->analogbuffers[rdr_index][inst->sample_index] = radr->value;
        radr->value_read = 1;
        rdr_index++;
      }
      temp = LinkedList_getNext(temp);
    }
    temp = inst->digital;
    rdr_index=0;
    while(temp != NULL)
    {
      LogicalNodeClass *ln = LinkedList_getData(temp);
      if(ln != NULL)
      {
        RBDR * rbdr = ln->instance;
        inst->digitalbuffers[rdr_index][inst->sample_index]= rbdr->value;
        rdr_index++;
      }
      temp = LinkedList_getNext(temp);
    }
    if(inst->recording == 2)
    {
      write_comtrade(inst);
      inst->recording = 0;
    }
    inst->sample_index++;
    if(inst->sample_index >= RDRE_MAX_SAMPLES)
    {
      inst->sample_index = 0;
    }
    do
    {
      clock_gettime(CLOCK_MONOTONIC_RAW, &curtime);
      timediff_ns = ((curtime.tv_sec - begintime.tv_sec)*1000000000) + (curtime.tv_nsec - begintime.tv_nsec);
    } while(timediff_ns < 250000);//wait for 250 microseconds
    begintime = curtime;
  }
}

void * RDRE_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues)
{
  RDRE *inst = (RDRE *)malloc(sizeof(RDRE)); // create new instance with MALLOC
  inst->server = server;
  inst->analog = LinkedList_create();
  inst->digital = LinkedList_create();
  inst->recording = 0;
  inst->sample_index = 0;
  inst->analogbuffer_size = 0;
  inst->digitalbuffer_size = 0;

  //register callback for input
  //fault recorder, input is RADR/RBDR ln's current/voltage/digital, trigger is trip
  // when trip, collect few more samples, and then write comtrade file away with timestamp

  if (input != NULL)
  {
    InputEntry *extRef = input->extRefs;

    while (extRef != NULL)
    {
      // receive status of associated XCBR
      if (strcmp(extRef->intAddr, "RDRE_analog") == 0)
      {
          //this should work if the input ref is the logical node instance instead of a DA, is this allowed?
          //this could be called before radr extension is initialised based on the order in the SCL file!!!!!!!!!!!!!!!!!!!!!!!!
          //CFG should ignore ., or SCL file should be fixed, and parent should be retrieved here....
          LogicalNodeClass *ln = getLNClass(model, model_ex, extRef->Ref);
          if (ln != NULL){
            LinkedList_add(inst->analog, ln);
            inst->analogbuffer_size++;
          }
      }
      // receive status of associated XCBR
      if (strcmp(extRef->intAddr, "RDRE_digital") == 0)
      {
          //this should work if the input ref is the logical node instance instead of a DA, is this allowed?
          LogicalNodeClass *ln = getLNClass(model, model_ex, extRef->Ref);
          if (ln != NULL){
            LinkedList_add(inst->digital, ln);
            inst->digitalbuffer_size++;
          }
      }
      if (strcmp(extRef->intAddr, "RDRE_Trigger") == 0)
      {
        extRef->callBack = (callBackFunction)RDRE_callback_trip;
        extRef->callBackParam = inst;
      }
      extRef = extRef->sibling;
    }
  }


  inst->analogbuffers =  (int32_t **)malloc(sizeof(int32_t *) * inst->analogbuffer_size);
  int i = 0;
  for(i = 0; i < inst->analogbuffer_size; i++)
      inst->analogbuffers[i] = malloc(sizeof(int32_t) * RDRE_MAX_SAMPLES);

  inst->digitalbuffers =  (uint32_t **)malloc((sizeof(uint32_t *) * inst->digitalbuffer_size));
  for(i = 0; i < inst->digitalbuffer_size; i++)
      inst->digitalbuffers[i] = malloc(sizeof(uint32_t) * RDRE_MAX_SAMPLES);

  if(inst->analogbuffers == NULL || inst->digitalbuffers == NULL)
  {
    printf("RDRE: ERROR could not allocate recording buffers during init");
    return NULL;
  }
  Thread thread = Thread_create((ThreadExecutionFunction)recorder_callback, inst, true);
  Thread_start(thread);
  return inst;
}