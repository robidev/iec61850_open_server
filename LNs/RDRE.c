#include <libiec61850/hal_thread.h>
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include <time.h>
#include <math.h>
#include "RDRE.h"
#include "RADR.h"
#include "RBDR.h"

#define TRIP_RECORD_DELAY_MS 100
#define COMTRADE_DAT_FILE_NAME "vmd-filestore/comtrade_data.dat"
#define COMTRADE_CFG_FILE_NAME "vmd-filestore/comtrade_data.cfg"

typedef struct sRDRE {
  IedServer server;
  LinkedList analog;
  LinkedList digital;
  int recording;
} RDRE;

typedef struct sComtradeTimestamp
{
    time_t seconds;
    long milliseconds;
    char timestring[60];
} ComtradeTimestamp;


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


void timer_callback(RDRE *inst);

void RDRE_callback_trip(InputEntry *extRef)
{
  RDRE *inst = extRef->callBackParam;
  if(inst->recording == 0)
  {
    inst->recording = 1;
    Thread thread = Thread_create((ThreadExecutionFunction)timer_callback, inst, true);
    Thread_start(thread);
  }
}

void timer_callback(RDRE *inst)
{
  ComtradeTimestamp triptime;
  struct timespec curtime;
  // Get current time
  clock_gettime(CLOCK_REALTIME, &curtime);
  triptime.seconds      = curtime.tv_sec;
  triptime.milliseconds = round(curtime.tv_nsec/1.0e6);
  getTimestamp(&triptime); //get string

  Thread_sleep(TRIP_RECORD_DELAY_MS);//record a little after the trip

  ComtradeTimestamp starttime;
  int delta = ((RADR_MAX_SAMPLES/4000)*1000)-TRIP_RECORD_DELAY_MS;
  starttime.seconds      = triptime.seconds - (delta / 1000);
  long millis = triptime.milliseconds - (delta % 1000);
  if(millis < 0)
  {
    starttime.seconds -=1;
    millis += 1000;
  }
  starttime.milliseconds = millis;
  getTimestamp(&starttime); //get string

  uint32_t time = 0;//
  FILE *fp, *cfgfp;

  if(inst->recording == 2)
  {
    return;
  }
  inst->recording = 2;

  fp = fopen(COMTRADE_DAT_FILE_NAME, "w+");
  if(fp == NULL)
  {
    printf("RDRE: ERROR could not open %s", COMTRADE_DAT_FILE_NAME);
    inst->recording = 0;
    return;
  }
  for(int i = 0; i < RADR_MAX_SAMPLES; i++)
  {
    fprintf(fp,"%d,%d",i,time);
    LinkedList temp = inst->analog;
    while(temp != NULL)
    {
      LogicalNodeClass *ln = LinkedList_getData(temp);
      if(ln != NULL)
      {
        RADR * radr = ln->instance;
        int32_t bufindex = (radr->bufferIndex +1) % RADR_MAX_SAMPLES; //start at the oldest sample
        fprintf(fp,",%d", radr->buffer[(bufindex + i) % RADR_MAX_SAMPLES]);
      }
      temp = LinkedList_getNext(temp);
    }

    temp = inst->digital;
    while(temp != NULL)
    {
      LogicalNodeClass *ln = LinkedList_getData(temp);
      if(ln != NULL)
      {
        RBDR * rbdr = ln->instance;
        int32_t bufindex = (rbdr->bufferIndex +1) % RBDR_MAX_SAMPLES; //start at the oldest sample
        fprintf(fp,",%d", rbdr->buffer[(bufindex + i) % RBDR_MAX_SAMPLES]);
      }
      temp = LinkedList_getNext(temp);
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
  fprintf(cfgfp,"4000,%u \r\n",RADR_MAX_SAMPLES);
  fprintf(cfgfp,"%s\r\n",starttime.timestring);
  fprintf(cfgfp,"%s\r\n",triptime.timestring);
  fprintf(cfgfp,"ASCII\r\n"\
"1\r\n"\
"+1h,+1h\r\n"\
"B,3");
  fclose(cfgfp);
  inst->recording = 0;
}


void * RDRE_init(IedServer server, LogicalNode *ln, IedModel * model , IedModel_extensions * model_ex,Input *input, LinkedList allInputValues)
{
  RDRE *inst = (RDRE *)malloc(sizeof(RDRE)); // create new instance with MALLOC
  inst->server = server;
  inst->analog = LinkedList_create();
  inst->digital = LinkedList_create();
  inst->recording = 0;

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
          }
      }
      // receive status of associated XCBR
      if (strcmp(extRef->intAddr, "RDRE_digital") == 0)
      {
          //this should work if the input ref is the logical node instance instead of a DA, is this allowed?
          LogicalNodeClass *ln = getLNClass(model, model_ex, extRef->Ref);
          if (ln != NULL){
            LinkedList_add(inst->digital, ln);
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
  return inst;
}