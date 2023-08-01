
set(simulation_SRCS
   simulation.c
)

include_directories(
    ./inc
)

add_library(simulation SHARED
  ${simulation_SRCS}
)

target_link_libraries(simulation
    pthread
)

set_target_properties( simulation
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)