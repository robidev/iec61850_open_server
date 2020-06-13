/*
 *  inputs.c
 *
 *  Copyright 2013-2018 Michael Zillgith
 *
 *  This file is part of libIEC61850.
 *
 *  libIEC61850 is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  libIEC61850 is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with libIEC61850.  If not, see <http://www.gnu.org/licenses/>.
 *
 *  See COPYING file for the complete license text.
 */

#include "iec61850_server.h"
#include "libiec61850_platform_includes.h"
#include "inputs_api.h"
#include "goose_subscriber.h"


int strcmp_p(const char* str1, const char* str2);

InputValue* create_InputValue(int index, DataAttribute* da, Input* input, InputEntry* extRef);

void subscriber_callback_inputs_GOOSE(GooseSubscriber subscriber, void* parameter);
void subscriber_callback_inputs_SMV(SVSubscriber subscriber, void* parameter, SVSubscriber_ASDU asdu);


int strcmp_p(const char* str1, const char* str2)
{
  if(str1 == NULL || str2 == NULL)
    return -1;

  int s1 = strlen(str1);
  int s2 = strlen(str2);
  if(s1 == s2 && s1 != 0 && s1 < 140)
  {
      return strcmp(str1, str2);
  }
  return -1;
}

InputValue* create_InputValue(int index, DataAttribute* da, Input* input, InputEntry* extRef)
{
  InputValue* self = (InputValue *) GLOBAL_MALLOC(sizeof(struct sInputValue));
  if(self == NULL)
    return NULL;

  self->input = input;
  self->extRef = extRef;

  self->DA = da;
  self->index = index;

  self->sibling = NULL;
  return self;
}


//order of elements for sampled values matter, they should appear grouped per dataset, and ordered per index
//for goose, a new subscriber-instance is made for every extref
LinkedList subscribeToGOOSEInputs(IedModel_extensions* self, GooseReceiver GSEreceiver)
{
  LinkedList GOOSElist = LinkedList_create();
  SubscriberEntry* subscriberEntry = self->subRefs;

  InputValue* previous_inputValue = NULL;
  SubscriberEntry* previous_subscriberEntry = NULL;

  char* previous_datset = NULL;
  uint16_t previous_APPID = 0;
  uint8_t* previous_ethAddr[6] = {0,0,0,0,0,0};
  int dataSetIndex = 0;

  while(subscriberEntry != NULL)
  {
    //figure out index in dataset based on ordering and dataset-name
    //limitation: we assume that a dataset is not subscribed by 2 control-blocks
    if(strcmp_p(previous_datset, subscriberEntry->Dataset) == 0 \
        && previous_APPID == subscriberEntry->APPID \
        && memcmp(previous_ethAddr,subscriberEntry->ethAddr,6) == 0)
      dataSetIndex++;
    else
    {
      dataSetIndex = 0;
      previous_datset = subscriberEntry->Dataset;
      previous_APPID = subscriberEntry->APPID;
      memcpy(previous_ethAddr,subscriberEntry->ethAddr,6);
    }

    //find a matching input, iterate over all of them (all inputs are grouped by logical node)
    Input* inputs = self->inputs;
    while(inputs != NULL)
    {
      InputEntry* extRef = inputs->extRefs; 
      while(extRef != NULL)//find all matching extref for this extRef
      {
        if(strcmp_p(subscriberEntry->variableName, extRef->Ref) == 0)//if extref and datasetname match, we subscribe to it!
        {
          InputValue * inputValue = create_InputValue(dataSetIndex, NULL, inputs, extRef);//match a dataset index to an extref, so we know how to decode a subscribed dataset

          if(strcmp_p(extRef->serviceType, "GOOSE") == 0 && GSEreceiver != NULL)
          {//if the extref is GOOSE subscribed, then create a subscriber
            if(previous_subscriberEntry == NULL)//always create an initial subscriber 
            {
              previous_subscriberEntry = subscriberEntry;
              previous_inputValue = NULL;
            }

            if(subscriberEntry->APPID != previous_subscriberEntry->APPID || strcmp_p(subscriberEntry->cbRef,previous_subscriberEntry->cbRef) != 0)//check if a new subscriber should be made, or added to an existing
            {//no match with the previous subscriber-entry, so search all existing inputs for a usable subscriber
              previous_inputValue = NULL;
            }

            //create a new subscriber, if its the first inputValue in the list
            if(previous_inputValue == NULL)
            {
              GooseSubscriber subscriber = GooseSubscriber_create(subscriberEntry->cbRef, NULL);
              GooseSubscriber_setAppId(subscriber, subscriberEntry->APPID);
              GooseSubscriber_setListener(subscriber, subscriber_callback_inputs_GOOSE, inputValue);
              GooseReceiver_addSubscriber(GSEreceiver, subscriber);

              previous_subscriberEntry = subscriberEntry; 
            }
            else//add entries to the current subscriber
            {
              previous_inputValue->sibling = inputValue;
            }
            LinkedList_add(GOOSElist, inputValue);

            previous_inputValue = inputValue;
          }
        }
        extRef = extRef->sibling;
      }
      inputs = inputs->sibling;
    }
    subscriberEntry = subscriberEntry->sibling;
  }
  return GOOSElist;
}

