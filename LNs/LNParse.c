#include "iec61850_model_extensions.h"
#include "inputs_api.h"
#include "LNParse.h"
#include "SMVPublisher.h"
#include "XSWI.h"
#include "XCBR.h"
#include "RADR.h"
#include "PTRC.h"
#include "PTOC.h"
#include "MMXU.h"
#include "CSWI.h"
#include "CILO.h"
#include "LLN0.h"
#include "TCTR.h"
#include "TVTR.h"

void attachLogicalNodes(IedServer server, IedModel_extensions* model, LinkedList allInputValues)
{
  //iterate over struct that attaches model-instances to LogicalNode Classes
  LogicalNodeClass* lnClass = model->logicalNodes;
  while(lnClass != NULL)
  { // call init, to attach input-nodes of this instance to callback-items. store instance in lnClass
    Input* input = getInput( model, lnClass->parent); 

    if(strcmp(lnClass->lnClass,"LLN0") == 0)
    {
      printf("Found mandatory Class LLN0\n");
      LLN0_init(server, lnClass->parent);
    }
    else if(strcmp(lnClass->lnClass,"LPHD") == 0)
    {
      printf("Found mandatory Class LPHD\n");
    }
    //simulated
    else if(strcmp(lnClass->lnClass,"XSWI") == 0)
    {
      lnClass->instance = XSWI_init(server, lnClass->parent, input); 
    }
    else if(strcmp(lnClass->lnClass,"XCBR") == 0)
    {
      lnClass->instance = XCBR_init(server, lnClass->parent, input);
    }
    else if(strcmp(lnClass->lnClass,"TCTR") == 0)
    {
      lnClass->instance = TCTR_init(server, lnClass->parent, input, allInputValues);
    }
    else if(strcmp(lnClass->lnClass,"TVTR") == 0)
    {
      lnClass->instance = TVTR_init(server, lnClass->parent, input, allInputValues);
    }
    //basic functional
    else if(strcmp(lnClass->lnClass,"PTRC") == 0)
    {
      PTRC_init(server, lnClass->parent, input, allInputValues);
    }
    else if(strcmp(lnClass->lnClass,"PTOC") == 0)
    {
      PTOC_init(server, lnClass->parent, input, allInputValues);
    }
    else if(strcmp(lnClass->lnClass,"MMXU") == 0)
    {
      MMXU_init(server, lnClass->parent, input, allInputValues);
    }
    else if(strcmp(lnClass->lnClass,"CSWI") == 0)
    {
      CSWI_init(server, lnClass->parent, input, allInputValues);
    }
    //stubs
    else if(strcmp(lnClass->lnClass,"RADR") == 0)
    {
      RADR_init(input);
    }
    else if(strcmp(lnClass->lnClass,"CILO") == 0)
    {
      CILO_init(input);
    }
    else
    {
      printf("ERROR: Class %s not supported\n", lnClass->lnClass);
    }
    lnClass = lnClass->sibling;
  }
  
}

void attachSMV(IedServer server, IedModel* model, char* ethernetIfcID, LinkedList allInputValues) //allInputValues is needed for callbacks when a local value is updated
{
  SVControlBlock* svCBs = model->svCBs;
  while(svCBs != NULL)
  {
    	//smv publisher
	  SVPublisher SMVPublisher = SVPublisher_create((CommParameters *)svCBs->dstAddress, ethernetIfcID);
    SMVP_init(SMVPublisher, svCBs, server, allInputValues);

    svCBs = svCBs->sibling;
  }
}

LogicalNodeClass* getLNClass(IedModel* model, IedModel_extensions* model_ex, const char * objectReference)
{
  LogicalNode* ln = (LogicalNode*)IedModel_getModelNodeByObjectReference(model, objectReference);
  if(ln == NULL){
    printf("ERROR: could not find logical node object ref: %s", objectReference);
    return NULL;
  }
  
  LogicalNodeClass* lnClass = model_ex->logicalNodes;
  while(lnClass != NULL)
  {
    if(lnClass->parent == ln)
    {
      return lnClass;
    }
    lnClass = lnClass->sibling;
  }
  return NULL;
}