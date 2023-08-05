
set(cbr_simulation_SRCS
   main.c
)

include_directories(
    ./inc
)

add_library(cbr_simulation SHARED
  ${cbr_simulation_SRCS}
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