LinkedList subscribeToSMVInputs(IedModel_extensions* self, SVReceiver SMVreceiver)
{
  LinkedList SMVlist = LinkedList_create();
  SubscriberEntry* subscriberEntry = self->subRefs;

  InputValue* previous_inputValue = NULL;
  SubscriberEntry* previous_subscriberEntry = NULL;

  char * previous_datset = NULL;
  int dataSetIndex = 0;

  while(subscriberEntry != NULL)
  {
    //figure out index in dataset based on ordering and dataset-name
    //limitation: we assume that a dataset is not subscribed by 2 control-blocks
    if(strcmp_p(previous_datset, subscriberEntry->Dataset) == 0)
      dataSetIndex++;
    else
    {
      dataSetIndex = 0;
      previous_datset = subscriberEntry->Dataset;
    }

    //find a matching input, iterate over all of them (all inputs are grouped by logical node)
    Input* inputs = self->inputs;
    while(inputs != NULL)
    {
      InputEntry* extRef = inputs->extRefs; 
      while(extRef != NULL)//find all matching extref for this extRef
      {
        if(strcmp_p(subscriberEntry->variableName, extRef->Ref) == 0)//if extref and datasetname match, we subscribe to it!
        {
          InputValue * inputValue = create_InputValue(dataSetIndex, NULL, inputs, extRef);//match a dataset index to an extref, so we know how to decode a subscribed dataset

          if(strcmp_p(extRef->serviceType, "SMV") == 0 && SMVreceiver != NULL)
          {//if the extref is SMV, then create/add a subscriber
            if(previous_subscriberEntry == NULL)//always create an initial subscriber 
            {
              previous_subscriberEntry = subscriberEntry;
              previous_inputValue = NULL;
            }

            if(subscriberEntry->APPID != previous_subscriberEntry->APPID || memcmp(subscriberEntry->ethAddr,previous_subscriberEntry->ethAddr,6) != 0)//check if a new subscriber should be made, or added to an existing
            {
              previous_inputValue = NULL;
            }

            //create a new subscriber, if its the first inputValue in the list
            if(previous_inputValue == NULL)
            {
              char null_arr[6] = {0,0,0,0,0,0};
              SVSubscriber subscriber = SVSubscriber_create(subscriberEntry->ethAddr, subscriberEntry->APPID);
              SVSubscriber_setListener(subscriber, subscriber_callback_inputs_SMV, inputValue);
              SVReceiver_addSubscriber(SMVreceiver, subscriber);
              if(memcmp(subscriberEntry->ethAddr,null_arr,6) != 0)
              {
                SVReceiver_enableDestAddrCheck(SMVreceiver);
              }
              LinkedList_add(SMVlist,subscriberEntry);

              previous_subscriberEntry = subscriberEntry;            
            }
            else//add entries to the current subscriber
            {
              previous_inputValue->sibling = inputValue;
            }
            previous_inputValue = inputValue;
          }
        }
        extRef = extRef->sibling;
      }
      inputs = inputs->sibling;
    }
    subscriberEntry = subscriberEntry->sibling;
  }
  return SMVlist;
}


