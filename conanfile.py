#!/usr/bin/env python
from conans import ConanFile, CMake, tools
import shutil
import os

class CxxoptsConan(ConanFile):
    name = "cxxopts"
    version = "2.2.0_src"
    license = "MIT"
    author = "Ruisheng Wang (ruisheng.wang@outlook.com)"
    url = "https://github.com/darcamo/conan-cxxopts"
    description = "Lightweight C++ command line option parser."
    homepage = "https://github.com/jarro2783/cxxopts"
    exports = "file.patch"
    _source_subfolder = "source_subfolder"
    exports_sources = os.path.join(_source_subfolder, '*')

    def _source(self):
        tools.get("https://github.com/jarro2783/cxxopts/archive/v{}.zip".format(self.version))
        shutil.move("cxxopts-{}/".format(self.version), self._source_subfolder)
        tools.patch(base_path=self._source_subfolder, patch_file="file.patch")

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.install()

    def package_id(self):
        self.info.header_only()
