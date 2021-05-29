from conans import ConanFile, CMake, tools


class LivingConan(ConanFile):
    name = "living"
#    version = "0.1"
    license = "Apache-2.0"
    author = "cyan21 <yann.chaysinh@gmail.com>"
    url = "https://github.com/cyan21/CPP_Demo.git"
    description = "living package"
    topics = ("demo", "yann")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    requires = "greeting/0.1@yann/test"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
            
    def source(self):
        self.run("git clone https://github.com/cyan21/CPP_Demo.git")
        self.run("cd CPP_Demo/Living && git checkout conan")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_folder + "/CPP_Demo/Living/")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*Living.h", dst="include", keep_path=False)
        self.copy("*living.lib", dst="lib", keep_path=False)
        self.copy("*living.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["living"]

