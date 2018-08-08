from conans import ConanFile, CMake, tools


class LivingConan(ConanFile):
    name = "living"
    version = "0.1"
    license = "Apache-2.0"
    url = "https://github.com/cyan21/CPP_Demo.git"
    description = "living package"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "greeting/0.1@yann/test"

    def source(self):
        self.run("git clone https://github.com/cyan21/CPP_Demo.git")
        self.run("cd CPP_Demo/Living && git checkout conan")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="CPP_Demo/Living")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="CPP_Demo/Living/")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["living"]

