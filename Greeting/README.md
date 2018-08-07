# Greeting project

## How to generate the Conan package 

```
$ mkdir build && cd build
$ cmake .. -DCMAKE_BUILD_TYPE=Release && cmake --build . --config Release
$ conan export-pkg .. greeting/0.1@yann/test
```
> conanfile.py  was generated through 'conan new greeting/0.1@yann/test' and then customized

## How to test the Conan package 


in the CMakeLists.txt, comment out "add_library" and uncomment add_executable with the target_link

```
$ cd build
$ rm -rf * && cmake .. -DCMAKE_BUILD_TYPE=Release && cmake --build . --config Release
$ ./bin/greet
```


