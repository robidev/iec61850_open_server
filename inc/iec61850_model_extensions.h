/*
 *  model_extensions.h
 *
 */

#ifndef MODEL_EXTENSIONS_H_
#define MODEL_EXTENSIONS_H_

#include <libiec61850/iec61850_server.h>
#include <libiec61850/iec61850_common.h>
#include <libiec61850/iec61850_model.h>

#ifdef __cplusplus
extern "C" {
#endif

/** \addtogroup server_api_group
 *  @{
 */

/**
 * @defgroup DATA_MODEL General data model definitions, access and iteration functions
 *
 * @{
 */

/**
 * \brief Root node of the IEC 61850 data model. This is usually created by the model generator tool (genmodel.jar)
 */
typedef struct sIedModel_extensions IedModel_extensions;
typedef struct sLogicalNodeClass LogicalNodeClass;
typedef struct sInput Input;
typedef struct sSubscriberEntry SubscriberEntry;
typedef void (*callBackFunction) (void* param);

// struct that describes the iedmodel elements that are needed to implement the input-model
// the elements can be filled from the SCL using a static datamodel, as well as dynamic config files
struct sIedModel_extensions {
    Input* inputs;                      // describes the input elements in the datamodel
    SubscriberEntry* subRefs;           // describes the dataset-references that can be subscribed to from other IED's
    LogicalNodeClass* logicalNodes;     // describes the class of each LN, so that functions can be attached
};

// struct that describes extref elements from the SCL file, as defined in the standard
typedef struct sInputEntry {
    char* desc;
    char* Ref;
    char* intAddr;
    char* serviceType;
    char* srcRef;

    MmsValue* value;
    callBackFunction callBack;    // callback to be called when value is updated
    void* callBackParam;
    
    struct sInputEntry* sibling;
} InputEntry;

// struct that describes inputs elements from the SCL file, as defined in the standard
struct sInput {
    LogicalNode* parent;
    int elementCount;
    InputEntry* extRefs;
    Input* sibling;
};

// struct that describes dataset elements from the SCL file, as defined in the standard
struct sSubscriberEntry {
    char* variableName; //
    char* Dataset; //
    uint16_t APPID; //
    char* cbRef; //svCbRef/goCbRef
    char* ID; //svID/goID
    uint8_t ethAddr[6]; //smv ethaddr[6]
    struct sSubscriberEntry* sibling;
};

// struct that describes the class of each logical node in the model, and allows code to be attached
struct sLogicalNodeClass {
  LogicalNode* parent;
  char* lnClass;
  void* instance;
  LogicalNodeClass* sibling;
};

#ifdef __cplusplus
}
#endif


#endif /* MODEL_EXTENSIONS_H_ */
