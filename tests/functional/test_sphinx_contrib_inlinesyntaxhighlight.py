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
test_sphinx_contrib_inlinesyntaxhighlight
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the
sphinxcontrib.inlinesyntaxhighlight extension as part of the
publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests.functional import fixtures

import re


class TestCaseSphinxContribInlineSyntaxHighlight(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_html_app(
        testroot='contrib-inlinesyntaxhighlight',
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.inlinesyntaxhighlight: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check inline syntax highlighting
        r = re.compile(
            '(?ms)'
            + re.escape(r'<p>This is a address: ')
            + re.escape(r'<code class="code highlight hexdump docutils literal highlight-hexdump">')
            + re.escape(r'<span></span><span class="nl">40h</span></code></p>') + '.*'
            + re.escape(r'<p>This is a code: ')
            + re.escape(r'<code class="code highlight hexdump docutils literal highlight-hexdump">')
            + re.escape(r'<span></span><span class="nl">0C</span></code></p>') + '.*'
            + re.escape(r'<p>This is a port: ')
            + re.escape(r'<code class="code highlight hexdump docutils literal highlight-hexdump">')
            + re.escape(r'<span></span><span class="nl">20</span></code></p>') + '.*'
            + re.escape(r'<p>This is a console output: ')
            + re.escape(r'<code class="code highlight console docutils literal highlight-console">')
            + re.escape(r'<span></span><span class="go">ERROR: not found.</span></code></p>') + '.*'
            + re.escape(r'<p>This is a assembler mnemonic: ')
            + re.escape(r'<code class="code highlight nasm docutils literal highlight-nasm">')
            + re.escape(r'<span></span><span class="nf">NOP</span></code></p>')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
        testroot='contrib-inlinesyntaxhighlight',
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.inlinesyntaxhighlight: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check inline syntax highlighting
        r = re.compile(
            '(?ms)'
            + re.escape(r'This is a address: ' + self.get_latex_code() + r'{40h}') + '.*'
            + re.escape(r'This is a code: ' + self.get_latex_code() + r'{0C}') + '.*'
            + re.escape(r'This is a port: ' + self.get_latex_code() + r'{20}') + '.*'
            + re.escape(r'This is a console output: ' + self.get_latex_code() + r'{ERROR: not found.}') + '.*'
            + re.escape(r'This is a assembler mnemonic: ' + self.get_latex_code() + r'{NOP}')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
        testroot='contrib-inlinesyntaxhighlight',
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.inlinesyntaxhighlight: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check inline syntax highlighting
        r = re.compile(
            '(?ms)'
            + re.escape(r'This is a address: "40h"') + '.*'
            + re.escape(r'This is a code: "0C"') + '.*'
            + re.escape(r'This is a port: "20"') + '.*'
            + re.escape(r'This is a console output: "ERROR: not found."') + '.*'
            + re.escape(r'This is a assembler mnemonic: "NOP"')
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
