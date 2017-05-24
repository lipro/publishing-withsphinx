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
test_sphinx_contrib_email
~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinxcontrib.email extension
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests.functional import fixtures

import re


class TestCaseSphinxContribEmail(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_html_app(
        testroot='contrib-email',
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.email: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check email encryption
        r = re.compile(
            '(?ms)' +
            re.escape(r'<p><script type="text/javascript">document.write(') + '.*' +
            re.escape(r'"<n uers=\"znvygb:n\100op\056qr\">N Op <\057n>".replace(/[a-zA-Z]/g,') + '.*' +
            re.escape(r'function(c){') + '.*' +
            re.escape(r'return String.fromCharCode(') + '.*' +
            re.escape(r'(c<="Z"?90:122)>=(c=c.charCodeAt(0)+13)?c:c-26);}));') + '.*' +
            re.escape(r'</script></p>') + '.*' +
            re.escape(r'<p>A Bc &lt;<a class="reference external" href="mailto:a&#37;&#52;&#48;bc&#46;de">') +
            re.escape(r'a<span>&#64;</span>bc<span>&#46;</span>de</a>&gt;</p>')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
        testroot='contrib-email',
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.email: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check email encryption
        # TODO: add support for latex backend of this extention
        r = re.compile(
            '(?ms)' +
            re.escape(r'A Bc \textless{}') +
            re.escape(self.get_latex_href() + r'{mailto:a@bc.de}{a@bc.de}') +
            re.escape(r'\textgreater{}')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
        testroot='contrib-email',
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.email: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check email encryption
        # TODO: add support for text backend of this extention
        r = re.compile(
            '(?ms)' + re.escape(r'A Bc <a@bc.de>')
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
