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
# How to write tests: http://docs.python-guide.org/en/latest/writing/tests/
#

'''
test_sphinx_ext_autodoc
~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinx.ext.autodoc extension
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

import re
from tests import util


class TestCaseSphinxExtAutoDoc(util.TestCasePublishingSphinx):

    @util.with_html_app(
        testroot='ext-autodoc',
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.autodoc: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' 'A pypi demonstration vehicle\.'
            '.*'    '<em.*>class </em>'
            '.*'    '<(code|tt).*>an_example_pypi_project\.useful_1\.</(code|tt)>'
            '.*'    '<(code|tt).*>MyPublicClass<\/(code|tt)>'
            '.*'    '\(.*<em>foo</em>, <em>bar=\'baz\'</em>.*\)'
            '.*'    '<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
            '.*'    '<(code|tt).*>public_fn_with_googley_docstring<\/(code|tt)>'
            '.*'    '\(.*<em>name</em>, <em>state=None</em>.*\)'
            '.*'    '<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
            '.*'    '<(code|tt).*>public_fn_with_sphinxy_docstring<\/(code|tt)>'
            '.*'    '\(.*<em>name</em>, <em>state=None</em>.*\)'
            '.*'    'A very useful module indeed\.'
            '.*'    '<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
            '.*'    '<(code|tt).*>public_fn_with_sphinxy_docstring<\/(code|tt)>'
            '.*'    '\(.*<em>name</em>, <em>state=None</em>.*\)'
            '.*'    '<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
            '.*'    '<(code|tt).*>_private_fn_with_docstring<\/(code|tt)>'
            '.*'    '\(.*<em>foo</em>, <em>bar=\'baz\'</em>, <em>foobarbas=None</em>.*\)'
            '.*'    '<em.*>class </em>'
            '.*'    '<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
            '.*'    '<(code|tt).*>MyPublicClass<\/(code|tt)>'
            '.*'    '\(.*<em>foo</em>, <em>bar=\'baz\'</em>.*\)'
        )
        self.assertRegex(c, r)

    @util.with_latex_app(
        testroot='ext-autodoc',
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.autodoc: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' 'A pypi demonstration vehicle\.'
            '.*'    'A very useful module indeed\.'
        )
        self.assertRegex(c, r)

    @util.with_text_app(
        testroot='ext-autodoc',
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.autodoc: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' 'A pypi demonstration vehicle\.'
            '.*'    'class an_example_pypi_project\.useful_1\.MyPublicClass\(foo, bar=\'baz\'\)'
            '.*'    'an_example_pypi_project\.useful_1\.public_fn_with_googley_docstring\(name, state=None\)'
            '.*'    'an_example_pypi_project\.useful_1\.public_fn_with_sphinxy_docstring\(name, state=None\)'
            '.*'    'A very useful module indeed\.'
            '.*'    'an_example_pypi_project\.useful_2\.public_fn_with_sphinxy_docstring\(name, state=None\)'
            '.*'    'an_example_pypi_project\.useful_2\._private_fn_with_docstring\(foo, bar=\'baz\', foobarbas=None\)'
            '.*'    'class an_example_pypi_project\.useful_2\.MyPublicClass\(foo, bar=\'baz\'\)'
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    util.main()
