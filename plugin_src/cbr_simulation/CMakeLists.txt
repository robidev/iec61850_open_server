
set(cbr_simulation_SRCS
   cbr_simulation.c
)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/../../inc
    ${IEC61850_INCLUDE_DIR}
)

add_library(cbr_simulation SHARED
  ${cbr_simulation_SRCS}
)

target_compile_options(cbr_simulation PRIVATE
    -Wall
    -Wextra
    -Wshadow
    -Wconversion
    -Wno-unused-parameter
)

target_link_libraries(cbr_simulation
    pthread
)

set_target_properties( cbr_simulation
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)