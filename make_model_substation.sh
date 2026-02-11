#!/bin/sh

PROJECT_ICD_FILE=scd/model_substation.scd

java -jar model_input_generator/genconfig.jar $PROJECT_ICD_FILE -ied FEED1 ./cfg/FEED1.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied FEED1 ./cfg/FEED1.ext

java -jar model_input_generator/genconfig.jar $PROJECT_ICD_FILE -ied FEED2 ./cfg/FEED2.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied FEED2 ./cfg/FEED2.ext

java -jar model_input_generator/genconfig.jar $PROJECT_ICD_FILE -ied BUS1 ./cfg/BUS1.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied BUS1 ./cfg/BUS1.ext

java -jar model_input_generator/genconfig.jar $PROJECT_ICD_FILE -ied BUS2 ./cfg/BUS2.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied BUS2 ./cfg/BUS2.ext

java -jar model_input_generator/genconfig.jar $PROJECT_ICD_FILE -ied BUS2 ./cfg/BUS2.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied BUS2 ./cfg/BUS2.ext

java -jar model_input_generator/genconfig.jar $PROJECT_ICD_FILE -ied TR1 ./cfg/TR1.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied TR1 ./cfg/TR1.ext

java -jar model_input_generator/genconfig.jar $PROJECT_ICD_FILE -ied TR2 ./cfg/TR2.cfg
java -jar model_input_generator/genconfig_input.jar $PROJECT_ICD_FILE -ied TR2 ./cfg/TR2.ext



