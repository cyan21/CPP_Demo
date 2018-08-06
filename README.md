# Super C++ project 

## Projects

- Greeting : basic C++ class 
- Living   : relies on Greeting project
- MyApp    : relies on Living project and generate exec 


## How to build

- Build Myapp Project  
```

$ cd MyApp 
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build . 
```

- Execute application

in Myapp/build:

```
$ ./myapp
```

> You can also generate an executable for Greeting and Living projects, see the README in each folder
