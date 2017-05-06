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
test_sphinx_contrib_ansi
~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinxcontrib.ansi extension
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

import re
from tests import util


class TestCaseSphinxContribAnsi(util.TestCasePublishingSphinx):

    @util.with_testroot_app(
        testroot='contrib-ansi',
        confoverrides={
            'html_ansi_stylesheet': None,
        },
        buildername='html',  # TODO: add support for singlehtml backend of this extention
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.ansi: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check ANSI text block
        r = re.compile(
            '(?ms)' '<pre class="ansi-block literal-block">'
            '.*'    'This is a <span class="ansi-red ansi-bold">ANSI</span> control sequence\.'
            '.*'    '</pre>'
        )
        self.assertRegex(c, r)

    @util.with_latex_app(
        testroot='contrib-ansi',
        confoverrides={
            'html_ansi_stylesheet': None,
        },
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.ansi: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check ANSI text block
        # TODO: add support for latex backend of this extention
        r = re.compile(
            '(?ms)' '.begin\{' + self.get_latex_verbatim() + '\}\[commandchars=...\{.\}\]'
            '.*'    'This.*is.*a.*ANSI.*control.*sequence.*\.'
            '.*'    '.end\{' + self.get_latex_verbatim() + '\}'
        )
        self.assertRegex(c, r)

    @util.with_text_app(
        testroot='contrib-ansi',
        confoverrides={
            'html_ansi_stylesheet': None,
        },
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.ansi: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check ANSI text block
        r = re.compile(
            '(?ms)' 'This is a ANSI control sequence\.'
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    util.main()
