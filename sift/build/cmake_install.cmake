# Install script for directory: /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/sift" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/sift")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/sift"
         RPATH "")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/sift")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin" TYPE EXECUTABLE FILES "/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/build/sift")
  if(EXISTS "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/sift" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/sift")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/sift"
         OLD_RPATH "/usr/local/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/sift")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/surf" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/surf")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/surf"
         RPATH "")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/surf")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin" TYPE EXECUTABLE FILES "/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/build/surf")
  if(EXISTS "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/surf" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/surf")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/surf"
         OLD_RPATH "/usr/local/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/bin/surf")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
