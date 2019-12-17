############################################################################
# Copyright (c) 2018, Johan Mabille, Sylvain Corlay and Loic Gouarin       #
#                                                                          #
# Distributed under the terms of the BSD 3-Clause License.                 #
#                                                                          #
# The full license is in the file LICENSE, distributed with this software. #
############################################################################

import os
from setuptools import setup, find_packages

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: MacOS"
]

here = os.path.dirname(os.path.abspath(__file__))
version_ns = {}
with open(os.path.join(here, 'xhale', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup(
    name = "xhale",
    author = "loic.gouarin@gmail.com",
    description = "convert sphinx inventory file into a doxygen tag file",
    version = version_ns['__version__'],
    license = "BSD",
    classifiers = CLASSIFIERS,
    packages = find_packages(),
    install_requires = ["six", "sphinx"],
    entry_points={ 'console_scripts': [
        'xhale=xhale.xhale_cli:main',
        ],
    },
)
