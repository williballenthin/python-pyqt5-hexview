#!/usr/bin/env python

# to upload to PyPi
# 
#    3  mkdir /tmp/env
#    4  virtualenv -p python3 /tmp/env
#    6  /tmp/env/bin/pip install twine
#    7  git clone https://github.com/williballenthin/python-pyqt5-hexview.git
#    8 cd python-pyqt5-hexview
#   12  /tmp/env/bin/pip install -r requirements.txt 
#   16  ln -s /usr/lib/python3/dist-packages/PyQt5 /tmp/env/lib/python3.4/site-packages/PyQt5
#   17  ln -s /usr/lib/python3/dist-packages/sip.cpython-34m-x86_64-linux-gnu.so /tmp/env/lib/python3.4/site-packages/sip.cpython-34m-x86_64-linux-gnu.so
#   18  /tmp/env/bin/pip install .
#   19  python setup.py sdist --formats=gztar,zip
#   23  vi setup.py --> update version
#   26  /tmp/env/bin/python setup.py sdist --formats=gztar,zip
#   27  /tmp/env/bin/twine upload dist/*
from setuptools import setup

description = "PyQt5 hex viewer widget."
setup(name="python-pyqt5-hexview",
      version="0.4.2",
      description=description,
      long_description=description,
      author="Willi Ballenthin",
      author_email="willi.ballenthin@gmail.com",
      url="https://github.com/williballenthin/python-pyqt5-hexview",
      license="Apache 2.0 License",
      install_requires=["hexdump", "intervaltree", "funcy"],
      packages=["hexview"],
      package_dir={"hexview": "hexview"},
      package_data={"hexview": ["hexview/hexview.ui"]},
      entry_points={
        "console_scripts": [
            "hexview=hexview.scripts.hexview_bin:main",
        ]
      },
)
