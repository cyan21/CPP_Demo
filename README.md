# Super C++ project 

## Projects

- Greeting : basic C++ class 
- Living   : relies on Greeting project
- MyApp    : relies on Living project and generate exec 


## Main steps

- Generate greeting conan package
- Generate living conan package which consumes greeting conan package
- Generate the app which is consuming living conan package

> conanfile.txt = resolve conan packages + generate files for CMake (to point to header files, libs from imported conan package)
> conanfile.py  = create conan package
> DO NOT FORGET to modify the CMakeLists.txt to include CONAN LIBS
