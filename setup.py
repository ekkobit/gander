import setuptools
from gander import __version__, __authors__, __email__


def readme():
    with open('README.rst') as f:
        return f.read()


def license():
    with open('LICENSE') as f:
        return f.read()


setuptools.setup(name='gander',
                 version=__version__,
                 description='Technical indicators for the stock market',
                 long_description=readme(),
                 long_description_content_type="text/x-rst",
                 classifiers=[
                        'Development Status :: 3 - Alpha',
                        'License :: OSI Approved :: MIT License',
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