LinkedList subscribeToLocalDAInputs(IedModel_extensions* self, IedModel* model, IedServer server )
{
  LinkedList DAlist = LinkedList_create();

  char iedNameString [130];
  StringUtils_copyStringToBuffer(model->name, iedNameString);
  char* separator = iedNameString + strlen(iedNameString);

  StringUtils_copyStringToBuffer(model->firstChild->name, separator);

  Input* inputs = self->inputs;
  while(inputs != NULL)
  {
    InputEntry* extRef = inputs->extRefs; 
    while(extRef != NULL)//find all matching extref for this extRef
    {
      if(true)//strcmp_p(extRef->serviceType, "Poll") == 0)//if type is polling
      { 
        char buf1 [130];
        StringUtils_copyStringToBuffer(extRef->Ref, buf1);
        separator = strchr(buf1, '/');
        *separator = 0;
        
        if(strcmp_p(buf1, iedNameString) == 0)// IED is our own IED, link the mmsValue
        {
          DataAttribute* da = (DataAttribute*) IedModel_getModelNodeByObjectReference(model, extRef->Ref);
          MmsValue* value = IedServer_getAttributeValue(server, da);
          extRef->value = value;

          InputValue * inputValue = create_InputValue(0, da, inputs, extRef);
          
          LinkedList DAlist_local = DAlist;
          while( DAlist_local != NULL && inputValue != NULL)
          {
            InputValue * inputValue_local = (InputValue *) DAlist_local->data;
            if(inputValue_local != NULL && inputValue_local->DA != NULL && inputValue_local->DA == da)//find a similar DA
            {
              while(inputValue_local->sibling != NULL)//find the last entry in the list of this DA
              {
                inputValue_local = inputValue_local->sibling;
              }
              //add this entry to the list of the similar DA's
              inputValue_local->sibling = inputValue;
              inputValue = NULL; //ensure we add only once
            }
            DAlist_local = LinkedList_getNext(DAlist_local);
          }
          //if we did not add it to any existing list
          if(inputValue != NULL)
          {
            //then add an entry to the linked list
            LinkedList_add(DAlist,inputValue);
          }
        }
      }
      extRef = extRef->sibling;
    }
    inputs = inputs->sibling;
  }
  return DAlist;
}


//called for subscribed GOOSE data
void subscriber_callback_inputs_GOOSE(GooseSubscriber subscriber, void* parameter)
{
  InputValue* inputVal = (InputValue*)parameter;
  if(inputVal != NULL && inputVal->extRef != NULL)  //iterate trough list of value-indexes that need to be copied, and
  {
    MmsValue* values = GooseSubscriber_getDataSetValues(subscriber);
    if(MmsValue_getType(values) == MMS_STRUCTURE || MmsValue_getType(values) == MMS_ARRAY)
    {
      int arraySize = MmsValue_getArraySize(values);
      int arrayIndex;
      for(arrayIndex=0; arrayIndex<arraySize; arrayIndex++)
      {
        //find all extrefs for this index
        while(inputVal->index == arrayIndex)
        {
          MmsValue* value = MmsValue_getElement(values, inputVal->index);
          if(value == NULL)
          {
            printf("ERROR: could not retrieve element from subscribed GOOSE dataset, '%s' value not updated\n",inputVal->extRef->Ref);
            return;
          }
          printf("GOOSE: copying value-index %i to extRef:'%s'\n", inputVal->index, inputVal->extRef->Ref);
          if(inputVal->extRef->value == NULL)
            inputVal->extRef->value = MmsValue_clone(value);
          else
          {
            if(!MmsValue_update(inputVal->extRef->value, value))
              printf("ERROR: GOOSE datatype does not match, '%s' value not updated\n",inputVal->extRef->Ref);
          }

          //perform trigger for value update
          if(inputVal->extRef->callBack != NULL){
            inputVal->extRef->callBack(inputVal->extRef);
          }
          if(inputVal->sibling != NULL)
            inputVal = inputVal->sibling;
          else
            break;
        }
      }
    }
    else
    {
      printf("ERROR: general GOOSE datatype does not match, '%s' value not updated\n",inputVal->extRef->Ref);
    }
  }
  else
  {
    printf("ERROR: no valid GOOSE inputval struct, no data processed\n");
  }
}

