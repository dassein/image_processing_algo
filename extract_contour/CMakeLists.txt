cmake_minimum_required(VERSION 2.8)
project(extract_contour)

# set(CMAKE_BUILD_TYPE Release)
# set(CMAKE_CXX_FLAGS "-std=c++14 -O3")
# list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

# OpenCV
find_package(OpenCV REQUIRED)
# include_directories(${OpenCV_INCLUDE_DIRS}) # we can use this statement as well
include_directories(OpenCV_INCLUDE_DIRS)

add_executable(canny_contour1 canny_contour1.cpp)
target_link_libraries(canny_contour1 ${OpenCV_LIBS})
set( CMAKE_INSTALL_BINDIR "${CMAKE_SOURCE_DIR}/bin/")
install(TARGETS canny_contour1
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

add_executable(canny_contour2 canny_contour2.cpp)
target_link_libraries(canny_contour2 ${OpenCV_LIBS})
set( CMAKE_INSTALL_BINDIR "${CMAKE_SOURCE_DIR}/bin/")
install(TARGETS canny_contour2
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

add_executable(hough_transform hough_transform.cpp)
target_link_libraries(hough_transform ${OpenCV_LIBS})
set( CMAKE_INSTALL_BINDIR "${CMAKE_SOURCE_DIR}/bin/")
install(TARGETS hough_transform
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

# commands for compile to "./build"" folder, and install to "./bin" folder:
# mkdir build
# cd ./build
# cmake ..
# make 
# make install