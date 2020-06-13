/*
 *  config_file_parser_extensions.c
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

#include "iec61850_server.h"
#include "iec61850_dynamic_model.h"
#include "iec61850_config_file_parser.h"

#include "iec61850_model_extensions.h"
#include "iec61850_dynamic_model_extensions.h"
#include "iec61850_config_file_parser_extensions.h"

#include "libiec61850_platform_includes.h"
#include "stack_config.h"

#define READ_BUFFER_MAX_SIZE 1024

static uint8_t lineBuffer[READ_BUFFER_MAX_SIZE];

IedModel_extensions*
ConfigFileParser_createModelFromConfigFile_inputs(FileHandle fileHandle,IedModel* iedModel);

static int
readLine(FileHandle fileHandle, uint8_t* buffer, int maxSize)
{
    int bytesRead = 0;
    int bufPos = 0;

    int fileReadResult = 1;

    /* eat up leading cr or lf */
    while (fileReadResult > 0) {
        fileReadResult = FileSystem_readFile(fileHandle, buffer + bufPos, 1);

        if (fileReadResult == 1) {

            if (!((buffer[bufPos] == '\n') || (buffer[bufPos] == '\r'))) {
                bufPos++;
                bytesRead++;
                break;
            }
        }
    }

    if (fileReadResult > 0) {
        while (fileReadResult > 0) {
            fileReadResult = FileSystem_readFile(fileHandle, buffer + bufPos, 1);

            if (fileReadResult == 1) {

                if ((buffer[bufPos] == '\n') || (buffer[bufPos] == '\r'))
                    break;
                else {
                    bufPos++;
                    bytesRead++;
                }
            }
        }
    }


    return bytesRead;
}

static void
terminateString(char* string, char ch)
{
    int index = 0;

    while (string[index] != 0) {
        if (string[index] == ch) {
            string[index] = 0;
            break;
        }

        index++;
    }
}

IedModel_extensions*
ConfigFileParser_createModelFromConfigFileEx_inputs(const char* filename,IedModel* iedModel)
{
    FileHandle configFile = FileSystem_openFile((char*)filename, false);

    if (configFile == NULL) {
        if (DEBUG_IED_SERVER)
            printf("IED_SERVER: Error opening config file!\n");
        return NULL;
    }

    IedModel_extensions* model = ConfigFileParser_createModelFromConfigFile_inputs(configFile, iedModel);

    FileSystem_closeFile(configFile);

    return model;
}

