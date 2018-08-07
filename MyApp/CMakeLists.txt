project(MyApp)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# generate myapp
add_executable(myapp main.cpp)
target_link_libraries(myapp ${CONAN_LIBS})

