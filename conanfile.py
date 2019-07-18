#!/usr/bin/env python
from conans import ConanFile, CMake, tools
import shutil

class CxxoptsConan(ConanFile):
    name = "cxxopts"
    version = "2.2.0"
    license = "MIT"
    author = "Ruisheng Wang (ruisheng.wang@outlook.com)"
    url = "https://github.com/darcamo/conan-cxxopts"
    description = "Lightweight C++ command line option parser."
    homepage = "https://github.com/jarro2783/cxxopts"
    source_subfolder = "source_subfolder"
    exports = "file.patch"

    def source(self):
        tools.get("https://github.com/jarro2783/cxxopts/archive/v{}.zip".format(self.version))
        shutil.move("cxxopts-{}/".format(self.version), self.source_subfolder)
        tools.patch(base_path=self.source_subfolder, patch_file="file.patch")

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder)
        cmake.install()

    def package_id(self):
        self.info.header_only()
