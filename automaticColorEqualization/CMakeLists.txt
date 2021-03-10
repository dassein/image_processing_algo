cmake_minimum_required(VERSION 2.8)
project(ACE)

find_package(OpenCV)
include_directories(OpenCV_INCLUDE_DIRS)
add_executable(ACE ACE.cpp)
target_link_libraries(ACE ${OpenCV_LIBRARIES})