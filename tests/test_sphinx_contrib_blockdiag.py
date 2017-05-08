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
test_sphinx_contrib_blockdiag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinxcontrib.blockdiag
extension as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

import re
from tests import util


class TestCaseSphinxContribBlockdiag(util.TestCasePublishingSphinx):

    @util.with_html_app(
        testroot='contrib-blockdiag',
        confoverrides={
            'blockdiag_antialias': True,
            'blockdiag_transparency': True,
            'blockdiag_html_image_format': 'PNG',
        },
    )
    def test_build_html_png(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.blockdiag: can build html with PNG
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check blockdiag graphic
        r = re.compile(
            '(?ms)' +
            re.escape(r'<div><img ') + '.*' + re.escape(r'src="_images/blockdiag-') + '.*' +
            re.escape(r'.png"') + '.*' + re.escape(r' /></div>') + '.*' +
            re.escape(r'<div><img ') + '.*' + re.escape(r'src="_images/blockdiag-') + '.*' +
            re.escape(r'.png"') + '.*' + re.escape(r' /></div>')
        )
        self.assertRegex(c, r)

    @util.with_html_app(
        testroot='contrib-blockdiag',
        confoverrides={
            'blockdiag_antialias': True,
            'blockdiag_transparency': True,
            'blockdiag_html_image_format': 'SVG',
        },
    )
    def test_build_html_svg(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.blockdiag: can build html with SVG
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check blockdiag graphic
        r = re.compile(
            '(?ms)' +
            re.escape(r'<div><svg ') + '.*' +
            re.escape(r'xmlns="http://www.w3.org/2000/svg"') + '.*' +
            re.escape(r'xmlns:inkspace="http://www.inkscape.org/namespaces/inkscape"') + '.*' +
            re.escape(r'xmlns:xlink="http://www.w3.org/1999/xlink">') + '.*' +
            re.escape(r'<title>blockdiag</title>') + '.*' +
            re.escape(r'<text ') + '.*' + re.escape(r'>A</text>') + '.*' +
            re.escape(r'<text ') + '.*' + re.escape(r'>B</text>') + '.*' +
            re.escape(r'</svg>') + '.*' + re.escape(r'</div>') + '.*' +
            re.escape(r'<div><svg ') + '.*' +
            re.escape(r'xmlns="http://www.w3.org/2000/svg"') + '.*' +
            re.escape(r'xmlns:inkspace="http://www.inkscape.org/namespaces/inkscape"') + '.*' +
            re.escape(r'xmlns:xlink="http://www.w3.org/1999/xlink">') + '.*' +
            re.escape(r'<title>blockdiag</title>') + '.*' +
            re.escape(r'<text ') + '.*' + re.escape(r'>A</text>') + '.*' +
            re.escape(r'<text ') + '.*' + re.escape(r'>B</text>') + '.*' +
            re.escape(r'<text ') + '.*' + re.escape(r'>C</text>') + '.*' +
            re.escape(r'<text ') + '.*' + re.escape(r'>D</text>') + '.*' +
            re.escape(r'</svg>') + '.*' + re.escape(r'</div>')
        )
        self.assertRegex(c, r)

    @util.with_latex_app(
        testroot='contrib-blockdiag',
        confoverrides={
            'blockdiag_antialias': True,
            'blockdiag_transparency': True,
            'blockdiag_latex_image_format': 'PNG',
        },
    )
    def test_build_latex_png(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.blockdiag: can build latex with PNG
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check blockdiag graphic
        # TODO: add support for latex backend of this extention
        r = re.compile(
            '(?ms)' +
            re.escape(self.get_latex_includegraphics()) + '.*' +
            re.escape(r'{blockdiag-') + '.*' + re.escape(r'.png}') + '.*' +
            re.escape(self.get_latex_includegraphics()) + '.*' +
            re.escape(r'{blockdiag-') + '.*' + re.escape(r'.png}')
        )
        self.assertRegex(c, r)

    @util.with_latex_app(
        testroot='contrib-blockdiag',
        confoverrides={
            'blockdiag_antialias': True,
            'blockdiag_transparency': True,
            'blockdiag_latex_image_format': 'PDF',
        },
    )
    def test_build_latex_pdf(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.blockdiag: can build latex with PDF
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check blockdiag graphic
        # TODO: add support for latex backend of this extention
        r = re.compile(
            '(?ms)' +
            re.escape(self.get_latex_includegraphics()) + '.*' +
            re.escape(r'{blockdiag-') + '.*' + re.escape(r'.pdf}') + '.*' +
            re.escape(self.get_latex_includegraphics()) + '.*' +
            re.escape(r'{blockdiag-') + '.*' + re.escape(r'.pdf}')
        )
        self.assertRegex(c, r)

    @util.with_text_app(
        testroot='contrib-blockdiag',
        confoverrides={
            'blockdiag_antialias': True,
            'blockdiag_transparency': True,
        },
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.blockdiag: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check blockdiag graphic
        # TODO: add support for text backend of this extention
        r = re.compile(
            '(?ms)' + re.escape(r'[image][image]')
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    util.main()
