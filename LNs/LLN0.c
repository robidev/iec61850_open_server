#include "open_server.h"
#include <libiec61850/iec61850_server.h>
#include "iec61850_model_extensions.h"
#include "LLN0.h"


bool LLN0_GetLoc (LLN0 *inst)
{
    return inst->LLN0_Loc;
}

void LLN0_SetLoc (LLN0 *inst, bool Local)
{
    if(Local)
        printf("LLN0.Loc changed to Local (true)\n");
    else
        printf("LLN0.Loc changed to Remote (false)\n");
    uint64_t timestamp = Hal_getTimeInMs();
    IedServer_updateBooleanAttributeValue(inst->server, inst->Loc_stVal, Local);
    IedServer_updateUTCTimeAttributeValue(inst->server, inst->Loc_t, timestamp);
    InputValueHandleExtensionCallbacks(inst->Loc_stVal_callback); // update the associated callbacks with this Data Element
    inst->LLN0_Loc = Local;
}

//  LLN0.Health.stVal (Ok=1, Warn=2, Alarm=3)
//      .Mod (opt for all other LN's)
//      .Beh (every LN mandatory)
void *LLN0_init(IedServer server, LogicalNode* ln, Input *input, LinkedList allInputValues)
{
    LLN0 *inst = (LLN0 *)malloc(sizeof(LLN0)); // create new instance with MALLOC
    inst->server = server;
    inst->Loc_stVal = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Loc.stVal");
    inst->Loc_t = (DataAttribute *)ModelNode_getChild((ModelNode *)ln, "Loc.t");       // the node to operate on when a operate is triggered
    inst->Loc_stVal_callback = _findAttributeValueEx(inst->Loc_stVal, allInputValues); // find node that this element was subscribed to, so that it will be called during an update
    inst->LLN0_Loc = false;

    return inst;
}
