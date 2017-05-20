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
publishing.withsphinx
~~~~~~~~~~~~~~~~~~~~~

This module provides the extended publishing support for the |Sphinx_dsc|.
'''

from __future__ import absolute_import

import types

__author__ = 'Stephan Linz'
__author_email__ = 'linz@li-pro.net'
__date__ = '2016-10-11'
__version__ = '0.0.1'


def setup(app):
    '''
    Set up :data:`publishing.withsphinx` extension and register it with |Sphinx|

    :param app: |Sphinx| application instance, representing the Sphinx process.
    :type app: class sphinx.application.Sphinx

    :returns: Return a dictionary, that is treated by Sphinx as metadata of the
              extension.
    :rtype: Dictionary
    '''

    # Import package modules here to avoid errors from setuptools when the
    # package will be load to fetch meta data (version, author, ...).
    from . import backports
    from . import required

    if isinstance(app, types.ModuleType):
        return

    # Load all required backports
    backports.sphinx15(app)

    # Load all required extensions
    required.extensions(app)

    # Return a dictionary, that is treated by Sphinx as metadata of the extension.
    return {
        # it is used for extension version requirement checking (needs_extensions)
        'version': __version__,
        # parallel reading of source files when the extension is loaded
        'parallel_read_safe': True,
        # parallel writing of output files when the extension is loaded
        'parallel_write_safe': True,
    }
