cmake_minimum_required(VERSION 3.5.0)
project(opencvtest VERSION 0.1.0)

include(CTest)
enable_testing()

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

#set(YOUR_DIRECTORY "./")
#target_include_directories(opencvtest PRIVATE ${YOUR_DIRECTORY})

add_executable(opencvtest main.cpp StereoVision.cpp StereoVision.h)

target_link_libraries( opencvtest ${OpenCV_LIBS} )

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
