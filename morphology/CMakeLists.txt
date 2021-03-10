cmake_minimum_required(VERSION 2.8)
project(extract_contour)

# set(CMAKE_BUILD_TYPE Release)
# set(CMAKE_CXX_FLAGS "-std=c++14 -O3")
# list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

# OpenCV
find_package(OpenCV REQUIRED)
# include_directories(${OpenCV_INCLUDE_DIRS}) # we can use this statement as well
include_directories(OpenCV_INCLUDE_DIRS)

add_executable(dilate_erode dilate_erode.cpp)
target_link_libraries(dilate_erode ${OpenCV_LIBS})
set( CMAKE_INSTALL_BINDIR "${CMAKE_SOURCE_DIR}/bin/")
install(TARGETS dilate_erode
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

add_executable(open_close open_close.cpp)
target_link_libraries(open_close ${OpenCV_LIBS})
set( CMAKE_INSTALL_BINDIR "${CMAKE_SOURCE_DIR}/bin/")
install(TARGETS open_close
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

add_executable(open_extract_line open_extract_line.cpp)
target_link_libraries(open_extract_line ${OpenCV_LIBS})
set( CMAKE_INSTALL_BINDIR "${CMAKE_SOURCE_DIR}/bin/")
install(TARGETS open_extract_line
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

# commands for compile to "./build"" folder, and install to "./bin" folder:
# mkdir build
# cd ./build
# cmake ..
# make 
# make install