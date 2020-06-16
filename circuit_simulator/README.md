this is the primary process simulator. it reads the substation section and based on the conductingequipment and terminal elements a netlist is generated. 
logicalnode declarations in this section are used to understand how the primary process is connected to the ieds.
this allows actuators and measurements to be connected to the respective logical node in the ieds over tcp. 
the simulation initiates the connection, and upon failure the data is ignored. 

the submodels are defined in the models subdirectory. The name should match the conductingequipment name in the substation section of the scd.


# install:
pip3 install PySpice

sudo apt install gcc, bison, flex, libtool, autoconf, automake, libreadline-dev
download ngspice-30

in compile_linux.sh > Replace --with-x by --with-ngshared in line ../configure ... .

chmod 700 compile_linux.sh
sudo ./compile_linux.sh
sudo ldconfig

