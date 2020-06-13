/*
 *  inputs_api.h
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

#ifndef INPUT_API_H_
#define INPUT_API_H_


#include "libiec61850_platform_includes.h"
#include "iec61850_server.h"
#include "iec61850_common.h"
#include "iec61850_model.h"

#include "iec61850_model_extensions.h"

#include "goose_receiver.h"
#include "sv_subscriber.h"

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

  InputValue* sibling;          // additional extref that are related (same DA or same dataset)
};


LinkedList subscribeToGOOSEInputs(IedModel_extensions* self, GooseReceiver GSEreceiver);

LinkedList subscribeToSMVInputs(IedModel_extensions* self, SVReceiver SMVreceiver);

LinkedList subscribeToLocalDAInputs(IedModel_extensions* self, IedModel* model, IedServer server );

Input* getInput(IedModel_extensions* model, LogicalNode* ln);

void InputValueHandleExtensionCallbacks(void* param);

InputValue* _findAttributeValueEx(DataAttribute* dataAttribute, LinkedList inputvalues);

#ifdef __cplusplus
}
#endif


#endif /* INPUT_API_H_ */