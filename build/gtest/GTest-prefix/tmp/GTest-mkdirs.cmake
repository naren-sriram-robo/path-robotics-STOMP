# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/nsriram/ws_moveit/build/gtest/../ros_industrial_cmake_boilerplate-googletest-src"
  "/home/nsriram/ws_moveit/build/gtest/../ros_industrial_cmake_boilerplate-googletest-build"
  "/home/nsriram/ws_moveit/build/gtest/GTest-prefix"
  "/home/nsriram/ws_moveit/build/gtest/GTest-prefix/tmp"
  "/home/nsriram/ws_moveit/build/gtest/GTest-prefix/src/GTest-stamp"
  "/home/nsriram/ws_moveit/build/gtest/GTest-prefix/src"
  "/home/nsriram/ws_moveit/build/gtest/GTest-prefix/src/GTest-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/nsriram/ws_moveit/build/gtest/GTest-prefix/src/GTest-stamp/${subDir}")
endforeach()
