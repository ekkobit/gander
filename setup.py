"""Setup for project Gander.

Copyright (C) 2020  Ekkobit AS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Questions may be directed to resonate@ekkobit.com
"""

import setuptools
from gander import __version__, __authors__, __email__


def readme():
    """Open and read README.rst into memory."""
    with open('README.rst') as f:
        return f.read()


def license():
    """Open and read COPYING into memory."""
    with open('COPYING') as f:
        return f.read()


setuptools.setup(name='gander',
                 version=__version__,
                 description='Technical indicators for the stock market',
                 long_description=readme(),
                 long_description_content_type="text/x-rst",
                 classifiers=[
                        'Development Status :: 3 - Alpha',
                        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                        'Programming Language :: Python :: 3',
                        'Topic :: Office/Business :: Financial :: Investment',
                        ],
                 url='http://github.com/ekkobit/gander',
                 author=__authors__,
                 author_email=__email__,
                 license='MIT',
                 license_file=license(),
                 packages=setuptools.find_packages(),
                 test_suite='nose.collector',
                 tests_require=['pytest'],
                 install_requires=[
                        'pandas',
                        'numpy',
                        'matplotlib'
                        ],
                 include_package_data=True,
                 )
