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
test_sphinx_ext_extlinks
~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinx.ext.extlinks extension
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

import re
from tests import util


class TestCaseSphinxExtExtLinks(util.TestCasePublishingSphinx):

    @util.with_html_app(
        testroot='ext-extlinks',
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.extlinks: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' +
            re.escape(r'<ul class="simple">') + '.*' + re.escape(r'<li>The Datasheet Archive:<ul>') + '.*' +
            re.escape(r'<li><a class="reference external"') + '.*' +
            re.escape(r'href="http://datasheet.datasheetarchive.com/originals') +
            re.escape(r'/scans/Scans-048/DSAGER000371.pdf">') +
            re.escape(r'Datasheet Archive (IDXF): Scans-048/DSAGER000371</a></li>') + '.*' +
            re.escape(r'<li><a class="reference external"') + '.*' +
            re.escape(r'href="http://datasheet.datasheetarchive.com/originals') +
            re.escape(r'/distributors/Datasheets-AE/DSA5GERT0000353.pdf">') +
            re.escape(r'Datasheet Archive (MAIN): Datasheets-AE/DSA5GERT0000353</a></li>') + '.*' +
            re.escape(r'</ul>') + '.*' + re.escape(r'</li>') + '.*' + re.escape(r'</ul>')
        )
        self.assertRegex(c, r)

    @util.with_latex_app(
        testroot='ext-extlinks',
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.extlinks: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' +
            re.escape(r'\begin{itemize}') + '.*' + re.escape(r'\item {}') + '.*' +
            re.escape(r'The Datasheet Archive:') + '.*' + re.escape(r'\begin{itemize}') + '.*' +
            re.escape(r'\item {}') + '.*' + re.escape(self.get_latex_href()) +
            re.escape('{http://datasheet.datasheetarchive.com/originals') +
            re.escape(r'/scans/Scans-048/DSAGER000371.pdf}') +
            re.escape(r'{Datasheet Archive (IDXF): Scans-048/DSAGER000371}') + '.*' +
            re.escape(r'\item {}') + '.*' + re.escape(self.get_latex_href()) +
            re.escape('{http://datasheet.datasheetarchive.com/originals') +
            re.escape(r'/distributors/Datasheets-AE/DSA5GERT0000353.pdf}') +
            re.escape(r'{Datasheet Archive (MAIN): Datasheets-AE/DSA5GERT0000353}') + '.*' +
            re.escape(r'\end{itemize}') + '.*' + re.escape(r'\end{itemize}')
        )
        self.assertRegex(c, r)

    @util.with_text_app(
        testroot='ext-extlinks',
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.extlinks: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' +
            re.escape(r'* The Datasheet Archive:') + '.*' +
            re.escape(r'  * Datasheet Archive (IDXF): Scans-048/DSAGER000371') + '.*' +
            re.escape(r'  * Datasheet Archive (MAIN): Datasheets-AE/DSA5GERT0000353')
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    util.main()
