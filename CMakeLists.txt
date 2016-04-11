cmake_minimum_required(VERSION 3.2)
project(v8_test)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

include_directories("/home/chrisvm/.local/lib/v8/include")
set(SOURCE_FILES
    hello_world.cpp)

add_executable(v8_test ${SOURCE_FILES})