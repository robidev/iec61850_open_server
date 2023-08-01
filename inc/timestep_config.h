#ifndef TIMESTEP_CONFIG_H_
#define TIMESTEP_CONFIG_H_


#ifdef __cplusplus
extern "C" {
#endif

enum timestep_type {
    TIMESTEP_TYPE_LOCAL,
    TIMESTEP_TYPE_REMOTE
};

int IEC61850_server_timestep_type();

void IEC61850_server_timestep_next_step();

void IEC61850_server_timestep_sync(int local); // waits until global is unequal to local 

int IEC61850_server_timestep_async(int local); // returns 1 on global equal to local, 0 on not equal

#ifdef __cplusplus
}
#endif


#endif /* TIMESTEP_CONFIG_H_ */