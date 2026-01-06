
set(python_SRCS
   main.c
)

find_package(Python3 COMPONENTS Development REQUIRED)

include_directories(
    ./inc
    ${Python3_INCLUDE_DIRS}
)

add_library(python SHARED
  ${python_SRCS}
)

target_link_libraries(python
    pthread
    ${Python3_LIBRARIES}
)

set_target_properties( python
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)