IedModel_extensions*
ConfigFileParser_createModelFromConfigFile_inputs(FileHandle fileHandle,IedModel* iedModel)
{
    int bytesRead = 1;

    bool stateInModel = false;
    int indendation = 0;

    IedModel* IEDmodel = iedModel;
    IedModel_extensions* model = NULL;
    LogicalDevice* currentLD = NULL;
    LogicalNode* currentLN = NULL;
    ModelNode* currentModelNode = NULL;
    DataSet* currentDataSet = NULL;
    Input* currentInput = NULL;
    GSEControlBlock* currentGoCB = NULL;
    SVControlBlock* currentSvCB = NULL;

    char nameString[130];
    char nameString2[130];
    char nameString3[130];

    int currentLine = 0;

    while (bytesRead > 0) {
        bytesRead = readLine(fileHandle, lineBuffer, READ_BUFFER_MAX_SIZE);

        currentLine++;

        if (bytesRead > 0) {
            lineBuffer[bytesRead] = 0;

            if (stateInModel) {

                if (StringUtils_startsWith((char*) lineBuffer, "}")) {
                    if (indendation == 1) {
                        stateInModel = false;
                        indendation = 0;
                    }
                    else if (indendation == 2) {
                        indendation = 1;
                    }
                    else if (indendation == 3) {
                        indendation = 2;
                    }
                    else if (indendation == 4) {
                        indendation = 3;
                    }
                    else if (indendation > 4) {
                        currentModelNode = currentModelNode->parent;
                        indendation--;
                    }
                }

                else if (indendation == 1) {
                    if (StringUtils_startsWith((char*) lineBuffer, "LD")) {
                        indendation = 2;

                        if (sscanf((char*) lineBuffer, "LD(%s)", nameString) < 1)
                            goto exit_error;

                        terminateString(nameString, ')');

                        // find the LD in the existing model
                        currentLD = IEDmodel->firstChild;
                        while(currentLD != NULL)
                        {
                            if(strcmp(currentLD->name,nameString) == 0)
                                break;
                            currentLD = (LogicalDevice*)currentLD->sibling;
                        }
                        //if the LDname cannot be found in the model, create it
                        if(currentLD == NULL)
                            currentLD = LogicalDevice_create(nameString, IEDmodel);
                    }
                    else if (StringUtils_startsWith((char*) lineBuffer, "SD")) {
                        uint32_t appid = 0;
                        char nameString4[130];
                        char nameString5[130];
                        uint8_t ethAddr[6];
                        //SD( simpleIOGenericIO/GGIO1$ST$SPCSO1$stVal Events 4096 0x1,0xc,0xcd,0x1,0x0,0x1 gcbEvents events );
                        int matchedItems = sscanf((char*) lineBuffer, "SD(%s %s %u %s %s %s)",
                                nameString, nameString2, &appid, nameString3, nameString4, nameString5);
                        
                        if (matchedItems < 6) goto exit_error;
                        terminateString(nameString5, ')');

                        if (StringUtils_createBufferFromHexString(nameString3, ethAddr) != 6)
                            goto exit_error;
         
                        SubscriberEntry_create(model, nameString, nameString2, appid, nameString4, nameString5, ethAddr);

                    }
                    else
                        goto exit_error;
                }
                else if (indendation == 2) {
                    if (StringUtils_startsWith((char*) lineBuffer, "LN")) {
                        indendation = 3;

                        if (sscanf((char*) lineBuffer, "LN(%s)", nameString) < 1)
                            goto exit_error;

                        terminateString(nameString, ')');

                        
                        // find the LN in the existing model
                        currentLN = (LogicalNode*)currentLD->firstChild;
                        while(currentLN != NULL)
                        {
                            if(strcmp(currentLN->name,nameString) == 0)
                                break;
                            currentLN = (LogicalNode*)currentLN->sibling;
                        }
                        //if the LNname cannot be found in the model, create it
                        if(currentLN == NULL)
                            currentLN = LogicalNode_create(nameString, currentLD);
                    }
                    else
                        goto exit_error;
                }
                else if (indendation == 3) {
                    if (StringUtils_startsWith((char*) lineBuffer, "IN")) {
                        indendation = 4;

                        currentInput = Input_create(currentLN, model);
                    }
                    else if (StringUtils_startsWith((char*) lineBuffer, "CL")) {
                        sscanf((char*) lineBuffer, "CL(%s)", nameString);
                        terminateString(nameString, ')');
                        LogicalNodeClass_create(currentLN, model,nameString);
                    }
                    else if (StringUtils_startsWith((char*) lineBuffer, "SV")) {
                        uint32_t confRev = 0;
                        uint8_t smpMod = 0;
                        uint32_t smpRate = 0;
                        uint8_t optFlds = 0;
                        uint8_t isUnicast = 0;
                        int matchedItems = sscanf((char*) lineBuffer, "SV(%s %s %s %i %c %i %c %c)", 
                            nameString, 
                            nameString2, 
                            nameString3, 
                            &confRev, 
                            &smpMod, 
                            &smpRate, 
                            &optFlds, 
                            &isUnicast );

                        if (matchedItems < 8) goto exit_error;
                        //                    name        ln         svID         dataSet      convRev  smpMod  smpRate  optFlds isUnicast
                        currentSvCB = SVControlBlock_create(nameString, currentLN, nameString2, nameString3, confRev, smpMod, (uint16_t)smpRate, optFlds, isUnicast);
                        if (currentLN != NULL)
                            LogicalNode_addSVControlBlock(currentLN, currentSvCB);
                        indendation = 4;            
                    }
                    else {
                        if (DEBUG_IED_SERVER)
                            printf("IED_SERVER: Unknown identifier (%s)\n", lineBuffer);

                        goto exit_error;
                    }

                }
                else if (indendation > 3) {
                    if (StringUtils_startsWith((char*) lineBuffer, "ER")) {
                        char serviceType[130];
                        char srcRef[130];
                        sscanf((char*) lineBuffer, "ER(%s %s %s %s %s)", nameString, nameString2, nameString3, serviceType, srcRef );
                        terminateString(srcRef, ')');

                        InputEntry_create(currentInput, nameString,nameString2,nameString3, serviceType, srcRef);
                    }
                    else if (StringUtils_startsWith((char*) lineBuffer, "PS")) {
                        uint32_t vlanPrio;
                        uint32_t vlanId;
                        uint32_t appId;

                        int matchedItems = sscanf((char*) lineBuffer, "PS(%u %u %u %s)", &vlanPrio, &vlanId, &appId, nameString);

                        if ((matchedItems != 4) || (currentSvCB == NULL)) goto exit_error;

                        terminateString(nameString, ')');

                        if (strlen(nameString) != 12) goto exit_error;

                        if (StringUtils_createBufferFromHexString(nameString, (uint8_t*) nameString2) != 6)
                            goto exit_error;


                        PhyComAddress* dstAddress =
                                PhyComAddress_create((uint8_t) vlanPrio, (uint16_t) vlanId, (uint16_t) appId,
                                        (uint8_t*) nameString2);
                        SVControlBlock_addPhyComAddress(currentSvCB, dstAddress);
                    }
                    else
                        goto exit_error;
                }


            }
            else {
                if (StringUtils_startsWith((char*) lineBuffer, "MODEL{")) {

                    model = IedModel_extensions_create();
                    if(IEDmodel == NULL)
                        IEDmodel = IedModel_create("");

                    stateInModel = true;
                    indendation = 1;
                }
                else if (StringUtils_startsWith((char*) lineBuffer, "MODEL(")) {
                    sscanf((char*) lineBuffer, "MODEL(%s)", nameString);
                    terminateString(nameString, ')');
                    model = IedModel_extensions_create();

                    if(IEDmodel == NULL) 
                        IEDmodel = IedModel_create(nameString);
                    else if(strcmp(IEDmodel->name,nameString) != 0)
                        IEDmodel = IedModel_create(nameString);
                    
                    stateInModel = true;
                    indendation = 1;
                }
                else
                    goto exit_error;
            }
        }
    }

    return model;

exit_error:
    if (DEBUG_IED_SERVER)
        printf("IED_SERVER: error parsing line %i (indendation level = %i)\n", currentLine, indendation);
    IedModel_destroy_inputs(model);
    return NULL;
}


