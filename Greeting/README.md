# Greeting project

## How to generate a conan package from scratch 

- Get the conanfile.py (recipe) from this folder and use the 'conan create' command to generate the package from the source

> the create command will build the package from the source code fetched from my github repo

```
$ mkdir greeting_conan && cd greeting_conan
$ conan create . greeting/0.1@yann/test
```
> conanfile.py  was generated through 'conan new greeting/0.1@yann/test' and then customized


## How to generate a conan package from pre-built binaries

TO DO 


## How to test the code  

in the CMakeLists.txt, comment out "add_library" and uncomment add_executable with the target_link

```
$ mkdir build && cd build
$ rm -rf * && cmake .. -DCMAKE_BUILD_TYPE=Release && cmake --build . --config Release
$ ./bin/greet
```

## How to test the conan package 

TO DO 
