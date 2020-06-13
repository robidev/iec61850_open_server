# iec61850_inputs
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

# License
This software is licensed under the Apache 2.0 License where applicable. Please note that the libiec61850 is licensed differently (GPLv3), and this license will prevail for components that use this library. 

# Questions and Feedback

Feel free to ask questions and provide feedback using the Github issues. Github issues is also used for backlog items.

# Getting started:

Create a working folder, e.g. substation;  
  
`# mkdir ~/substation`  
`# cd ~/substation`  
  
Get the necesarry libraries;  
`git clone https://github.com/mz-automation/libiec61850.git`  
`git clone https://github.com/robidev/iec61850_inputs.git`  
`# cd iec61850_inputs`  
  
Generate the config files;  
`# make model`  
  
Generate the compose file;  
`# make compose`  
  
Run the Docker compose file;  
`# sudo docker-compose -f substation.yml up`  

# Under development

iec61850 python based client. This is a client that is configured using an SVG file for the mimics and data-references.
