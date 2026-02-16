cmake_minimum_required(VERSION 3.10)
#cmake_minimum_required(VERSION 2.8.12)

#cmake   -DCMAKE_BUILD_TYPE=Debug   -DCMAKE_INSTALL_PREFIX=$HOME/libiec61850/stage ..
#cmake -DIEC61850_ROOT=$HOME/libiec61850/stage -DCMAKE_BUILD_TYPE=Debug ..

# ------------------------------------------------------------------------------
# Toolchain / Cross compile
# ------------------------------------------------------------------------------
if(DEFINED ENV{TOOLCHAIN})
    set(CMAKE_C_COMPILER   $ENV{TOOLCHAIN}gcc)
    set(CMAKE_CXX_COMPILER $ENV{TOOLCHAIN}g++)
    set(CMAKE_AR           "$ENV{TOOLCHAIN}ar" CACHE FILEPATH "Archiver" FORCE)
endif()

project(iec61850-open-server C)

enable_testing()

# ------------------------------------------------------------------------------
# Version
# ------------------------------------------------------------------------------
set(PROJECT_VERSION_MAJOR 0)
set(PROJECT_VERSION_MINOR 9)
set(PROJECT_VERSION_PATCH 0)
set(PROJECT_VERSION
    "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${PROJECT_VERSION_PATCH}"
)

# ------------------------------------------------------------------------------
# Options
# ------------------------------------------------------------------------------
option(DEBUG "Enable debugging" ON)
option(BUILD_PLUGINS "Build the plugins" ON)

if(DEBUG)
    set(CMAKE_BUILD_TYPE Debug CACHE STRING "" FORCE)
endif()

# ------------------------------------------------------------------------------
# Feature checks
# ------------------------------------------------------------------------------
include(CheckLibraryExists)
check_library_exists(rt clock_gettime "time.h" CONFIG_SYSTEM_HAS_CLOCK_GETTIME)

include(TestBigEndian)
test_big_endian(PLATFORM_IS_BIGENDIAN)

# ------------------------------------------------------------------------------
# libiec61850 (local, non-installed)
# ------------------------------------------------------------------------------
set(IEC61850_ROOT "" CACHE PATH "Path to libiec61850 build or install root")

find_path(IEC61850_INCLUDE_DIR
    NAMES libiec61850/iec61850_server.h
    PATHS
        ${IEC61850_ROOT}/include
)

find_library(IEC61850_LIBRARY
    NAMES iec61850
    PATHS
        ${IEC61850_ROOT}/lib
)

if(NOT IEC61850_LIBRARY OR NOT IEC61850_INCLUDE_DIR)
    message(FATAL_ERROR
        "libiec61850 not found. Set -DIEC61850_ROOT=/path/to/libiec61850"
    )
endif()


# ------------------------------------------------------------------------------
# Sources
# ------------------------------------------------------------------------------
set(open_server_SRCS
    utils/string_utilities.c
    utils/mms_utilities.c
    
    input/inputs.c
    model/config_file_parser_extensions.c
    model/dynamic_model_extensions.c

    functions/rms.c
    functions/dft.c
    functions/dsp.c

    LNs/SMVPublisher.c
    LNs/LNParse.c
    LNs/CILO.c
    LNs/CSWI.c
    LNs/MMXU.c
    LNs/PTOC.c
    LNs/PIOC.c
    LNs/PDIF.c
    LNs/PDIS.c
    LNs/PTRC.c
    LNs/RADR.c
    LNs/RBDR.c
    LNs/RDRE.c
    LNs/XCBR.c
    LNs/XSWI.c
    LNs/LLN0.c
    LNs/TVTR.c
    LNs/TCTR.c
    LNs/RREC.c

    open_server.c
)

# ------------------------------------------------------------------------------
# Target
# ------------------------------------------------------------------------------
add_executable(open_server ${open_server_SRCS})

target_compile_options(open_server PRIVATE
    -Wall
    -Wextra
    -Wshadow
    -Wconversion
    -Wno-unused-parameter
)

target_include_directories(open_server PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/inc
    ${IEC61850_INCLUDE_DIR}
)

target_link_libraries(open_server
    ${IEC61850_LIBRARY}
    pthread
    dl
    m
)

target_link_options(open_server PRIVATE -rdynamic)

# ------------------------------------------------------------------------------
# Runtime library search path (no install needed)
# ------------------------------------------------------------------------------
set_target_properties(open_server PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
    BUILD_RPATH "${IEC61850_ROOT}/build/src"
)

# ------------------------------------------------------------------------------
# Plugins
# ------------------------------------------------------------------------------
if(BUILD_PLUGINS)
    add_subdirectory(plugin_src)
endif()

# ------------------------------------------------------------------------------
# Install
# ------------------------------------------------------------------------------
install(TARGETS open_server
    DESTINATION ${CMAKE_PROJECT_NAME}
    COMPONENT Applications
)

install(FILES
    Dockerfile.libiec61850_server
    README.md
    COPYING
    DESTINATION ${CMAKE_PROJECT_NAME}
    COMPONENT Data
)

install(PROGRAMS
    make_model.sh
    make_compose.sh
    DESTINATION ${CMAKE_PROJECT_NAME}
    COMPONENT Data
)

install(FILES
    model_input_generator/genconfig.jar
    model_input_generator/genconfig_input.jar
    model_input_generator/gendocker.jar
    DESTINATION ${CMAKE_PROJECT_NAME}/model_input_generator
    COMPONENT Data
)

install(DIRECTORY
    cfg
    scd
    schema
    DESTINATION ${CMAKE_PROJECT_NAME}
    COMPONENT Data
)

# ------------------------------------------------------------------------------
# CPack
# ------------------------------------------------------------------------------
set(CPACK_PACKAGE_DESCRIPTION "IEC 61850 open server")
set(CPACK_PACKAGE_VENDOR "https://github.com/robidev")
set(CPACK_PACKAGE_CONTACT "robin.dev@gmail.com")
set(CPACK_PACKAGE_VERSION ${PROJECT_VERSION})
set(CPACK_PACKAGE_FILE_NAME
    "${CMAKE_PROJECT_NAME}_${PROJECT_VERSION}_${CMAKE_SYSTEM_PROCESSOR}"
)

set(CPACK_COMPONENTS_ALL Applications Data)
set(CPACK_PACKAGE_INSTALL_DIRECTORY
    "${CMAKE_INSTALL_PREFIX}/${CMAKE_PROJECT_NAME}"
)

include(InstallRequiredSystemLibraries)
include(CPack)
