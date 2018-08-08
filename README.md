# Super C++ project 

using dynamic librairies (.so)

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


## How to 

- create the lib dir
```
$ mkdir lib 
```

- run the make command 
```
$ make myapp
```
the Makefile will generate : 
libgreet.so (from Greeting folder)
liblive.so (from Living folder)
myapp (from MyApp folder)

- execute the app
```
$ LIBRARY_PATH=lib ./myapp
```

## TO DO
- complete makefile
