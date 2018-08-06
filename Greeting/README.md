# Greeting project

## How to build

- Uncomment the main method in Greeting.cpp

- in the CMakeLists.txt, comment out "add_library" and uncomment add_executable

- Generate exec 
```
$ cd Greeting
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build .
```

- Execution
```
$ ./greet
```
