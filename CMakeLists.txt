cmake_minimum_required(VERSION 2.8.12)

# automagically detect if we should cross-compile
if(DEFINED ENV{TOOLCHAIN})
    set(CMAKE_C_COMPILER	$ENV{TOOLCHAIN}gcc)
    set(CMAKE_CXX_COMPILER	$ENV{TOOLCHAIN}g++)
    set(CMAKE_AR	"$ENV{TOOLCHAIN}ar" CACHE FILEPATH "CW archiver" FORCE)
endif()

SET(CMAKE_INSTALL_PREFIX /opt)

project(iec61850_open_server)

ENABLE_TESTING()

# feature checks
include(CheckLibraryExists)
check_library_exists(rt clock_gettime "time.h" CONFIG_SYSTEM_HAS_CLOCK_GETTIME)

# check if we are on a little or a big endian
include (TestBigEndian)
test_big_endian(PLATFORM_IS_BIGENDIAN)

include_directories(
    ./inc
)

set(open_server_SRCS
   input/inputs.c
   model/config_file_parser_extensions.c
   model/dynamic_model_extensions.c
   LNs/SMVPublisher.c
   LNs/LNParse.c
   LNs/CILO.c
   LNs/CSWI.c
   LNs/MMXU.c
   LNs/PTOC.c
   LNs/PTRC.c
   LNs/RADR.c
   LNs/XCBR.c
   LNs/XSWI.c
   LNs/LLN0.c
   LNs/TVTR.c
   LNs/TCTR.c

   open_server.c
)

add_executable(open_server
  ${open_server_SRCS}
)

target_link_libraries(open_server
    libiec61850.so
    libiec61850.a
    libhal.a
    libhal-shared.a
    pthread
    m
)

# NOTE: this project uses a dual license scheme, as libiec61850 is covered by GPL 3.0
# this means that any software that incorporates this library should adhere to GPL 3.0 as well
# however, the circuit-simulator does not use libiec61850, and therefore this is apache licensed
# the circuit-simulator should normally be run on a separate, non-realtime test machine, and is 
# therefore ommitted from the install script
install ( TARGETS open_server DESTINATION ${CMAKE_PROJECT_NAME} )

install ( FILES Dockerfile.libiec61850_server DESTINATION ${CMAKE_PROJECT_NAME} )

install ( FILES make_model.sh DESTINATION ${CMAKE_PROJECT_NAME} 
    PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ GROUP_EXECUTE GROUP_READ WORLD_EXECUTE WORLD_READ
)
install ( FILES make_compose.sh DESTINATION ${CMAKE_PROJECT_NAME} 
    PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ GROUP_EXECUTE GROUP_READ WORLD_EXECUTE WORLD_READ
)
install ( FILES README.md DESTINATION ${CMAKE_PROJECT_NAME} )

install ( FILES COPYING DESTINATION ${CMAKE_PROJECT_NAME} )

install ( FILES model_input_generator/genconfig.jar
    DESTINATION ${CMAKE_PROJECT_NAME}/model_input_generator 
    PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ GROUP_WRITE WORLD_READ 
)
install ( FILES model_input_generator/genconfig_input.jar 
    DESTINATION ${CMAKE_PROJECT_NAME}/model_input_generator
    PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ GROUP_WRITE WORLD_READ 
)
install ( FILES model_input_generator/gendocker.jar
    DESTINATION ${CMAKE_PROJECT_NAME}/model_input_generator
    PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ GROUP_WRITE WORLD_READ 
)

install ( DIRECTORY cfg DESTINATION ${CMAKE_PROJECT_NAME} )
install ( DIRECTORY scd DESTINATION ${CMAKE_PROJECT_NAME} ) 
install ( DIRECTORY schema DESTINATION ${CMAKE_PROJECT_NAME} ) 




