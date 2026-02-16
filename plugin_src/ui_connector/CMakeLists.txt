
set(ui_connector_SRCS
   ui_connector.c
   config_parser.c
)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/../../inc
    ${IEC61850_INCLUDE_DIR}
)

add_library(ui_connector SHARED
  ${ui_connector_SRCS}
)

target_compile_options(ui_connector PRIVATE
    -Wall
    -Wextra
    -Wshadow
    -Wconversion
    -Wno-unused-parameter
)

target_link_libraries(ui_connector
    pthread
)

set_target_properties( ui_connector
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/plugin"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)