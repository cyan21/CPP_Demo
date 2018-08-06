project(MyApp)
cmake_minimum_required(VERSION 2.8.12)

# import Living folder (should contain CMakeLists.txt) in build/bin_liv folder
add_subdirectory(../Living bin_liv)

# generate myapp
add_executable(myapp main.cpp)

# link libliving.a (in bin_liv folder) to myapp
target_link_libraries(myapp living)

# generate executable relying only on source code (no libs)
#add_executable(myapp ../../Living/Living.cpp ../../Greeting/Greeting.cpp ../main.cpp)
