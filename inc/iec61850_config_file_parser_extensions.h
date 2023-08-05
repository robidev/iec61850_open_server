/*
 *  config_file_parser_extensions.h
 *
 */

#ifndef CONFIG_FILE_PARSER_EXTENSIONS_H_
#define CONFIG_FILE_PARSER_EXTENSIONS_H_

#include <libiec61850/iec61850_model.h>
#include "iec61850_model_extensions.h"

#ifdef __cplusplus
extern "C" {
#endif

LIB61850_API IedModel_extensions*
ConfigFileParser_createModelFromConfigFileEx_inputs(const char* filename,IedModel* iedModel);

#ifdef __cplusplus
}
#endif

#endif /* CONFIG_FILE_PARSER_EXTENSIONS_H_ */
