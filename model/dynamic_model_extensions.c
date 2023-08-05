/*
 *  dynamic_model_extensions.c
 *
 */

#include "iec61850_model_extensions.h"
#include "iec61850_dynamic_model_extensions.h"

#include <libiec61850/iec61850_server.h>
#include "libiec61850_platform_includes.h"
#include "stack_config.h"
#include "lib_memory.h"

IedModel_extensions *
IedModel_extensions_create()
{
    IedModel_extensions *self = (IedModel_extensions *)GLOBAL_CALLOC(1, sizeof(IedModel_extensions));

    self->inputs = NULL;

    self->subRefs = NULL;

    self->logicalNodes = NULL;

    return self;
}

/* DEPRECATED
static void
IedModel_addSVControlBlock(IedModel* self, SVControlBlock* vcb)
{
    if (self->svCBs == NULL)
        self->svCBs = vcb;
    else {
        SVControlBlock* lastSVcb = self->svCBs;

        while (lastSVcb->sibling != NULL)
            lastSVcb = lastSVcb->sibling;

        lastSVcb->sibling = vcb;
    }
}


void
LogicalNode_addSVControlBlock(LogicalNode* self, SVControlBlock* vcb)
{
    IedModel* model = (IedModel*) self->parent->parent;

    IedModel_addSVControlBlock(model, vcb);
}
*/

static void
IedModel_addInput(IedModel_extensions *self, Input *input)
{
    if (self->inputs == NULL)
        self->inputs = input;
    else
    {
        Input *lastinput = self->inputs;

        while (lastinput != NULL)
        {
            if (lastinput->sibling == NULL)
            {
                lastinput->sibling = input;
                break;
            }

            lastinput = lastinput->sibling;
        }
    }
}

static void
IedModel_addLogicalNodeClass(IedModel_extensions *self, LogicalNodeClass *lnClass)
{
    if (self->logicalNodes == NULL)
        self->logicalNodes = lnClass;
    else
    {
        LogicalNodeClass *lastlnClass = self->logicalNodes;

        while (lastlnClass != NULL)
        {
            if (lastlnClass->sibling == NULL)
            {
                lastlnClass->sibling = lnClass;
                break;
            }

            lastlnClass = lastlnClass->sibling;
        }
    }
}

LogicalNodeClass *
LogicalNodeClass_create(LogicalNode *parent, IedModel_extensions *model, char *lnClass)
{
    LogicalNodeClass *self = (LogicalNodeClass *)GLOBAL_MALLOC(sizeof(LogicalNodeClass));

    self->parent = parent;

    if (lnClass != NULL)
        self->lnClass = StringUtils_copyString(lnClass);

    self->instance = NULL;
    self->sibling = NULL;

    IedModel_addLogicalNodeClass(model, self);

    return self;
}

Input *
Input_create(LogicalNode *parent, IedModel_extensions *model)
{
    Input *self = (Input *)GLOBAL_MALLOC(sizeof(Input));

    self->parent = parent;
    self->elementCount = 0;
    self->sibling = NULL;
    self->extRefs = NULL;

    IedModel_addInput(model, self);

    return self;
}

int Input_getSize(Input *self)
{
    return self->elementCount;
}

InputEntry *
Input_getFirstEntry(Input *self)
{
    return self->extRefs;
}

InputEntry *
InputEntry_getNext(InputEntry *self)
{
    return self->sibling;
}

static void
Input_addEntry(Input *self, InputEntry *newEntry)
{
    self->elementCount++;

    if (self->extRefs == NULL)
        self->extRefs = newEntry;
    else
    {
        InputEntry *lastEntry = self->extRefs;

        while (lastEntry != NULL)
        {

            if (lastEntry->sibling == NULL)
            {
                lastEntry->sibling = newEntry;
                break;
            }

            lastEntry = lastEntry->sibling;
        }
    }
}

InputEntry *
InputEntry_create(Input *input, const char *desc, const char *Ref, const char *intAddr, const char *serviceType, const char *srcRef)
{
    InputEntry *self = (InputEntry *)GLOBAL_MALLOC(sizeof(InputEntry));

    if (desc != NULL)
    {
        self->desc = StringUtils_copyString(desc);
    }

    if (Ref != NULL)
    {
        self->Ref = StringUtils_copyString(Ref);
    }

    if (intAddr != NULL)
    {
        self->intAddr = StringUtils_copyString(intAddr);
    }

    if (serviceType != NULL)
    {
        self->serviceType = StringUtils_copyString(serviceType);
    }

    if (srcRef != NULL)
    {
        self->srcRef = StringUtils_copyString(srcRef);
    }

    self->value = NULL;

    self->callBackParam = NULL;
    self->callBack = NULL;

    self->sibling = NULL;

    Input_addEntry(input, self);

    return self;
}

static void
Subscriber_addEntry(IedModel_extensions *self, SubscriberEntry *newEntry)
{
    if (self->subRefs == NULL)
        self->subRefs = newEntry;
    else
    {
        SubscriberEntry *lastEntry = self->subRefs;

        while (lastEntry != NULL)
        {

            if (lastEntry->sibling == NULL)
            {
                lastEntry->sibling = newEntry;
                break;
            }

            lastEntry = lastEntry->sibling;
        }
    }
}

SubscriberEntry *
SubscriberEntry_create(IedModel_extensions *model, const char *variableName, const char *Dataset, uint16_t APPID, const char *cbRef, const char *ID, uint8_t *ethAddr)
{
    SubscriberEntry *self = (SubscriberEntry *)GLOBAL_MALLOC(sizeof(SubscriberEntry));
    if (self == NULL)
        return NULL;

    if (variableName != NULL)
        self->variableName = StringUtils_copyString(variableName);

    if (Dataset != NULL)
        self->Dataset = StringUtils_copyString(Dataset);

    self->APPID = APPID;

    if (cbRef != NULL)
        self->cbRef = StringUtils_copyString(cbRef);

    if (ID != NULL)
        self->ID = StringUtils_copyString(ID);

    if (ethAddr != NULL)
        memcpy(self->ethAddr, ethAddr, 6);

    self->sibling = NULL;

    Subscriber_addEntry(model, self);

    return self;
}

void IedModel_destroy_inputs(IedModel_extensions *model)
{
    /* delete all model nodes and dynamically created strings */

    /*  delete all inputs */

    Input *input = model->inputs;

    while (input != NULL)
    {
        Input *nextinput = input->sibling;

        InputEntry *dse = input->extRefs;

        while (dse != NULL)
        {
            InputEntry *nextDse = dse->sibling;

            // TODO clean extref mem

            GLOBAL_FREEMEM(dse);

            dse = nextDse;
        }

        GLOBAL_FREEMEM(input);

        input = nextinput;
    }

    /*  delete all SubscriberEntry */

    SubscriberEntry *subref = model->subRefs;

    while (subref != NULL)
    {
        SubscriberEntry *nextsubref = subref->sibling;
        // TODO clean subRefs mem
        GLOBAL_FREEMEM(subref);
        subref = nextsubref;
    }

    GLOBAL_FREEMEM(model);
}
