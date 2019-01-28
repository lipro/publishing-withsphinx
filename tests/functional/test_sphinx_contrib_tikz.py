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
test_sphinx_contrib_tikz
~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinxcontrib.tikz extension
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests.functional import fixtures

import re


class TestCaseSphinxContribTikz(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_html_app(
        testroot='contrib-tikz',
        confoverrides={
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
            'tikz_proc_suite': 'GhostScript',
            'tikz_transparent': True,
        },
    )
    def test_build_html_png(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.tikz: can build html with PNG
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check TikZ figure
        r = re.compile(
            '(?ms)' +
            re.escape(r'<div class="figure">') + '.*' +
            re.escape(r'<p><img src="_images/tikz-') + '.*' +
            re.escape(r'.png" alt="[transform shape,') + '.*' + re.escape(r']') + '.*' +
            re.escape(r'\sffamily\tiny') + '.*' +
            re.escape(r'\tikzfoldingdodecahedron[') + '.*' + re.escape(r'];" /></p>') + '.*' +
            re.escape(r'<p class="caption">A new year is coming soon ...</p></div>')
        )
        self.assertRegex(c, r)

    @fixtures.with_html_app(
        testroot='contrib-tikz',
        confoverrides={
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
            'tikz_proc_suite': 'pdf2svg',
            'tikz_transparent': True,
        },
    )
    def test_build_html_svg(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.tikz: can build html with SVG
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check TikZ figure
        r = re.compile(
            '(?ms)' +
            re.escape(r'<div class="figure">') + '.*' +
            re.escape(r'<p><img src="_images/tikz-') + '.*' +
            re.escape(r'.svg" alt="[transform shape,') + '.*' + re.escape(r']') + '.*' +
            re.escape(r'\sffamily\tiny') + '.*' +
            re.escape(r'\tikzfoldingdodecahedron[') + '.*' + re.escape(r'];" /></p>') + '.*' +
            re.escape(r'<p class="caption">A new year is coming soon ...</p></div>')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
        testroot='contrib-tikz',
        confoverrides={
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
            'tikz_proc_suite': 'pdf2svg',
            'tikz_transparent': True,
        },
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.tikz: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check TikZ figure
        r = re.compile(
            '(?ms)' +
            re.escape(r'\begin{figure}[htp]\centering\begin{tikzpicture}') + '.*' +
            re.escape(r'[transform shape,') + '.*' + re.escape(r']') + '.*' +
            re.escape(r'\sffamily\tiny') + '.*' +
            re.escape(r'\tikzfoldingdodecahedron[') + '.*' + re.escape(r']') + '.*' +
            re.escape(r'\end{tikzpicture}\caption{A new year is coming soon ...}\end{figure}')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
        testroot='contrib-tikz',
        confoverrides={
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
            'tikz_proc_suite': 'pdf2svg',
            'tikz_transparent': True,
        },
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.tikz: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check TikZ figure
        # TODO: add support for text backend of this extention
        r = re.compile(
            '(?ms)' + re.escape(r'A new year is coming soon ...')
        )
        self.assertNotRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
