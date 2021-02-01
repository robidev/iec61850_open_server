#!/bin/sh


LIBIEC_HOME=../libiec61850

PROJECT_ICD_FILE=scd/open_substation.scd

java -jar $LIBIEC_HOME/tools/model_generator/genconfig.jar $PROJECT_ICD_FILE -ied IED1_XCBR ./cfg/IED1_XCBR.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied IED1_XCBR ./cfg/IED1_XCBR.ext

java -jar $LIBIEC_HOME/tools/model_generator/genconfig.jar $PROJECT_ICD_FILE -ied IED2_PTOC ./cfg/IED2_PTOC.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied IED2_PTOC ./cfg/IED2_PTOC.ext

java -jar $LIBIEC_HOME/tools/model_generator/genconfig.jar $PROJECT_ICD_FILE -ied IED3_SMV ./cfg/IED3_SMV.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied IED3_SMV ./cfg/IED3_SMV.ext

java -jar $LIBIEC_HOME/tools/model_generator/genconfig.jar $PROJECT_ICD_FILE -ied IED4_SMV ./cfg/IED4_SMV.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied IED4_SMV ./cfg/IED4_SMV.ext

#java -jar $(LIBIEC_HOME)/tools/model_generator/genmodel.jar $(PROJECT_ICD_FILE) -ied IED3_SMV
#java -jar model_input_generator/genmodel_input.jar $(PROJECT_ICD_FILE) -ied IED3_SMV

