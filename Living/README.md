# Living project

## How to generate the Conan package 

- Download the greeting package (conanfile.py)
```
$ mkdir build && cd build
$ conan install ..
```
> this will also generate : conanbuildinfo.cmake, conanbuildinfo.txt, conaninfo.txt
> these files will be used to compile and link the Living project (see CMakeLists.txt)


- Compile and link the project
```
$ cmake .. -DCMAKE_BUILD_TYPE=Release && cmake --build . --config Release
```

- Create the living package (require the conanfile.py)
```
$ conan export-pkg .. living/0.1@yann/test
```
> conanfile.py  was generated through 'conan new greeting/0.1@yann/test' and then customized


## How to test the Conan package 

in the CMakeLists.txt, comment out "add_library" and uncomment add_executable with the target_link

```
$ cd build
$ rm -rf * && conan install .. && cmake .. -DCMAKE_BUILD_TYPE=Release && cmake --build . --config Release
$ ./bin/livingApp
```
