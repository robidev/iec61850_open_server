cmake_minimum_required(VERSION 2.8.12)

# automagically detect if we should cross-compile
if(DEFINED ENV{TOOLCHAIN})
    set(CMAKE_C_COMPILER	$ENV{TOOLCHAIN}gcc)
    set(CMAKE_CXX_COMPILER	$ENV{TOOLCHAIN}g++)
    set(CMAKE_AR	"$ENV{TOOLCHAIN}ar" CACHE FILEPATH "CW archiver" FORCE)
endif()

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
