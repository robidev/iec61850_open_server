
set(ctr_simulation_SRCS
   main.c
)

include_directories(
    ./inc
)

add_library(ctr_simulation SHARED
  ${ctr_simulation_SRCS}
)

target_link_libraries(ctr_simulation
    pthread
)

set_target_properties( ctr_simulation
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)