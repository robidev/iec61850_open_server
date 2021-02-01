# IEC61850_open_server
An implementation of an IED using the libiec61850 library.

This project aims to simulate some options according to the IEC61850 standard, using only the SCL file. 
The main goal is feeding the SCL file into the system, and the system instantiating all IEDS, LD's, 
LN's and services accordingly.

The current implementation contains 3 IED's, a SMV publisher(merging unit), a protection IED containting 
a PTOC that will trigger on an overcurrent, and trigger the PTRC in the same LD. The PTOC is fed by 
sampled values from the merging unit. The PTRC publishes a trip command by GOOSE.
A XCBR IED subscribes to GOOSE messages from the PTRC, and publishes back its stVal.

Process values are static simulations, and not connected to a real process-simulation. This software is not desigend to run realtime. Software uses Docker to run in containers.

The same executable should be usable to describe all IED's, only the config-file should change, allowing
a flexible setup that can be used in a docker container for a more complete simulation setup of a substation.

# Process simulation using pySpice:  
The IEDS support simulated values from a spice-model. 
Currently amps and voltages can be send from the simulation to the IED, and XSWI/XCBR can influence the simulation creating a closed loop between the SPICE model and the IED functions. 
A final showcase is implemented that takes the measurements, sends them to the IED's, and has everything interacting. The simulator can be opened from the client. 

# IEC61850 python based client (iec61850_open_client):  
This is a client that is configured using an SVG file for the mimics and data-references. 
This client will provide a graphical interface to visualize the process, browse the model and control the simulation. 
This is provided as a stand-alone project, but is used in the docker environment as the frontend to the showcase. 

# The frontend
![Alt text](screenshot.png?raw=true "Screenshot of the frontend")

# Usage
When you follow the guide below; "Getting started the most easy way" you are presented with the IEC61850 client in your browser, with the instantiated IED's. The IED's are instantiated by 
the scd file in [scd/open_substation.scd](scd/open_substation.scd)  

You can click the circuit-breaker square(CBR), or the disconnector square(DIS) to open a dialog for operating the element. As it is currently configured as SBO with enhanced security,
you will need to press, select, and then operate. The value in the dialog is prepared to be the opposite of te current value, but can be changed by hand. A succesfull select/operate will
provide feedback in green. If there is an error, it will be shown in red. For example, you will get an error if you try to open the disconnector under load. 
This is because the disconnector will not open or close, if the circuit breaker is engaged due to interlocking(CILO logical node). To operate the disconnector, you should first open the 
circuit breaker.  

In the default state the circuit-breaker and switch are conducting, the 2 merging units are publishing(one for each side of the transformer), and the PTOC is checking if current is too high.
However, you can see in the HMI that current and voltage are 0. This is because the simulation is not running yet.  
To start the simulation, press the 'open simulation tab', wait for the initialisation to finish, and press "play". After a few seconds you should see nominal values in the HMI.  
You can manually open/close the circuit breaker and disconnector. However, the disconnector is protected by interlocking, and cannot open/close if the circuitbreaker is closed.  

Press the play/pause button in the simualtion tab to pause the simulation. You can also modify simulation values by pressing 'modify' in the simulation tab, and choose the elements
in the simulation you wish to modify value of. This way you can change the feed-in voltage per phase, and modify the load per-phase.  

If you want to manually modify a setting in an IED, you can click it's IP in the bottom field of the main client window. This will cause the IED field to display the IED's datamodel.
You can click the data-element you wish to modify, and a write dialog will be displayed.  

# License
This software is licensed under the Apache 2.0 License where applicable. Please note that the libiec61850 is licensed differently (GPLv3), and this license will prevail for components that use this library. 

# Questions and Feedback

Feel free to ask questions and provide feedback using the Github issues. Github issues is also used for backlog items.

# Getting started the most easy way:

This will allow you to just run the existing showcase.

Make sure you have installed the nessecary dependancies (Git and Docker-compose):  
`$ sudo apt install git docker-compose` 

Create a working folder, e.g. substation;  
  
`$ mkdir ~/substation`  
`$ cd ~/substation`  

Get the necesarry projects next to each other in the same directory;  
`$ git clone https://github.com/robidev/iec61850_open_server.git`  
`$ git clone https://github.com/robidev/iec61850_open_client.git`  

cd into the server project  
`$ cd iec61850_open_server`  

Build the Docker containers. Note: this uses the relative path, `../iec61850_open_client` so ensure you have this set up correctly like indicated in step 1;  
`$ sudo docker-compose -f substation.yml -f substation.simulator.yml build`  

Run the Docker compose file;  
`$ sudo docker-compose -f substation.yml -f substation.simulator.yml up`  

To stop the Docker compose file;  
`$ sudo docker-compose -f substation.yml -f substation.simulator.yml down`  
Other methodes to stop the docker-compose file to lead to issues at a restart.  

open the client via the browser at;  
http://127.0.0.1:5000

# Getting started with a modified SCL file:

These steps describe how to generate new configs from a modified SCL file and run them.  

Make sure you have installed the nessecary dependancies (Git,Java and Docker-compose):  
`$ sudo apt install git default-jre docker-compose` 

Create a working folder, e.g. substation;  
  
`$ mkdir ~/substation`  
`$ cd ~/substation`  
  
Get the necessary projects;  
`$ git clone https://github.com/robidev/iec61850_open_server.git`  
`$ git clone https://github.com/robidev/iec61850_open_client.git`  
`$ git clone https://github.com/mz-automation/libiec61850.git`  

cd into the server project  
`$ cd iec61850_open_server`  
  
Generate the config files from the scd-file; (you need libiec61850 for this located in the parent directory)  
`$ ./make_model.sh`  
  
Generate the compose file from the scd-file;  
`$ ./make_compose.sh`  
  
Build the Docker containers. Note: this uses the relative path, `../iec61850_open_client` so ensure you have this;  
`$ sudo docker-compose -f substation.yml -f substation.simulator.yml build`  

Run the Docker compose file;  
`$ sudo docker-compose -f substation.yml -f substation.simulator.yml up`  

open the client via the browser at;  
http://127.0.0.1:5000

