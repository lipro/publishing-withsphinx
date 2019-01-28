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
test_sphinx_contrib_argparse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinxarg.ext extension
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests.functional import fixtures

import re


class TestCaseSphinxContribArgParse(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_html_app(
        testroot='contrib-argparse',
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxarg.ext: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check CLI program documentation
        r = re.compile(
            '(?ms)' +
            re.escape(r'<pre') + '.*' + re.escape(r'usage') + '.*' + re.escape(r'cmdargs') + '.*' +
            re.escape(r'apply') + '.*' + re.escape(r'game') + '.*' + re.escape(r'</pre>') + '.*' +
            re.escape(r'<pre') + '.*' + re.escape(r'cmdargs') + '.*' + re.escape(r'apply') + '.*' +
            re.escape(r'tree') + '.*' + re.escape(r'dry') + '.*' + re.escape(r'force') + '.*' +
            re.escape(r'path') + '.*' + re.escape(r'</pre>') + '.*' +
            re.escape(r'<pre') + '.*' + re.escape(r'cmdargs') + '.*' + re.escape(r'game') + '.*' +
            re.escape(r'opt') + '.*' + re.escape(r'rock') + '.*' + re.escape(r'paper') + '.*' +
            re.escape(r'scissors') + '.*' + re.escape(r'rock') + '.*' + re.escape(r'paper') + '.*' +
            re.escape(r'scissors') + '.*' + re.escape(r'</pre>')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
        testroot='contrib-argparse',
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxarg.ext: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check CLI program documentation
        r = re.compile(
            '(?ms)' +
            re.escape(r'\begin{' + self.get_latex_verbatim(alltt=True) + r'}') + '.*' +
            re.escape(r'usage') + '.*' + re.escape(r'cmdargs') + '.*' + re.escape(r'apply') + '.*' +
            re.escape(r'game') + '.*' + re.escape(r'\end{' + self.get_latex_verbatim(alltt=True) + r'}') + '.*' +
            re.escape(r'\begin{' + self.get_latex_verbatim(alltt=True) + r'}') + '.*' +
            re.escape(r'cmdargs') + '.*' + re.escape(r'apply') + '.*' + re.escape(r'tree') + '.*' +
            re.escape(r'dry') + '.*' + re.escape(r'force') + '.*' + re.escape(r'path') + '.*' +
            re.escape(r'\end{' + self.get_latex_verbatim(alltt=True) + r'}') + '.*' +
            re.escape(r'\begin{' + self.get_latex_verbatim(alltt=True) + r'}') + '.*' +
            re.escape(r'cmdargs') + '.*' + re.escape(r'game') + '.*' + re.escape(r'opt') + '.*' +
            re.escape(r'rock') + '.*' + re.escape(r'paper') + '.*' + re.escape(r'scissors') + '.*' +
            re.escape(r'rock') + '.*' + re.escape(r'paper') + '.*' + re.escape(r'scissors') + '.*' +
            re.escape(r'\end{' + self.get_latex_verbatim(alltt=True) + r'}')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
        testroot='contrib-argparse',
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxarg.ext: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check CLI program documentation
        r = re.compile(
            '(?ms)' +
            re.escape(r'usage: cmdargs [-h] {apply,game} ...') + '.*' +
            re.escape(r'cmdargs apply [-h] [-r] [--tree] [--dry] [--force] path') + '.*' +
            re.escape(r'cmdargs game [-h] [--opt {rock,paper,scissors}] {rock,paper,scissors}')
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
