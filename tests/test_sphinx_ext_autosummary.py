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
test_sphinx_ext_autosummary
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinx.ext.autosummary
extension as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

import re
from tests import util


class TestCaseSphinxExtAutoSummary(util.TestCasePublishingSphinx):

    @util.with_testroot_app(
        testroot='ext-autosummary',
        confoverrides={
            'autosummary_generate': True,
        },
        buildername='html',  # TODO: add support for singlehtml backend of this extention
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.autosummary: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'autosummary.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' 'an_example_pypi_project'
            '.*'    'A pypi demonstration vehicle\.'
            '.*'    'an_example_pypi_project\.useful_1'
            '.*'    'an_example_pypi_project\.useful_2'
            '.*'    'A very useful module indeed\.'
        )
        self.assertRegex(c, r)

        p = util.path(app.outdir / 'autosummary' / 'an_example_pypi_project.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' 'This starts this module running \.\.\.'
        )
        self.assertRegex(c, r)

        p = util.path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_1.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' 'Functions'
            '.*'    'public_fn_with_googley_docstring'
            '.*'    'This function does something\.'
            '.*'    'public_fn_with_sphinxy_docstring'
            '.*'    'This function does something\.'
            '.*'    'public_fn_without_docstring'
            '.*'    'Classes'
            '.*'    'MyPublicClass'
            '.*'    'We use this as a public class example class\.'
        )
        self.assertRegex(c, r)

        p = util.path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_2.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' 'Functions'
            '.*'    'public_fn_with_googley_docstring'
            '.*'    'This function does something\.'
            '.*'    'public_fn_with_sphinxy_docstring'
            '.*'    'This function does something\.'
            '.*'    'public_fn_without_docstring'
            '.*'    'Classes'
            '.*'    'MyPublicClass'
            '.*'    'We use this as a public class example class\.'
        )
        self.assertRegex(c, r)

    @util.with_latex_app(
        testroot='ext-autosummary',
        confoverrides={
            'autosummary_generate': True,
        },
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.autosummary: can build latex
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
            '.*'    'This starts this module running \.\.\.'
            '.*'    'This function does something\.'
            '.*'    'This function does something\.'
            '.*'    'This function does something\.'
            '.*'    'This function does something\.'
        )
        self.assertRegex(c, r)

    @util.with_text_app(
        testroot='ext-autosummary',
        confoverrides={
            'autosummary_generate': True,
        },
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.autosummary: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'autosummary.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' 'A pypi demonstration vehicle\.'
            '.*'    'A very useful module indeed\.'
            '.*'    'an_example_pypi_project'
            '.*'    'an_example_pypi_project\.useful_1'
            '.*'    'an_example_pypi_project\.useful_2'
        )
        self.assertRegex(c, r)

        p = util.path(app.outdir / 'autosummary' / 'an_example_pypi_project.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' 'This starts this module running \.\.\.'
        )
        self.assertRegex(c, r)

        p = util.path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_1.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' '-\[ Functions \]-'
            '.*'    'This function does something\.'
            '.*'    'This function does something\.'
            '.*'    '-\[ Classes \]-'
            '.*'    'We use this as a public class example class\.'
        )
        self.assertRegex(c, r)

        p = util.path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_2.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)' '-\[ Functions \]-'
            '.*'    'This function does something\.'
            '.*'    'This function does something\.'
            '.*'    '-\[ Classes \]-'
            '.*'    'We use this as a public class example class\.'
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    util.main()
