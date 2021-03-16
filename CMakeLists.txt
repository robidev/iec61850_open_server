cmake_minimum_required(VERSION 2.8.12)

# automagically detect if we should cross-compile
if(DEFINED ENV{TOOLCHAIN})
    set(CMAKE_C_COMPILER	$ENV{TOOLCHAIN}gcc)
    set(CMAKE_CXX_COMPILER	$ENV{TOOLCHAIN}g++)
    set(CMAKE_AR	"$ENV{TOOLCHAIN}ar" CACHE FILEPATH "CW archiver" FORCE)
endif()

project(iec61850_open_server-dpdk)

ENABLE_TESTING()

set(PROJECT_VERSION_MAJOR "0")
set(PROJECT_VERSION_MINOR "9")
set(PROJECT_VERSION_PATCH "0")
set(PROJECT_VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${PROJECT_VERSION_PATCH}")

  
# feature checks
include(CheckLibraryExists)
check_library_exists(rt clock_gettime "time.h" CONFIG_SYSTEM_HAS_CLOCK_GETTIME)

# check if we are on a little or a big endian
include (TestBigEndian)
test_big_endian(PLATFORM_IS_BIGENDIAN)

#include_directories(${CMAKE_SOURCE_DIR}/../libiec61850/build)
#link_directories(../libiec61850/build/hal)
#link_directories(../libiec61850/build/src)

include_directories(
    ./inc
)

SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fno-stack-protector -Wall -Wextra -Wno-unused-parameter -g -O3 -std=gnu11 -mavx2")
SET(CMAKE_EXE_LINKER_FLAGS "-static")   

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

SET(DPDK_LIBS
	rte_net      rte_ethdev       rte_distributor 	 rte_mbuf      rte_pmd_bond       rte_kni              rte_pmd_ring     
	rte_acl      rte_eal          rte_kvargs   	 rte_mempool   rte_mempool_ring	  rte_pmd_e1000        rte_pmd_virtio   rte_ring
	rte_cfgfile  rte_hash         rte_lpm      	 rte_meter     rte_pmd_i40e   	  rte_sched        rte_timer
	rte_cmdline  rte_ip_frag      rte_pipeline 	 rte_pmd_ixgbe rte_mempool_stack  rte_table        rte_pmd_bnxt
	rte_pmd_ena  rte_pmd_nfp      rte_stack          rte_bus_vdev  rte_bus_pci        rte_pci              rte_cryptodev
)

add_executable(open_server-dpdk
  ${open_server_SRCS}
)
target_link_libraries (open_server-dpdk
  -Wl,--whole-archive -Wl,--start-group ${DPDK_LIBS} -Wl,--end-group pthread -Wl,--no-whole-archive dl rt m numa iec61850-dpdk hal-dpdk
)


# NOTE: this project uses a dual license scheme, as libiec61850 is covered by GPL 3.0
# this means that any software that incorporates this library should adhere to GPL 3.0 as well
# however, the circuit-simulator does not use libiec61850, and therefore this is apache licensed
# the circuit-simulator should normally be run on a separate, non-realtime test machine, and is 
# therefore ommitted from the install script
install ( TARGETS open_server-dpdk DESTINATION ${CMAKE_PROJECT_NAME} COMPONENT Applications)

install ( FILES Dockerfile.libiec61850_server DESTINATION ${CMAKE_PROJECT_NAME} COMPONENT Data)

install ( FILES make_model.sh DESTINATION ${CMAKE_PROJECT_NAME} 
    PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ GROUP_EXECUTE GROUP_READ WORLD_EXECUTE WORLD_READ
    COMPONENT Data
)
install ( FILES make_compose.sh DESTINATION ${CMAKE_PROJECT_NAME} 
    PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ GROUP_EXECUTE GROUP_READ WORLD_EXECUTE WORLD_READ
    COMPONENT Data
)
install ( FILES README.md DESTINATION ${CMAKE_PROJECT_NAME} COMPONENT Data )

install ( FILES COPYING DESTINATION ${CMAKE_PROJECT_NAME} COMPONENT Data )

install ( FILES model_input_generator/genconfig.jar
    DESTINATION ${CMAKE_PROJECT_NAME}/model_input_generator 
    PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ GROUP_WRITE WORLD_READ 
    COMPONENT Data
)
install ( FILES model_input_generator/genconfig_input.jar 
    DESTINATION ${CMAKE_PROJECT_NAME}/model_input_generator
    PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ GROUP_WRITE WORLD_READ 
    COMPONENT Data
)
install ( FILES model_input_generator/gendocker.jar
    DESTINATION ${CMAKE_PROJECT_NAME}/model_input_generator
    PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ GROUP_WRITE WORLD_READ 
    COMPONENT Data
)

install ( DIRECTORY cfg DESTINATION ${CMAKE_PROJECT_NAME} COMPONENT Data )
install ( DIRECTORY scd DESTINATION ${CMAKE_PROJECT_NAME} COMPONENT Data ) 
install ( DIRECTORY schema DESTINATION ${CMAKE_PROJECT_NAME} COMPONENT Data ) 


set(CPACK_PACKAGE_DESCRIPTION "IEC 61850 open server dpdk")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "IEC 61850 open server dpdk")
set(CPACK_PACKAGE_VENDOR "https://github.com/robidev")
set(CPACK_PACKAGE_CONTACT "robin.dev@gmail.com")
set(CPACK_PACKAGE_VERSION_MAJOR "${PROJECT_VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${PROJECT_VERSION_MINOR}")
set(CPACK_PACKAGE_VERSION_PATCH "${PROJECT_VERSION_PATCH}")
set(CPACK_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}_${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${CPACK_PACKAGE_VERSION_PATCH}_${CMAKE_SYSTEM_PROCESSOR}")
set(CPACK_SOURCE_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}_${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${CPACK_PACKAGE_VERSION_PATCH}")

set(CPACK_COMPONENTS_ALL Applications Data)
set(CPACK_PACKAGE_INSTALL_DIRECTORY "${CMAKE_INSTALL_PREFIX}/${CMAKE_PROJECT_NAME}")

if(EXISTS "${CMAKE_ROOT}/Modules/CPack.cmake")
    include(InstallRequiredSystemLibraries)

    include(CPack)
endif(EXISTS "${CMAKE_ROOT}/Modules/CPack.cmake")


