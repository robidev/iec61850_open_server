
find_package(Python3 REQUIRED COMPONENTS Development)

set(python_SRCS
   python.c
)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/../../inc
    ${Python3_INCLUDE_DIRS}
    ${IEC61850_INCLUDE_DIR}
)

add_library(python SHARED
  ${python_SRCS}
)

target_compile_options(python PRIVATE
    -Wall
    -Wextra
    -Wshadow
    -Wconversion
    -Wno-unused-parameter
)

target_link_libraries(python
    pthread
    ${Python3_LIBRARIES}
    ${IEC61850_LIBRARY}
)

set_target_properties( python
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)