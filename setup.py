#!/usr/bin/env python

from hexview import __version__
from setuptools import setup


description = "PyQt5 hex viewer widget."
setup(name="python-pyqt5-hexview",
      version=__version__,
      description=description,
      long_description=description,
      author="Willi Ballenthin",
      author_email="willi.ballenthin@gmail.com",
      url="https://github.com/williballenthin/python-pyqt5-hexview",
      license="Apache 2.0 License",
      install_depends=["hexdump"],
      packages=["hexview"],
      package_dir={"hexview": "hexview"},
      package_data={"hexview": ["hexview.ui"]})
