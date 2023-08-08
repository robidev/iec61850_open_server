
set(python_SRCS
   main.c
)

include_directories(
    ./inc
    /usr/include/python3.11
)

add_library(python SHARED
  ${python_SRCS}
)

target_link_libraries(python
    pthread
    python3.11
)

set_target_properties( python
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)