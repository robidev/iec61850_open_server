#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "LNParse.h"
#include "SMVPublisher.h"
#include "XSWI.h"
#include "XCBR.h"
#include "RADR.h"
#include "RBDR.h"
#include "RDRE.h"
#include "RREC.h"
#include "PTRC.h"
#include "PTOC.h"
#include "PIOC.h"
#include "PDIS.h"
#include "PDIF.h"
#include "MMXU.h"
#include "CSWI.h"
#include "CILO.h"
#include "LLN0.h"
#include "TCTR.h"
#include "TVTR.h"

void attachLogicalNodes(IedServer server, IedModel *model, IedModel_extensions *model_ex, LinkedList allInputValues)
{
  // iterate over struct that attaches model_ex-instances to LogicalNode Classes
  LogicalNodeClass *lnInstance = model_ex->logicalNodes;
  while (lnInstance != NULL)
  { // call init, to attach input-nodes of this instance to callback-items. store instance in lnInstance
    Input *input = getInput(model_ex, lnInstance->parent);
    
    if (strcmp(lnInstance->lnClass, "LLN0") == 0)
    {
      printf("Found mandatory Class LLN0\n");
      LLN0_init(server, lnInstance->parent);
    }
    else if (strcmp(lnInstance->lnClass, "LPHD") == 0)
    {
      printf("Found mandatory Class LPHD\n");
    }
    // simulated
    else if (strcmp(lnInstance->lnClass, "XSWI") == 0)
    {
      lnInstance->instance = XSWI_init(server, lnInstance->parent, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "XCBR") == 0)
    {
      lnInstance->instance = XCBR_init(server, lnInstance->parent, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "TCTR") == 0)
    {
      lnInstance->instance = TCTR_init(server, lnInstance->parent, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "TVTR") == 0)
    {
      lnInstance->instance = TVTR_init(server, lnInstance->parent, input, allInputValues);
    }
    // basic functional
    else if (strcmp(lnInstance->lnClass, "PTRC") == 0)
    {
      PTRC_init(server, lnInstance->parent, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "PIOC") == 0)
    {
      PIOC_init(server, lnInstance->parent, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "PTOC") == 0)
    {
      PTOC_init(server, lnInstance->parent, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "PDIS") == 0)
    {
      PDIS_init(server, lnInstance->parent, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "PDIF") == 0)
    {
      PDIF_init(server, lnInstance->parent, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "MMXU") == 0)
    {
      MMXU_init(server, lnInstance->parent, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "CSWI") == 0)
    {
      CSWI_init(server, lnInstance->parent, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "CILO") == 0)
    {
      CILO_init(server, lnInstance->parent, input, allInputValues);
    }
    // stubs
    else if (strcmp(lnInstance->lnClass, "RADR") == 0)
    {
      RADR_init(server, lnInstance->parent, model, model_ex, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "RBDR") == 0)
    {
      RBDR_init(server, lnInstance->parent, model, model_ex, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "RDRE") == 0)
    {
      RDRE_init(server, lnInstance->parent, model, model_ex, input, allInputValues);
    }
    else if (strcmp(lnInstance->lnClass, "RREC") == 0)
    {
      RREC_init(server, lnInstance->parent, model, model_ex, input, allInputValues);
    }
    else
    {
      printf("ERROR: Class %s not supported\n", lnInstance->lnClass);
    }
    lnInstance = lnInstance->sibling;
  }
}

SMVcB *attachSMV(IedServer server, IedModel *model, LinkedList allInputValues, char *ethernetIfcID) // allInputValues is needed for callbacks when a local value is updated
{
  SMVcB *head = NULL;
  SMVcB *last = NULL;

  SVControlBlock *svCBs = model->svCBs;
  while (svCBs != NULL)
  {
    // smv publisher
    SVPublisher SMVPublisher = SVPublisher_create((CommParameters *)svCBs->dstAddress, ethernetIfcID);
    void *inst = SMVP_init(SMVPublisher, svCBs, server, allInputValues);
    if (inst != NULL)
    {
      SMVcB *ref = (SMVcB *)malloc(sizeof(SMVcB));
      ref->instance = inst;
      ref->svCBs = svCBs;
      ref->sibling = NULL;
      if (head == NULL)
      {
        head = ref;
        last = ref;
      }
      else
      {
        last->sibling = ref;
        last = ref;
      }
    }
    svCBs = svCBs->sibling;
  }
  return head;
}

LogicalNodeClass *getLNClass(IedModel *model, IedModel_extensions *model_ex, const char *objectReference)
{
  LogicalNode *ln = (LogicalNode *)IedModel_getModelNodeByObjectReference(model, objectReference);
  if (ln == NULL)
  {
    printf("ERROR: could not find logical node object ref: %s\n", objectReference);
    return NULL;
  }

  LogicalNodeClass *lnClass = model_ex->logicalNodes;
  while (lnClass != NULL)
  {
    if (lnClass->parent == ln)
    {
      return lnClass;
    }
    lnClass = lnClass->sibling;
  }
  return NULL;
}

SMVcB *getSMVInstance(IedModel *model, SMVcB *SMVControlInstances, const char *objectReference)
{
  SVControlBlock *svCBs = model->svCBs;
  while (svCBs != NULL)
  {
    if (strcmp(svCBs->name, objectReference) == 0)
    {
      SMVcB *entry = SMVControlInstances;
      while (entry)
      {
        if (entry->svCBs == svCBs)
        {
          return entry;
        }
        entry = entry->sibling;
      }
      return NULL;
    }
    svCBs = svCBs->sibling;
  }
  return NULL;
}