reference: https://blog.csdn.net/qq_38410730/article/details/102837401

steps of cmake:
```bash
mkdir build && cd build
cmake ..
make
make install
```

for the command `make install`, we should statements in file `CMakeLists.txt`
```txt
Install(TARGETS myrun mylib mystaticlib
       RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
       LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
       ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
```
可执行二进制myrun安装到`${CMAKE_INSTALL_BINDIR}`目录,  
动态库libmylib.so安装到`${CMAKE_INSTALL_LIBDIR}`目录,  
静态库libmystaticlib.a安装到`${CMAKE_INSTALL_LIBDIR}`目录

thus, we can set the `${CMAKE_INSTALL_BINDIR}` as `./bin` in file `CMakeLists.txt`
```txt
set( CMAKE_INSTALL_BINDIR "${CMAKE_SOURCE_DIR}/bin/")
install(TARGETS canny_contour1
       RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
```