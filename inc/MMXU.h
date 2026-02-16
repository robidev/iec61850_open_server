#ifndef MMXU_H_
#define MMXU_H_

#include "iec61850_model_extensions.h"
#include "inputs_api.h"


#ifdef __cplusplus
extern "C" {
#endif

typedef struct sMMXU
{
  IedServer server;
  Input *input;

  void *da_A;
  void *da_V;

  void *da_A_callback;
  void *da_V_callback;

  void *da_A_phsAng[4];
  void *da_V_phsAng[4];

  void *da_A_phs[4];
  void *da_A_phs_callback[4];
  void *da_V_phs[4];
  void *da_V_phs_callback[4];

} MMXU;

void * MMXU_init(IedServer server, LogicalNode* ln, Input* input, LinkedList allInputValues);

#ifdef __cplusplus
}
#endif


#endif /* MMXU_H_ */