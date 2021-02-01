#!/bin/sh

PROJECT_ICD_FILE=scd/open_substation.scd

java -jar model_input_generator/gendocker.jar $PROJECT_ICD_FILE substation.yml
