cmake_minimum_required(VERSION 3.10)

project(project2)

#将当前目录的所有源码文件保存在SRC——LIST这个变量中
aux_source_directory(. SRC_LIST)

#add_executable(main2 main.cpp test1.cpp test2.cpp)
add_executable(main2 ${SRC_LIST})
