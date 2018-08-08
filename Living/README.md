# Living project

## How to generate a conan package from scratch 

- Get the conanfile.py (recipe) from this folder and use the 'conan create' command to generate the package from the source

> the create command will build the package from the source code fetched from my github repo and will download the greeting package at the same time

```
$ mkdir living_conan && cd living_conan
$ conan create . living/0.1@yann/test
```
> conanfile.py  was generated through 'conan new living/0.1@yann/test' and then customized


## How to generate a conan package from pre-built binaries

TO DO


## How to test the code  

in the CMakeLists.txt, comment out "add_library" and uncomment add_executable with the target_link

```
$ cd build
$ rm -rf * && conan install .. && cmake .. -DCMAKE_BUILD_TYPE=Release && cmake --build . --config Release
$ ./bin/livingApp
```

## How to test the conan package 

TO DO 

