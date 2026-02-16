
set(cbr_process_SRCS
   cbr_process.c
)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/../../inc
    ${IEC61850_INCLUDE_DIR}
)

add_library(cbr_process SHARED
  ${cbr_process_SRCS}
)

target_compile_options(cbr_process PRIVATE
    -Wall
    -Wextra
    -Wshadow
    -Wconversion
    -Wno-unused-parameter
)

target_link_libraries(cbr_process
    pthread
)

set_target_properties( cbr_process
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)