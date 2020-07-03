# Circuit simulator
This is the primary process simulator. it reads the SCL substation section and based on the conducting-equipment and terminal elements a netlist is generated. 
Logicalnode declarations in this SCL section are used to understand how the primary process is connected to the ieds.
This allows actuators and measurements to be connected to the respective logical node in the ieds using a basic TCP protocol. 
The simulation initiates the connection, and upon failure the data is ignored.  

![Alt text](screenshot.png?raw=true "Screenshot of simulation interface")

The submodels are defined in the models subdirectory. The name should match the conductingequipment name in the substation section of the scd. 

# Docker install:

Navigate to the docker-file

`$ cd ..`

build the container

`$ sudo docker build -f Dockerfile.circuit_simulator --tag simulator .`

run the container

`$ sudo docker run --rm -p 5010:5010 simulator`

and browse to

http://127.0.0.1:5010

# Local install:

`$ sudo apt install gcc, bison, flex, libtool, autoconf, automake, libreadline-dev`

download ngspice-30 from http://ngspice.sourceforge.net/download.html and cd into directory

in compile_linux.sh > Replace --with-x by --with-ngshared in line ../configure ... .

`$ chmod 700 compile_linux.sh`
`$ sudo ./compile_linux.sh 64`
`$ sudo ldconfig`

`$ cd ../circuit_simulator`

`$ pip3 install -r requirements.txt`

`$ python3 webAPI.py`

and browse to

http://127.0.0.1:5010
