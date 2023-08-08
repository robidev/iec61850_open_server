/*
 *  inputs_api.h
 *
 */

#ifndef INPUT_API_H_
#define INPUT_API_H_


#include "libiec61850_platform_includes.h"
#include <libiec61850/iec61850_server.h>
#include <libiec61850/iec61850_common.h>
#include <libiec61850/iec61850_model.h>

#include "iec61850_model_extensions.h"

#include <libiec61850/goose_receiver.h>
#include <libiec61850/sv_subscriber.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct sInputValue InputValue;

// struct that describes input-extref elements, and additional data
	//inputValues are lists of input/extref elements that belong to the same dataset(subscriber) or same DA's.
	//an inputvalue describes the data reference(input/extref), the index in the dataset, or associated DA pointer. 
	//It contains a callback that can be used when a new value arrives from the respective source 
struct sInputValue {
  Input* input;                 // pointer to related input 
  InputEntry* extRef;           // pointer to related extref

  int index;                    // index of value in the dataset, if remote value
  DataAttribute* DA;            // data-attribute-reference if local value is referenced by extref
  int32_t RefCount;		// Refcount of packet

  InputValue* sibling;          // additional extref that are related (same DA or same dataset)

};


LinkedList subscribeToGOOSEInputs(IedModel_extensions* self, GooseReceiver GSEreceiver);

LinkedList subscribeToSMVInputs(IedModel_extensions* self, SVReceiver SMVreceiver);

LinkedList subscribeToLocalDAInputs(IedServer server, IedModel_extensions* self, IedModel* model);

Input* getInput(IedModel_extensions* model, LogicalNode* ln);

void InputValueHandleExtensionCallbacks(void* param);

InputValue* _findAttributeValueEx(DataAttribute* dataAttribute, LinkedList inputvalues);

void AttributeValueHandleExtensionCallbacks(DataAttribute *dataAttribute, LinkedList inputvalues);

#ifdef __cplusplus
}
#endif


#endif /* INPUT_API_H_ */
