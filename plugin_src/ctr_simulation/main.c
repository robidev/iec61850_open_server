#include <libiec61850/iec61850_server.h>


#include "iec61850_dynamic_model_extensions.h"
#include "iec61850_config_file_parser_extensions.h"
#include "LNParse.h"

#include <libiec61850/iec61850_model.h>
#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "timestep_config.h"

#include <libiec61850/hal_thread.h>
#include <math.h>

static IedModel* model;
static IedModel_extensions* model_ex;

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

//TODO: move to includes
typedef void (*SampleCallback)(int,void *);
typedef struct sSMVP {
    int svcbEnabled;
    SVPublisher_ASDU asdu;
    SVPublisher svPublisher;
    bool running;

    LinkedList dataSetValues;

    IedServer server;
    LinkedList  da_el;
    LinkedList  da_el_callback;
    SampleCallback getSample;
    void * getSampleParameter;
} SMVP;

void SMV_Thread(); 
void SMV_Callback(int samplecount,void * parameter);
//TODO: move to includes
int setSampleCallback(void* instance, void * callback, void * parameter);
int open_server_running(void);

int init(IedModel* Model, IedModel_extensions* Model_ex)
{
	printf("ctr_simulation module initialising\n");
	model = Model;
	model_ex = Model_ex;
		
    //load ctr/vtr refs from file, that should be updated
    //...
    //LogicalNodeClass* ln = getLNClass(model, model_ex, "CTR/VTR"); //based on LN in model, find LNinst(parent LN) in extension
	//spawn a simulation thread per ctr/vtr combination
	// Thread thread = Thread_create((ThreadExecutionFunction)SMV_Thread, NULL, true);
	// Thread_start(thread);
    //or register a callback for the smv to retrieve a sample in lockstep
    //SMVcB *smv = getSMVInstance(Model,Model_ex,"SMVREF");
    //setSampleCallback(smv->instance,SMV_Callback,ln->instance);

	printf("ctr_simulation module initialised\n");
	return 0; // 0 means success
}

void SMV_Callback(int sampleCount, void *parameter)
{ 
    printf("smv callback called");
    int measurements[8];

    int vol = (int) (6350.f * sqrt(2));//RMS to peak
    int amp = (int) (10.f * sqrt(2));//RMS to peak
    float phaseAngle = 0.f;

    /* update measurement values */
    int samplePoint = sampleCount % 80;

    double angleA = (2 * M_PI / 80) * samplePoint;
    double angleB = (2 * M_PI / 80) * samplePoint - ( 2 * M_PI / 3);
    double angleC = (2 * M_PI / 80) * samplePoint - ( 4 * M_PI / 3);

    measurements[0] = (amp * sin(angleA - phaseAngle)) * 1000;
    measurements[1] = (amp * sin(angleB - phaseAngle)) * 1000;
    measurements[2] = (amp * sin(angleC - phaseAngle)) * 1000;
    measurements[3] = measurements[0] + measurements[1] + measurements[2]; //should be 0

    measurements[4] = (vol * sin(angleA)) * 100;
    measurements[5] = (vol * sin(angleB)) * 100;
    measurements[6] = (vol * sin(angleC)) * 100;
    measurements[7] = measurements[4] + measurements[5] + measurements[6]; //should be 0

    //for all refs
    //IedServer_updateInt32AttributeValue(inst->server,inst->da,i);
    //InputValueHandleExtensionCallbacks(inst->da_callback); //update the associated callbacks with this Data Element (e.g. MMXU)


}

void SMV_Thread()
{
    int measurements[8];

    int vol = (int) (6350.f * sqrt(2));//RMS to peak
    int amp = (int) (10.f * sqrt(2));//RMS to peak
    float phaseAngle = 0.f;

    int sampleCount = 0;

    uint64_t nextCycleStart = Hal_getTimeInMs() + 1000;
    while (open_server_running()) 
    {
        /* update measurement values */
        int samplePoint = sampleCount % 80;

        double angleA = (2 * M_PI / 80) * samplePoint;
        double angleB = (2 * M_PI / 80) * samplePoint - ( 2 * M_PI / 3);
        double angleC = (2 * M_PI / 80) * samplePoint - ( 4 * M_PI / 3);

        measurements[0] = (amp * sin(angleA - phaseAngle)) * 1000;
        measurements[1] = (amp * sin(angleB - phaseAngle)) * 1000;
        measurements[2] = (amp * sin(angleC - phaseAngle)) * 1000;
        measurements[3] = measurements[0] + measurements[1] + measurements[2]; //should be 0

        measurements[4] = (vol * sin(angleA)) * 100;
        measurements[5] = (vol * sin(angleB)) * 100;
        measurements[6] = (vol * sin(angleC)) * 100;
        measurements[7] = measurements[4] + measurements[5] + measurements[6]; //should be 0

        //for all refs
        //IedServer_updateInt32AttributeValue(inst->server,inst->da,i);
        //InputValueHandleExtensionCallbacks(inst->da_callback); //update the associated callbacks with this Data Element (e.g. MMXU)


        sampleCount = ((sampleCount + 1) % 4000);

        if ((sampleCount % 400) == 0) {
            uint64_t timeval = Hal_getTimeInMs();

            while (timeval < nextCycleStart + 100) {
                Thread_sleep(1);

                timeval = Hal_getTimeInMs();
            }

            nextCycleStart = nextCycleStart + 100;
        }
    }
}
