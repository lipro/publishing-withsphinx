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

from tests.functional import fixtures

import re


class TestCaseSphinxExtAutoSummary(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_testroot_app(
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

        p = fixtures.path(app.outdir / 'autosummary.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'<tr class="row-odd"><td><a class="reference internal"') + '.*'
            + re.escape(r'an_example_pypi_project</tt></a></td>') + '.*'
            + re.escape(r'<td>A pypi demonstration vehicle.</td>') + '.*'
            + re.escape(r'<tr class="row-even"><td><a class="reference internal"') + '.*'
            + re.escape(r'an_example_pypi_project.useful_1</tt></a></td>') + '.*'
            + re.escape(r'<tr class="row-odd"><td><a class="reference internal"') + '.*'
            + re.escape(r'an_example_pypi_project.useful_2</tt></a></td>') + '.*'
            + re.escape(r'<td>A very useful module indeed.</td>')
        )
        self.assertRegex(c, r)

        p = fixtures.path(app.outdir / 'autosummary' / 'an_example_pypi_project.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'<tr class="row-odd"><td><tt class="') + '.*' + re.escape(r'">start</tt>()</td>') + '.*'
            + re.escape(r'<td>This starts this module running ...</td>')
        )
        self.assertRegex(c, r)

        p = fixtures.path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_1.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'<p class="rubric">Functions</p>') + '.*'
            + re.escape(r'<tr class="row-odd"><td><tt class="') + '.*'
            + re.escape(r'">public_fn_with_googley_docstring</tt>(name[,&nbsp;state])</td>') + '.*'
            + re.escape(r'<td>This function does something.</td>') + '.*'
            + re.escape(r'<tr class="row-even"><td><tt class="') + '.*'
            + re.escape(r'">public_fn_with_sphinxy_docstring</tt>(name[,&nbsp;state])</td>') + '.*'
            + re.escape(r'<td>This function does something.</td>') + '.*'
            + re.escape(r'<tr class="row-odd"><td><tt class="') + '.*'
            + re.escape(r'">public_fn_without_docstring</tt>()</td>') + '.*'
            + re.escape(r'<td></td>') + '.*' + re.escape(r'<p class="rubric">Classes</p>') + '.*'
            + re.escape(r'<tr class="row-odd"><td><tt class="') + '.*'
            + re.escape(r'">MyPublicClass</tt>(foo[,&nbsp;bar])</td>') + '.*'
            + re.escape(r'<td>We use this as a public class example class.</td>')
        )
        self.assertRegex(c, r)

        p = fixtures.path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_2.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'<p class="rubric">Functions</p>') + '.*'
            + re.escape(r'<tr class="row-odd"><td><tt class="') + '.*'
            + re.escape(r'">public_fn_with_googley_docstring</tt>(name[,&nbsp;state])</td>') + '.*'
            + re.escape(r'<td>This function does something.</td>') + '.*'
            + re.escape(r'<tr class="row-even"><td><tt class="') + '.*'
            + re.escape(r'">public_fn_with_sphinxy_docstring</tt>(name[,&nbsp;state])</td>') + '.*'
            + re.escape(r'<td>This function does something.</td>') + '.*'
            + re.escape(r'<tr class="row-odd"><td><tt class="') + '.*'
            + re.escape(r'">public_fn_without_docstring</tt>()</td>') + '.*'
            + re.escape(r'<td></td>') + '.*' + re.escape(r'<p class="rubric">Classes</p>') + '.*'
            + re.escape(r'<tr class="row-odd"><td><tt class="') + '.*'
            + re.escape(r'">MyPublicClass</tt>(foo[,&nbsp;bar])</td>') + '.*'
            + re.escape(r'<td>We use this as a public class example class.</td>')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
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

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(self.get_latex_code() + r'{an\_example\_pypi\_project}') + '.*'
            + re.escape(r'A pypi demonstration vehicle.') + '.*'
            + re.escape(self.get_latex_code() + r'{an\_example\_pypi\_project.useful\_1}') + '.*'
            + re.escape(self.get_latex_code() + r'{an\_example\_pypi\_project.useful\_2}') + '.*'
            + re.escape(r'A very useful module indeed.') + '.*'
            + re.escape(self.get_latex_code() + r'{start}()') + '.*'
            + re.escape(r'This starts this module running ...') + '.*'
            + re.escape(r'\section{an\_example\_pypi\_project.useful\_1}') + '.*'
            + re.escape(r'\paragraph{Functions}') + '.*'
            + re.escape(self.get_latex_code() + r'{public\_fn\_with\_googley\_docstring}(name{[}, state{]})') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(self.get_latex_code() + r'{public\_fn\_with\_sphinxy\_docstring}(name{[}, state{]})') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(self.get_latex_code() + r'{public\_fn\_without\_docstring}()') + '.*'
            + re.escape(r'\paragraph{Classes}') + '.*'
            + re.escape(self.get_latex_code() + r'{MyPublicClass}(foo{[}, bar{]})') + '.*'
            + re.escape(r'We use this as a public class example class.') + '.*'
            + re.escape(r'\section{an\_example\_pypi\_project.useful\_2}') + '.*'
            + re.escape(r'\paragraph{Functions}') + '.*'
            + re.escape(self.get_latex_code() + r'{public\_fn\_with\_googley\_docstring}(name{[}, state{]})') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(self.get_latex_code() + r'{public\_fn\_with\_sphinxy\_docstring}(name{[}, state{]})') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(self.get_latex_code() + r'{public\_fn\_without\_docstring}()') + '.*'
            + re.escape(r'\paragraph{Classes}') + '.*'
            + re.escape(self.get_latex_code() + r'{MyPublicClass}(foo{[}, bar{]})') + '.*'
            + re.escape(r'We use this as a public class example class.')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
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

        p = fixtures.path(app.outdir / 'autosummary.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'A pypi demonstration vehicle.') + '.*'
            + re.escape(r'A very useful module indeed.') + '.*'
            + re.escape(r'an_example_pypi_project') + '.*'
            + re.escape(r'an_example_pypi_project.useful_1') + '.*'
            + re.escape(r'an_example_pypi_project.useful_2')
        )
        self.assertRegex(c, r)

        p = fixtures.path(app.outdir / 'autosummary' / 'an_example_pypi_project.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'-[ Functions ]-') + '.*'
            + re.escape(r'"start"()') + '.*'
            + re.escape(r'This starts this module running ...')
        )
        self.assertRegex(c, r)

        p = fixtures.path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_1.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'-[ Functions ]-') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(r'-[ Classes ]-') + '.*'
            + re.escape(r'We use this as a public class example class.')
        )
        self.assertRegex(c, r)

        p = fixtures.path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_2.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'-[ Functions ]-') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(r'-[ Classes ]-') + '.*'
            + re.escape(r'We use this as a public class example class.')
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
