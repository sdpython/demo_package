# -*- coding: utf-8 -*-
import os
from distutils.core import setup
from setuptools import find_packages

here = os.path.dirname(__file__)
if here == "":
    here = '.'
packages = find_packages(where=here)
package_dir = {k: os.path.join(here, k.replace(".", "/")) for k in packages}

with open(os.path.join(here, "requirements.txt"), "r") as f:
    requirements = f.read().split("\n")

setup(name='demo_package',
      version='0.1',
      description="Package to demo",
      long_description="Depends on the demo",
      author='Xavier Dupré',
      author_email='xavier.dupre@gmail.com',
      url='https://github.com/sdpython/demo_package',
      packages=packages,
      package_dir=package_dir)
