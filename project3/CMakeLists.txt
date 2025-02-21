cmake_minimum_required (VERSION 3.10)

project(project3)

#bin目录下存最后生成的可执行文件
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

#将源码文件.cpp的目录保存在SRC——LIST变量
aux_source_directory (src SRC_LIST)

#指定头文件路径
include_directories(include)

add_executable(main3 ${SRC_LIST})
