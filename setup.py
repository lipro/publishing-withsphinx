# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Stephan Linz
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

'''
A setuptools based setup module.

See:
    https://packaging.python.org/
    https://packaging.python.org/distributing/
    https://pythonhosted.org/setuptools/
    https://github.com/pypa/sampleproject
'''

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Command
from os import system

# To use a consistent encoding
from codecs import open
from os import path

# To enforce right Python version
from sys import version_info

# To use the module meta data (version, author, ...)
import publishing.withsphinx as pubwsphinx

_INSTALL_REQUIRES = [
    'Sphinx>=1.2.0,<=1.4.9999',
    'sphinx-argparse>=0.1.15,<=0.1.15',
    'sphinxcontrib-ansi>=0.6.dev0',
    'sphinxcontrib-bibtex>=0.3.4,<=0.3.4',
    'sphinxcontrib-blockdiag>=1.5.5,<=1.5.5',
    'sphinxcontrib-email>=0.2.dev0',
    'sphinxcontrib-embedly>=0.2.0,<=0.2.0',
    'sphinxcontrib-inlinesyntaxhighlight>=0.2.0,<=0.2.0',
    'sphinxcontrib-programoutput>=0.8.0,<=0.8.0',
    'sphinxcontrib-spelling>=2.2.0,<=2.2.0',
    'sphinxcontrib-tikz>=0.4.2,<=0.4.2',
    'reportlab>=3.3.0,<=3.3.9999',
]

_DEPENDENCY_LINKS = [
    'hg+https://bitbucket.org/rexut/sphinx-contrib@default#subdirectory=ansi&egg=sphinxcontrib-ansi-0.6.dev0',
    'hg+https://bitbucket.org/rexut/sphinx-contrib@default#subdirectory=email&egg=sphinxcontrib-email-0.2.dev0',
    'git+https://github.com/rexut/sphinxcontrib-traceables.git@py2to3-devel#egg=sphinxcontrib-traceables-0.1.5.dev0',
]

_EXTRAS_REQUIRE_DEV = [
    'sphinxcontrib-traceables>=0.1.5.dev0',
    'sphinxcontrib-traceability>=0.1.2,<=0.1.2',
    'sphinx-rtd-theme>=0.1.6,<=0.1.9',
    'check-manifest>=0.34.0,<=0.34.9999',
    'webob>=1.6.2,<=1.6.2',
    'wheel>=0.29.0,<=0.29.0',
]

_EXTRAS_REQUIRE_TEST = [
    'sphinx-testing>=0.5.2,<=0.7.1',
    'tox>=2.0.0,<=2.4.1',
    'nose>=1.3.7,<=1.3.7',
    'mock>=2.0.0,<=2.0.0',
    'coverage>=4.2.0,<=4.2.9999',
    'coveralls>=1.1.0,<=1.1.9999',
    'flake8>=3.0.4,<=3.0.4',
]

_EXTRAS_REQUIRE = {
    'dev': _EXTRAS_REQUIRE_DEV,
    'test': _EXTRAS_REQUIRE_TEST,
}

# Check and respect diferent Python versions
if version_info < (2, 7):
    exit('Sorry, Python 2 older than 2.7 is not supported')
elif version_info >= (3, 0) and version_info <= (3, 2):
    exit('Sorry, Python 3 older than 3.3 is not supported')

if version_info < (3, 0):
    _INSTALL_REQUIRES.append('sphinxcontrib-autoprogram>=0.1.2,<=0.1.2')
else:
    _INSTALL_REQUIRES.append('sphinxcontrib-autoprogram>=0.1.2,<=0.1.3')

# Get project path absolut
_HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(_HERE, 'README.rst'), encoding='utf-8') as f:
    _README = f.read()


# clean command within setup.py by jathanism
# See: http://stackoverflow.com/questions/3779915/
class clean(Command):
    '''Custom clean command to tidy up the project root.'''
    description = "tidy up the project root"
    user_options = []

    def initialize_options(self):
        '''init options'''
        pass

    def finalize_options(self):
        '''finalize options'''
        pass

    def run(self):
        '''runner'''
        system('rm -vrf ./_build ./_dist ./*.egg-info')


setup(
    name='publishing-withsphinx',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=pubwsphinx.__version__,

    # Author details
    author=pubwsphinx.__author__,
    author_email=pubwsphinx.__author_email__,

    # Package descriptions
    description='Sphinx extension to help document publishing',
    long_description=_README,

    # The project's main homepage.
    url='https://github.com/lipro/publishing-withsphinx',
    download_url='http://pypi.python.org/pypi/publishing-withsphinx',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',

        # Indicate who your project is intended for
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities',
    ],

    # What does your project relate to?
    keywords=[
        'publishing',
        'sphinx',
    ],

    # Prevent ZIP archive creation
    zip_safe=False,

    # Sort in as "publishing" namespace package -- Python does not normally allow
    # the contents of a package to be retrieved from more than one location.
    # Namespace packages are a solution for this problem.
    # Details, see: https://pythonhosted.org/setuptools/
    # --> "Building and Distributing Packages with Setuptools"
    #     --> "Namespace Packages"
    namespace_packages=['publishing'],

    # This package should work on any platforms that will be supported by Python
    platforms='any',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['docs', 'tests']),

    # Tells setuptools to look for a MANIFEST.in file and install all the
    # entries that match as package data
    include_package_data=True,

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     # Any package contains LICENSE, *.txt or *.rst files, include them:
    #     '': ['AUTHORS', 'LICENSE', 'README.rst', 'TODO', 'CHANGES'],
    #     # And include any *.svg files found in the 'publishing-withsphinx' package, too:
    #     # 'publishing-withsphinx': ['*.svg'],
    # },

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=_INSTALL_REQUIRES,
    dependency_links=_DEPENDENCY_LINKS,

    test_suite='nose.collector',
    tests_require=_EXTRAS_REQUIRE_TEST,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require=_EXTRAS_REQUIRE,

    # ... Other setup options
    cmdclass={
        'clean': clean,
    }
)
