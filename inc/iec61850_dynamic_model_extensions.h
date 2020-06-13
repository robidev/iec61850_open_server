/*
 *  dynamic_model_extensions.h
 *
 *  Copyright 2014 Michael Zillgith
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

#ifndef DYNAMIC_MODEL_EXTENSIONS_H_
#define DYNAMIC_MODEL_EXTENSIONS_H_

#include "iec61850_model.h"
#include "iec61850_model_extensions.h"
#include "iec61850_cdc.h"

#ifdef __cplusplus
extern "C" {
#endif

LIB61850_API IedModel_extensions*
IedModel_extensions_create(void);

/**
 * \brief create a new lnClass reference
 *
 * \param name the name of the input
 * \param parent the logical node that hosts the input 
 *
 * \return the new input instance
 */
LIB61850_API LogicalNodeClass*
LogicalNodeClass_create(LogicalNode* parent, IedModel_extensions* model, char * lnClass );


LIB61850_API void
LogicalNode_addSVControlBlock(LogicalNode* self, SVControlBlock* vcb);

/**
 * \brief create a new input
 *
 * \param name the name of the input
 * \param parent the logical node that hosts the input 
 *
 * \return the new input instance
 */
LIB61850_API Input*
Input_create(LogicalNode* parent, IedModel_extensions* model );

/**
 * \brief returns the number of elements (entries) of the Input
 *
 * \param self the instance of the Input
 *
 * \returns the number of Input elements
 */
LIB61850_API int
Input_getSize(Input* self);

LIB61850_API InputEntry*
Input_getFirstEntry(Input* self);

LIB61850_API InputEntry*
InputEntry_getNext(InputEntry* self);

/**
 * \brief create a new Input entry (ExtRef)
 *
 * Create a new ExtRef reference and add it to the given input as a new input member.
 *
 * \param input the input to which the new entry will be added
 * \param description the description of the input
 * \param Ref the reference of the variable as MMS variable name
 * \param intAddr the internal name of the reference
 * \param serviceType the type of service (Poll, Report, GOOSE, SMV)
 * \param srcRef the name of the source control block as MMS variable name
 *
 * \return the new input entry instance
 */
LIB61850_API InputEntry*
InputEntry_create(Input* input, const char* desc, const char* Ref, const char* intAddr, const char* serviceType, const char* srcRef);

/**
 * \brief create a new Subscriber entry
 *
 * Create a new Subscriber dataset element reference and add it to the iedmodel.
 *
 * \param model the model to which the new entry will be added
 * \param variableName the dataset member
 * \param Dataset the dataset of the dataset member
 * \param APPID the AppID name of the dataset member
 * \param cbRef the control block reference of the subscribed control block as MMS variable name
 * \param ID the id of the subscribed control block
 * \param ethAddr the ethernet address of the subscribed dataset
 *
 * \return the new SubscriberEntry instance
 */
LIB61850_API SubscriberEntry*
SubscriberEntry_create(IedModel_extensions* model, const char* variableName, const char* Dataset, uint16_t APPID, const char* cbRef, const char* ID, uint8_t* ethAddr);

LIB61850_API void
IedModel_destroy_inputs(IedModel_extensions* model);
/**@}*/

/**@}*/

#ifdef __cplusplus
}
#endif

#endif /* DYNAMIC_MODEL_EXTENSIONS_H_ */
