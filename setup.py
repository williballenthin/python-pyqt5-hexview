#!/usr/bin/env python

from setuptools import setup


description = "PyQt5 hex viewer widget."
setup(name="python-pyqt5-hexview",
      version="0.3.3",
      description=description,
      long_description=description,
      author="Willi Ballenthin",
      author_email="willi.ballenthin@gmail.com",
      url="https://github.com/williballenthin/python-pyqt5-hexview",
      license="Apache 2.0 License",
      install_requires=["hexdump", "intervaltree", "funcy"],
      packages=["hexview"],
      package_dir={"hexview": "hexview"},
      package_data={"hexview": ["hexview.ui"]})
