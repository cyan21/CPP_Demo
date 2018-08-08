# MyApp project

## How to generate app 

- Build the application

```
$ mkdir build && cd build

// this will fetch the living package and also the greeting package
$ conan install ..
$ cmake .. &&  cmake --build . 
```

- Execute the application

```
$ ./bin/myapp
```
