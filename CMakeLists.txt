cmake_minimum_required(VERSION 3.22)
project(Code)

set(CMAKE_CXX_STANDARD 14)

add_executable(Code
        cpp/hi.cpp)

add_executable(HW cpp/kmp_bad.c)