//called for subscribed SMV data
void subscriber_callback_inputs_SMV(SVSubscriber subscriber, void* parameter, SVSubscriber_ASDU asdu)
{
  uint64_t tm = SVSubscriber_ASDU_getRefrTmAsMs(asdu);//Hal_getTimeInMs();
  InputValue* inputVal = (InputValue*)parameter;
  if(inputVal != NULL && inputVal->extRef != NULL)  //iterate trough list of value-indexes that need to be copied, and
  {
    int size = SVSubscriber_ASDU_getDataSize(asdu);
    if(size > 63)//set to fixed size of 9-2LE
    {
      int32_t val[size/4];
      int arrayIndex;
      for(arrayIndex=0; arrayIndex < (size/4); arrayIndex += 2)//read the stval and q. time is for all the same.
      {
        val[arrayIndex] = SVSubscriber_ASDU_getINT32(asdu, arrayIndex * 4 );
        Quality q = SVSubscriber_ASDU_getQuality(asdu, (arrayIndex * 4) + 4 );
        val[arrayIndex + 1] = (int)q;
      }
      for(arrayIndex=0; arrayIndex < (size/8); arrayIndex++)//a mmsval with stval, q and time is expected
      {
        //find all extrefs for this index
        while(inputVal->index == arrayIndex)
        {
          //performancewise this could be improved, by performing the copy directly
          MmsValue* value = MmsValue_createEmptyStructure(3);

          MmsValue* stVal = MmsValue_newIntegerFromInt32(val[(arrayIndex * 2)]);
          MmsValue_setElement(value,0,stVal);
          
          MmsValue* q = MmsValue_newUnsignedFromUint32(val[(arrayIndex * 2) + 1]);
          MmsValue_setElement(value,1,q);
          
          MmsValue* t = MmsValue_newUtcTimeByMsTime(tm);
          MmsValue_setElement(value,2,t);

          if(inputVal->extRef->value == NULL)
          {
            inputVal->extRef->value = value;
          }
          else
          {
            if(!MmsValue_update(inputVal->extRef->value,value))
              printf("ERROR: SMV datatype does not match, '%s' value not updated\n",inputVal->extRef->Ref);
            MmsValue_delete(value);
          }
          
          //perform trigger for value update
          if(inputVal->extRef->callBack != NULL){
            inputVal->extRef->callBack(inputVal->extRef);
          }
          if(inputVal->sibling != NULL)
            inputVal = inputVal->sibling;
          else
            break;
        }
      }
    }
    else
    {
      printf("ERROR: SMV dataset not a valid size\n");
    }
  }
  else
  {
    printf("ERROR: no valid SMV inputval struct, no data processed\n");
  }
}


Input* getInput(IedModel_extensions* model, LogicalNode* ln)
{
    Input* inputs = model->inputs;
    while(inputs != NULL)//for each LN with an inputs/extref defined;
    {
      if(inputs->parent == ln)
      {
        return inputs;
      }
      inputs = inputs->sibling;
    }
    return NULL;
}

//update an inputvalue that contains a DA
void InputValueHandleExtensionCallbacks(void* param)
{
  InputValue* inputValue = param;
  //call all inputVals that are associated with this (local)DA
  while(inputValue != NULL)//list of associated inputvals with this DA
  {
    if(inputValue->extRef->callBack != NULL)
      inputValue->extRef->callBack(inputValue->extRef);

    inputValue = inputValue->sibling;
  }
}

//update an inputvalue that contains a DA
void UpdateAttributeValueEx(IedServer self, InputValue* inputValue, MmsValue* value)
{
  IedServer_updateAttributeValue(self, inputValue->DA, value);

  //call all inputVals that are associated with this (local)DA
  InputValueHandleExtensionCallbacks(inputValue);
}

//retrieve the inputValue_list associated with a DA. An inputvalue_list is a linked list of elements that use the DA as input
//during an update of the DA, all DA related inputvalues in the list will receive a callback
InputValue* _findAttributeValueEx(DataAttribute* dataAttribute, LinkedList inputvalues)
{
  while(inputvalues != NULL)//for each LN with an inputs/extref defined;
  {
    if(inputvalues->data != NULL)
    {
      InputValue* inputValue = inputvalues->data;
      if(inputValue->DA == dataAttribute)
      {
        return inputValue;
      }
    }
    inputvalues = LinkedList_getNext(inputvalues);
  }
  return NULL;
}

//call AttributeValueHandleExtensionCallback
//this call will trigger an update of all input elements that refer to this DA.
//slow, as it will iterate trough the whole list, instead this call can be done once during initialisation
void AttributeValueHandleExtensionCallbacks(DataAttribute* dataAttribute, LinkedList inputvalues)
{
  InputValue* inputValue = _findAttributeValueEx(dataAttribute, inputvalues);
  if(inputValue != NULL)
  {
    InputValueHandleExtensionCallbacks(inputValue);
  }
}







