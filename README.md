# Super C++ project 

## Projects

- Greeting : basic C++ class 
- Living   : relies on Greeting project
- MyApp    : relies on Living project and generate exec 


## Pre requisite

- Download the following packages
```
sudo apt-get install build-essential cmake python-pip g++-multilib gcc-multilib git 
```

- Install Conan
```
pip install conan
```


## Main steps

- Generate greeting conan package
- Generate living conan package which consumes greeting conan package
- Generate the app which is consuming living conan package

## Important facts about Conan

- conanfile.txt = easy way to resolve conan packages (will also generate files for CMake to point to header files, libs from imported conan package)
- conanfile.py  = create and resolve conan packages

> DO NOT FORGET to modify the CMakeLists.txt to include CONAN LIBS
