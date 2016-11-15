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
publishing.withsphinx.required
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module loads all required |Sphinx| extensions as needed by the
extended publishing support for the |Sphinx_dsc|.
'''

from __future__ import absolute_import

_REQUIRED = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.extlinks',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinxarg.ext',
    'sphinxcontrib.ansi',
    'sphinxcontrib.autoprogram',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.email',
    'sphinxcontrib.embedly',
    'sphinxcontrib.inlinesyntaxhighlight',
    'sphinxcontrib.programoutput',
    'sphinxcontrib.spelling',
    'sphinxcontrib.tikz',
]
'''List of all required |Sphinx| extensions.'''


def extensions(app):
    '''
    Load all required |Sphinx| extensions as needed by the
    :data:`publishing.withsphinx` extension.

    :param app: |Sphinx| application instance, representing the Sphinx process.
    :type app: class sphinx.application.Sphinx

    :returns: Nothing.
    :rtype: NoneType
    '''

    for ext in _REQUIRED:
        app.setup_extension(ext)
