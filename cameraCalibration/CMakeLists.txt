cmake_minimum_required(VERSION 3.5)
set(TARGET_NAME CalibrateDemo)

set(CMAKE_CXX_STANDARD 20)

project( ${TARGET_NAME} )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
# add_executable( ${TARGET_NAME} ${TARGET_NAME}.cpp )
add_executable( ${TARGET_NAME} main.cpp )
target_link_libraries( ${TARGET_NAME} ${OpenCV_LIBS} )
