from conans import ConanFile, CMake, tools


class GreetingConan(ConanFile):
    name = "greeting"
    version = "0.1"
    license = "Apache-2.0"
    url = "https://github.com/cyan21/CPP_Demo.git"
    description = "greeting package"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/cyan21/CPP_Demo.git")
        self.run("cd CPP_Demo/Greeting && git checkout conan")
#        print "source repo : " + self.source_folder
#        self.run("cp * %s" % self.source_folder)

        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
#        tools.replace_in_file("CPP_Demo/Greeting/CMakeLists.txt", "project(Greeting)",
#                              '''project(Greeting)
#				include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#				conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
	# source folder not mandatory if CMake file is on the root
        # cmake.configure()
        cmake.configure(source_folder=self.source_folder + "/CPP_Demo/Greeting/")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*greet.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["greet"]

