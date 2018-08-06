project(Living)
cmake_minimum_required(VERSION 2.8.12)

# import Greeting folder (should contain CMakeLists.txt) in build/bin_greet folder
add_subdirectory(../Greeting bin_greet)

add_library(living Living.cpp)
target_link_libraries(living greet)

# generate executable
#add_executable(living Living.cpp)
