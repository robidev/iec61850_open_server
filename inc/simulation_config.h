#ifndef SIMULATION_CONFIG_H_
#define SIMULATION_CONFIG_H_


#ifdef __cplusplus
extern "C" {
#endif

enum simulation_type {
    SIMULATION_TYPE_NONE,
    SIMULATION_TYPE_LOCAL,
    SIMULATION_TYPE_REMOTE
};

int IEC61850_server_simulation_type();

void IEC61850_server_simulation_next_step();

void IEC61850_server_simulation_sync(int local); // waits until global is unequal to local 

int IEC61850_server_simulation_async(int local); // returns 1 on global equal to local, 0 on not equal

#ifdef __cplusplus
}
#endif


#endif /* SIMULATION_CONFIG_H_ */