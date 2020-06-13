LIBIEC_HOME=../libiec61850

PROJECT_BINARY_NAME = open_server

PROJECT_ICD_FILE = open_substation.scd

PROJECT_SOURCES = input/inputs.c
PROJECT_SOURCES += model/config_file_parser_extensions.c
PROJECT_SOURCES += model/dynamic_model_extensions.c
PROJECT_SOURCES += LNs/SMVPublisher.c
PROJECT_SOURCES += LNs/LNParse.c
PROJECT_SOURCES += LNs/CILO.c
PROJECT_SOURCES += LNs/CSWI.c
PROJECT_SOURCES += LNs/MMXU.c
PROJECT_SOURCES += LNs/PTOC.c
PROJECT_SOURCES += LNs/PTRC.c
PROJECT_SOURCES += LNs/RADR.c
PROJECT_SOURCES += LNs/XCBR.c
PROJECT_SOURCES += LNs/XSWI.c
PROJECT_SOURCES += LNs/LLN0.c
PROJECT_SOURCES += LNs/TVTR.c
PROJECT_SOURCES += LNs/TCTR.c

PROJECT_SOURCES += open_server.c
#PROJECT_SOURCES += static_model.c
#PROJECT_SOURCES += static_input.c

include $(LIBIEC_HOME)/make/target_system.mk
include $(LIBIEC_HOME)/make/stack_includes.mk

LDFLAGS += -lm

INCLUDES += -I./inc

all:	$(PROJECT_BINARY_NAME)

include $(LIBIEC_HOME)/make/common_targets.mk

model:	$(PROJECT_ICD_FILE)
	java -jar $(LIBIEC_HOME)/tools/model_generator/genconfig.jar $(PROJECT_ICD_FILE) -ied IED1_XCBR ./cfg/IED1_XCBR.cfg
	java -jar model_input_generator/genconfig_input.jar $(PROJECT_ICD_FILE) -ied IED1_XCBR ./cfg/IED1_XCBR.ext

	java -jar $(LIBIEC_HOME)/tools/model_generator/genconfig.jar $(PROJECT_ICD_FILE) -ied IED2_PTOC ./cfg/IED2_PTOC.cfg
	java -jar model_input_generator/genconfig_input.jar $(PROJECT_ICD_FILE) -ied IED2_PTOC ./cfg/IED2_PTOC.ext

	java -jar $(LIBIEC_HOME)/tools/model_generator/genconfig.jar $(PROJECT_ICD_FILE) -ied IED3_SMV ./cfg/IED3_SMV.cfg
	java -jar model_input_generator/genconfig_input.jar $(PROJECT_ICD_FILE) -ied IED3_SMV ./cfg/IED3_SMV.ext
	#java -jar $(LIBIEC_HOME)/tools/model_generator/genmodel.jar $(PROJECT_ICD_FILE) -ied IED3_SMV
	#java -jar model_input_generator/genmodel_input.jar $(PROJECT_ICD_FILE) -ied IED3_SMV

compose:	$(PROJECT_ICD_FILE)
	java -jar model_input_generator/gendocker.jar $(PROJECT_ICD_FILE) substation.yml

$(PROJECT_BINARY_NAME):	$(PROJECT_SOURCES) $(LIB_NAME)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(PROJECT_BINARY_NAME) $(PROJECT_SOURCES) $(INCLUDES) $(LIB_NAME) $(LDFLAGS) $(LDLIBS)

clean:
	rm -f $(PROJECT_BINARY_NAME)


