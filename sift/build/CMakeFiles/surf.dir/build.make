# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/build

# Include any dependencies generated for this target.
include CMakeFiles/surf.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/surf.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/surf.dir/flags.make

CMakeFiles/surf.dir/surf.cpp.o: CMakeFiles/surf.dir/flags.make
CMakeFiles/surf.dir/surf.cpp.o: ../surf.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/surf.dir/surf.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/surf.dir/surf.cpp.o -c /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/surf.cpp

CMakeFiles/surf.dir/surf.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/surf.dir/surf.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/surf.cpp > CMakeFiles/surf.dir/surf.cpp.i

CMakeFiles/surf.dir/surf.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/surf.dir/surf.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/surf.cpp -o CMakeFiles/surf.dir/surf.cpp.s

# Object files for target surf
surf_OBJECTS = \
"CMakeFiles/surf.dir/surf.cpp.o"

# External object files for target surf
surf_EXTERNAL_OBJECTS =

surf: CMakeFiles/surf.dir/surf.cpp.o
surf: CMakeFiles/surf.dir/build.make
surf: /usr/local/lib/libopencv_stitching.so.3.4.11
surf: /usr/local/lib/libopencv_superres.so.3.4.11
surf: /usr/local/lib/libopencv_videostab.so.3.4.11
surf: /usr/local/lib/libopencv_aruco.so.3.4.11
surf: /usr/local/lib/libopencv_bgsegm.so.3.4.11
surf: /usr/local/lib/libopencv_bioinspired.so.3.4.11
surf: /usr/local/lib/libopencv_ccalib.so.3.4.11
surf: /usr/local/lib/libopencv_dnn_objdetect.so.3.4.11
surf: /usr/local/lib/libopencv_dpm.so.3.4.11
surf: /usr/local/lib/libopencv_face.so.3.4.11
surf: /usr/local/lib/libopencv_freetype.so.3.4.11
surf: /usr/local/lib/libopencv_fuzzy.so.3.4.11
surf: /usr/local/lib/libopencv_hdf.so.3.4.11
surf: /usr/local/lib/libopencv_hfs.so.3.4.11
surf: /usr/local/lib/libopencv_img_hash.so.3.4.11
surf: /usr/local/lib/libopencv_line_descriptor.so.3.4.11
surf: /usr/local/lib/libopencv_optflow.so.3.4.11
surf: /usr/local/lib/libopencv_reg.so.3.4.11
surf: /usr/local/lib/libopencv_rgbd.so.3.4.11
surf: /usr/local/lib/libopencv_saliency.so.3.4.11
surf: /usr/local/lib/libopencv_stereo.so.3.4.11
surf: /usr/local/lib/libopencv_structured_light.so.3.4.11
surf: /usr/local/lib/libopencv_surface_matching.so.3.4.11
surf: /usr/local/lib/libopencv_tracking.so.3.4.11
surf: /usr/local/lib/libopencv_xfeatures2d.so.3.4.11
surf: /usr/local/lib/libopencv_ximgproc.so.3.4.11
surf: /usr/local/lib/libopencv_xobjdetect.so.3.4.11
surf: /usr/local/lib/libopencv_xphoto.so.3.4.11
surf: /usr/local/lib/libopencv_shape.so.3.4.11
surf: /usr/local/lib/libopencv_highgui.so.3.4.11
surf: /usr/local/lib/libopencv_videoio.so.3.4.11
surf: /usr/local/lib/libopencv_viz.so.3.4.11
surf: /usr/local/lib/libopencv_phase_unwrapping.so.3.4.11
surf: /usr/local/lib/libopencv_video.so.3.4.11
surf: /usr/local/lib/libopencv_datasets.so.3.4.11
surf: /usr/local/lib/libopencv_plot.so.3.4.11
surf: /usr/local/lib/libopencv_text.so.3.4.11
surf: /usr/local/lib/libopencv_dnn.so.3.4.11
surf: /usr/local/lib/libopencv_ml.so.3.4.11
surf: /usr/local/lib/libopencv_imgcodecs.so.3.4.11
surf: /usr/local/lib/libopencv_objdetect.so.3.4.11
surf: /usr/local/lib/libopencv_calib3d.so.3.4.11
surf: /usr/local/lib/libopencv_features2d.so.3.4.11
surf: /usr/local/lib/libopencv_flann.so.3.4.11
surf: /usr/local/lib/libopencv_photo.so.3.4.11
surf: /usr/local/lib/libopencv_imgproc.so.3.4.11
surf: /usr/local/lib/libopencv_core.so.3.4.11
surf: CMakeFiles/surf.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable surf"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/surf.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/surf.dir/build: surf

.PHONY : CMakeFiles/surf.dir/build

CMakeFiles/surf.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/surf.dir/cmake_clean.cmake
.PHONY : CMakeFiles/surf.dir/clean

CMakeFiles/surf.dir/depend:
	cd /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/build /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/build /home/dassein/Dropbox/CS_book/图像处理实践/Image_Process_Algo/sift/build/CMakeFiles/surf.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/surf.dir/depend

