
set(local_sample_simulation_SRCS
   main.c
)

include_directories(
    ./inc
)

add_library(local_sample_simulation SHARED
  ${local_sample_simulation_SRCS}
)

target_link_libraries(local_sample_simulation
    pthread
)

set_target_properties( local_sample_simulation
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)