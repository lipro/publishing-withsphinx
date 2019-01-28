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

from tests.functional import fixtures

import re


class TestCaseSphinxContribEmbedly(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_html_app(
        testroot='contrib-embedly',
        confoverrides={
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
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

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check embedly block
        r = re.compile(
            '(?ms)' +
            re.escape(r'<h2>Website<a class="headerlink" href="#website"') + '.*' + re.escape(r'</a></h2>') + '.*' +
            re.escape(r'<a href="http://www.montypython.com/" title="') +
            re.escape(r"The official online home for all things Monty Python. Pages of everything you'll ever ") +
            re.escape(r'need to know about Monty Python and their movies, TV shows, books, live stage shows, ') +
            re.escape(r'apps and latest projects, as well as exclusive videos, news and a Fanwall where all your ') +
            re.escape(r'#montypython content will live.">Monty Python Official Site</a>') + '.*' +
            re.escape(r'<h2>Audio<a class="headerlink" href="#audio"') + '.*' + re.escape(r'</a></h2>') + '.*' +
            re.escape(r'<a href="http://www.montypython.net/sounds/lob/16done.wav" title="">') +
            re.escape(r'http://www.montypython.net/sounds/lob/16done.wav</a>') + '.*' +
            re.escape(r'<h2>Image<a class="headerlink" href="#image"') + '.*' + re.escape(r'</a></h2>') + '.*' +
            re.escape(r'<img width="660"') + '.*' + re.escape(r'height="273"') + '.*' + re.escape(r'alt=""') + '.*' +
            re.escape(r'src="https://i.embed.ly/1/image') + '.*' +
            re.escape(r'?url=http%3A%2F%2Fwww.montypython.com%2Fhimg%2F_0.png') + '.*' + re.escape(r'&key=') + '.*' +
            re.escape(r'/>') + '.*' + re.escape(r'<h2>Youtube<a class="headerlink" href="#youtube"') + '.*' +
            re.escape(r'</a></h2>') + '.*' + re.escape(r'<iframe class="embedly-embed"') + '.*' +
            re.escape(r'src="https://cdn.embedly.com/widgets/media.html?') + '.*' +
            re.escape(r'url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DM_eYSuPKP3Y') + '.*' +
            re.escape(r'&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FM_eYSuPKP3Y%2Fhqdefault.jpg') + '.*' +
            re.escape(r'&key=') + '.*' + re.escape(r'&type=text%2Fhtml') + '.*' +
            re.escape(r'&schema=youtube') + '.*' + re.escape(r'width="854"') + '.*' +
            re.escape(r'height="480"') + '.*' + re.escape(r'scrolling="no"') + '.*' +
            re.escape(r'frameborder="0"') + '.*' + re.escape(r'allowfullscreen') + '.*' +
            re.escape(r'></iframe>')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
        testroot='contrib-embedly',
        confoverrides={
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
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

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check embedly block
        # TODO: add support for latex backend of this extention
        r = re.compile(
            '(?ms)' +
            re.escape(r'\chapter{Website}') + '.*' +
            re.escape(self.get_latex_titleref() + r'{Monty Python \textless{}') +
            re.escape(r'http://www.montypython.com/\textgreater{}}') + '.*' +
            re.escape(r'\chapter{Audio}') + '.*' +
            re.escape(self.get_latex_titleref() + r'{Monty Python \textless{}') +
            re.escape(r'http://www.montypython.net/sounds/lob/16done.wav\textgreater{}}') + '.*' +
            re.escape(r'\chapter{Image}') + '.*' +
            re.escape(self.get_latex_titleref() + r'{Monty Python \textless{}') +
            re.escape(r'http://www.montypython.com/himg/\_0.png\textgreater{}}') + '.*' +
            re.escape(r'\chapter{Youtube}') + '.*' +
            re.escape(self.get_latex_titleref() + r'{SPAM \textless{}') +
            re.escape(r'http://www.youtube.com/watch?v=M\_eYSuPKP3Y\textgreater{}}')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
        testroot='contrib-embedly',
        confoverrides={
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
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

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check embedly block
        # TODO: add support for text backend of this extention
        r = re.compile(
            '(?ms)' +
            re.escape(r'Website') + '.*' +
            re.escape(r'*Monty Python <http://www.montypython.com/>*') + '.*' +
            re.escape(r'Audio') + '.*' +
            re.escape(r'*Monty Python <http://www.montypython.net/sounds/lob/16done.wav>*') + '.*' +
            re.escape(r'Image') + '.*' +
            re.escape(r'*Monty Python <http://www.montypython.com/himg/_0.png>*') + '.*' +
            re.escape(r'Youtube') + '.*' +
            re.escape(r"Monty Python's *SPAM <http://www.youtube.com/watch?v=M_eYSuPKP3Y>*")
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
