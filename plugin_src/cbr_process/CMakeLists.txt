
set(cbr_process_SRCS
   main.c
)

include_directories(
    ./inc
)

add_library(cbr_process SHARED
  ${cbr_process_SRCS}
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