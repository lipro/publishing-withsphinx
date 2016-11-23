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
test_sphinx_contrib_embedly
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinxcontrib.embedly
extension as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

import re
from tests import util


class TestCaseSphinxContribEmbedly(util.TestCasePublishingSphinx):

    @util.with_html_app(
        testroot='contrib-embedly',
        confoverrides={
            'embedly_key': '6fed632213d44dcb98cb860fabb33e7f',
            'embedly_timeout': 120,
        },
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.embedly: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check embedly block
        r = re.compile(
            '(?ms)' '<a href="http://www\.montypython\.com/" title="'
            '.*'    '">Monty Python Official Site</a>'
            '.*'    '<a href="http://www\.montypython\.net/sounds/lob/16done\.wav" title="'
            '.*'    '">http://www\.montypython\.net/sounds/lob/16done\.wav</a>'
            '.*'    '<img width=".*"'
            '.*'    'height=".*"'
            '.*'    'alt=".*"'
            '.*'    'src="https://i\.embed\.ly/'
            '.*'    'url=http%3A%2F%2Fwww\.montypython\.com%2Fhimg%2F_0\.png&key='
            '.*'    '/>'
            '.*'    '<iframe class="embedly-embed" src="https://cdn\.embedly\.com/'
            '.*'    'url=http%3A%2F%2Fwww\.youtube\.com%2Fwatch%3Fv%3DM_eYSuPKP3Y'
            '.*'    '&key='
            '.*'    '</iframe>'
        )
        self.assertRegex(c, r)

    @util.with_latex_app(
        testroot='contrib-embedly',
        confoverrides={
            'embedly_key': '6fed632213d44dcb98cb860fabb33e7f',
            'embedly_timeout': 120,
        },
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.embedly: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check embedly block
        # TODO: add support for latex backend of this extention
        r = re.compile(
            '(?ms)' '..*{Monty Python .textless\{\}'
                    'http://www\.montypython\.com/.textgreater\{\}\}'
            '.*'    '..*\{Monty Python .textless\{\}'
                    'http://www\.montypython\.net/sounds/lob/16done.wav.textgreater\{\}\}'
            '.*'    '..*\{Monty Python .textless\{\}'
                    'http://www.montypython.com/himg/._0\.png.textgreater\{\}\}'
            '.*'    'Monty Python\'s ..*\{SPAM .textless\{\}'
                    'http://www\.youtube\.com/watch\?v=M._eYSuPKP3Y.textgreater\{\}\}'
        )
        self.assertRegex(c, r)

    @util.with_text_app(
        testroot='contrib-embedly',
        confoverrides={
            'embedly_key': '6fed632213d44dcb98cb860fabb33e7f',
            'embedly_timeout': 120,
        },
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.embedly: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check embedly block
        # TODO: add support for text backend of this extention
        r = re.compile(
            '(?ms)' 'Monty Python <http://www.montypython\.com/>'
            '.*'    'Monty Python <http://www.montypython\.net/sounds/lob/16done\.wav>'
            '.*'    'Monty Python <http://www.montypython\.com/himg/_0\.png>'
            '.*'    'Monty Python.* .*SPAM <http://www\.youtube\.com/watch\?v=M_eYSuPKP3Y>'
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    util.main()
