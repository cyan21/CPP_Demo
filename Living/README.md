# Living project

## How to build

- Uncomment the main method in Living.cpp

- in the CMakeLists.txt, comment out "add_library" and uncomment add_executable

- Generate exec 
```
$ cd Living
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build .
```

- Execution
```
$ ./living
```
