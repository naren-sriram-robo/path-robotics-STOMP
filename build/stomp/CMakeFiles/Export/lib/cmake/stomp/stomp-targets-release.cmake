#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "stomp::stomp" for configuration "Release"
set_property(TARGET stomp::stomp APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(stomp::stomp PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libstomp.so"
  IMPORTED_SONAME_RELEASE "libstomp.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS stomp::stomp )
list(APPEND _IMPORT_CHECK_FILES_FOR_stomp::stomp "${_IMPORT_PREFIX}/lib/libstomp.so" )

# Import target "stomp::stomp_example" for configuration "Release"
set_property(TARGET stomp::stomp_example APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(stomp::stomp_example PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/stomp_example"
  )

list(APPEND _IMPORT_CHECK_TARGETS stomp::stomp_example )
list(APPEND _IMPORT_CHECK_FILES_FOR_stomp::stomp_example "${_IMPORT_PREFIX}/bin/stomp_example" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
