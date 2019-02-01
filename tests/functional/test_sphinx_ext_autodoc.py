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

from tests.functional import fixtures

import re


class TestCaseSphinxExtAutoDoc(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_html_app(
        testroot='ext-autodoc',
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.autodoc: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'<p>A pypi demonstration vehicle.</p>') + '.*'
            + re.escape(r'<p>This is something I want to say that is not in the docstring.</p>') + '.*'
            + re.escape(r'<em class="property">class </em>')
            + re.escape(self.get_html_code(args=' class="descclassname"'))
            + re.escape(r'an_example_pypi_project.useful_1.') + re.escape(self.get_html_code(close=True))
            + re.escape(self.get_html_code(args=' class="descname"')) + re.escape(r'MyPublicClass')
            + re.escape(self.get_html_code(close=True)) + '.*'
            + re.escape(r"<em>foo</em>, <em>bar='baz'</em>") + '.*'
            + re.escape(r'<p>We use this as a public class example class.</p>') + '.*'
            + re.escape(self.get_html_code(args=' class="descname"')) + re.escape(r'get_foobar')
            + re.escape(self.get_html_code(close=True)) + '.*' + re.escape(r'<em>foo</em>, <em>bar=True</em>') + '.*'
            + re.escape(r'<p>This gets the foobar</p>') + '.*'
            + re.escape(r'<p>This really should have a full function definition, but I am too lazy.</p>') + '.*'
            + re.escape(self.get_html_code(args=' class="descclassname"'))
            + re.escape(r'an_example_pypi_project.useful_1.') + re.escape(self.get_html_code(close=True))
            + re.escape(self.get_html_code(args=' class="descname"')) + re.escape(r'public_fn_with_googley_docstring')
            + re.escape(self.get_html_code(close=True)) + '.*'
            + re.escape(r'<em>name</em>, <em>state=None</em>') + '.*'
            + re.escape(r'<p>This function does something.</p>') + '.*'
            + re.escape(self.get_html_code(args=' class="descclassname"'))
            + re.escape(r'an_example_pypi_project.useful_1.') + re.escape(self.get_html_code(close=True))
            + re.escape(self.get_html_code(args=' class="descname"')) + re.escape(r'public_fn_with_sphinxy_docstring')
            + re.escape(self.get_html_code(close=True)) + '.*'
            + re.escape(r'<em>name</em>, <em>state=None</em>') + '.*'
            + re.escape(r'<p>This function does something.</p>') + '.*'
            + re.escape(r'<p>This is something I want to say that is not in the docstring.</p>') + '.*'
            + re.escape(r'<p>A very useful module indeed.</p>') + '.*'
            + re.escape(self.get_html_code(args=' class="descclassname"'))
            + re.escape(r'an_example_pypi_project.useful_2.') + re.escape(self.get_html_code(close=True))
            + re.escape(self.get_html_code(args=' class="descname"')) + re.escape(r'public_fn_with_sphinxy_docstring')
            + re.escape(self.get_html_code(close=True)) + '.*'
            + re.escape(r'<em>name</em>, <em>state=None</em>') + '.*'
            + re.escape(r'<p>This function does something.</p>') + '.*'
            + re.escape(self.get_html_code(args=' class="descclassname"'))
            + re.escape(r'an_example_pypi_project.useful_2.') + re.escape(self.get_html_code(close=True))
            + re.escape(self.get_html_code(args=' class="descname"')) + re.escape(r'_private_fn_with_docstring')
            + re.escape(self.get_html_code(close=True)) + '.*'
            + re.escape(r"<em>foo</em>, <em>bar='baz'</em>, <em>foobarbas=None</em>") + '.*'
            + re.escape(r'<p>I have a docstring, but ') + '.*' + re.escape(r'</p>') + '.*'
            + re.escape(r'<em class="property">class </em>')
            + re.escape(self.get_html_code(args=' class="descclassname"'))
            + re.escape(r'an_example_pypi_project.useful_2.') + re.escape(self.get_html_code(close=True))
            + re.escape(self.get_html_code(args=' class="descname"')) + re.escape(r'MyPublicClass')
            + re.escape(self.get_html_code(close=True)) + '.*'
            + re.escape(r"<em>foo</em>, <em>bar='baz'</em>") + '.*'
            + re.escape(r'<p>We use this as a public class example class.</p>') + '.*'
            + re.escape(self.get_html_code(args=' class="descname"')) + re.escape(r'_get_baz')
            + re.escape(self.get_html_code(close=True)) + '.*' + re.escape(r'<em>baz=None</em>') + '.*'
            + re.escape(r'<p>A private function to get baz.</p>') + '.*'
            + re.escape(r'<p>This really should have a full function definition, but I am too lazy.</p>') + '.*'
            + re.escape(self.get_html_code(args=' class="descname"')) + re.escape(r'get_foobar')
            + re.escape(self.get_html_code(close=True)) + '.*' + re.escape(r'<em>foo</em>, <em>bar=True</em>') + '.*'
            + re.escape(r'<p>This gets the foobar</p>') + '.*'
            + re.escape(r'<p>This really should have a full function definition, but I am too lazy.</p>')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
        testroot='ext-autodoc',
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.autodoc: can build latex
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
            + re.escape(r'A pypi demonstration vehicle.') + '.*'
            + re.escape(r'This is something I want to say that is not in the docstring.') + '.*'
            + re.escape(self.get_latex_strong() + r'{class }')
            + re.escape(self.get_latex_code() + r'{an\_example\_pypi\_project.useful\_1.}')
            + re.escape(self.get_latex_bfcode() + r'{MyPublicClass}') + '.*'
            + re.escape(r"{\emph{foo}, \emph{bar='baz'}}") + '.*'
            + re.escape(r'We use this as a public class example class.') + '.*'
            + re.escape(self.get_latex_bfcode() + r'{get\_foobar}') + '.*'
            + re.escape(r'{\emph{foo}, \emph{bar=True}}') + '.*'
            + re.escape(r'This gets the foobar') + '.*'
            + re.escape(r'This really should have a full function definition, but I am too lazy.') + '.*'
            + re.escape(self.get_latex_code() + r'{an\_example\_pypi\_project.useful\_1.}')
            + re.escape(self.get_latex_bfcode() + r'{public\_fn\_with\_googley\_docstring}') + '.*'
            + re.escape(r'{\emph{name}, \emph{state=None}}') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(self.get_latex_code() + r'{an\_example\_pypi\_project.useful\_1.}')
            + re.escape(self.get_latex_bfcode() + r'{public\_fn\_with\_sphinxy\_docstring}') + '.*'
            + re.escape(r'{\emph{name}, \emph{state=None}}') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(r'This is something I want to say that is not in the docstring.') + '.*'
            + re.escape(r'A very useful module indeed.') + '.*'
            + re.escape(self.get_latex_code() + r'{an\_example\_pypi\_project.useful\_2.}')
            + re.escape(self.get_latex_bfcode() + r'{public\_fn\_with\_sphinxy\_docstring}') + '.*'
            + re.escape(r'{\emph{name}, \emph{state=None}}') + '.*'
            + re.escape(r'This function does something.') + '.*'
            + re.escape(self.get_latex_code() + r'{an\_example\_pypi\_project.useful\_2.}')
            + re.escape(self.get_latex_bfcode() + r'{\_private\_fn\_with\_docstring}') + '.*'
            + re.escape(r"{\emph{foo}, \emph{bar='baz'}, \emph{foobarbas=None}}") + '.*'
            + re.escape(r'I have a docstring, but ') + '.*'
            + re.escape(self.get_latex_strong() + r'{class }')
            + re.escape(self.get_latex_code() + r'{an\_example\_pypi\_project.useful\_2.}')
            + re.escape(self.get_latex_bfcode() + r'{MyPublicClass}') + '.*'
            + re.escape(r"{\emph{foo}, \emph{bar='baz'}}") + '.*'
            + re.escape(r'We use this as a public class example class.') + '.*'
            + re.escape(self.get_latex_bfcode() + r'{\_get\_baz}') + '.*'
            + re.escape(r'{\emph{baz=None}}') + '.*'
            + re.escape(r'A private function to get baz.') + '.*'
            + re.escape(r'This really should have a full function definition, but I am too lazy.') + '.*'
            + re.escape(self.get_latex_bfcode() + r'{get\_foobar}') + '.*'
            + re.escape(r'{\emph{foo}, \emph{bar=True}}') + '.*'
            + re.escape(r'This gets the foobar') + '.*'
            + re.escape(r'This really should have a full function definition, but I am too lazy.')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
        testroot='ext-autodoc',
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.autodoc: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check API auto-documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'A pypi demonstration vehicle.') + '.*'
            + re.escape(r'This is something I want to say that is not in the docstring.') + '.*'
            + re.escape(r"class an_example_pypi_project.useful_1.MyPublicClass(foo, bar='baz')") + '.*'
            + re.escape(r'   We use this as a public class example class.') + '.*'
            + re.escape(r'   get_foobar(foo, bar=True)') + '.*'
            + re.escape(r'      This gets the foobar') + '.*'
            + re.escape(r'      This really should have a full function definition, but I am too') + '.*'
            + re.escape(r'      lazy.') + '.*'
            + re.escape(r'an_example_pypi_project.useful_1.public_fn_with_googley_docstring(name, state=None)') + '.*'
            + re.escape(r'   This function does something.') + '.*'
            + re.escape(r'an_example_pypi_project.useful_1.public_fn_with_sphinxy_docstring(name, state=None)') + '.*'
            + re.escape(r'   This function does something.') + '.*'
            + re.escape(r'This is something I want to say that is not in the docstring.') + '.*'
            + re.escape(r'A very useful module indeed.') + '.*'
            + re.escape(r'an_example_pypi_project.useful_2.public_fn_with_sphinxy_docstring(name, state=None)') + '.*'
            + re.escape(r'   This function does something.') + '.*'
            + re.escape(r'an_example_pypi_project.useful_2._private_fn_with_docstring')
            + re.escape(r"(foo, bar='baz', foobarbas=None)") + '.*'
            + re.escape(r'   I have a docstring, but ') + '.*'
            + re.escape(r"class an_example_pypi_project.useful_2.MyPublicClass(foo, bar='baz')") + '.*'
            + re.escape(r'   We use this as a public class example class.') + '.*'
            + re.escape(r'   _get_baz(baz=None)') + '.*'
            + re.escape(r'      A private function to get baz.') + '.*'
            + re.escape(r'      This really should have a full function definition, but I am too') + '.*'
            + re.escape(r'      lazy.') + '.*'
            + re.escape(r'   get_foobar(foo, bar=True)') + '.*'
            + re.escape(r'      This gets the foobar') + '.*'
            + re.escape(r'      This really should have a full function definition, but I am too') + '.*'
            + re.escape(r'      lazy.')
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
