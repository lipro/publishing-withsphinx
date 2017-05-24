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
test_sphinx_ext_ifconfig
~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinx.ext.ifconfig extension
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests.functional import fixtures

import re


class TestCaseSphinxExtIfConfig(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_html_app(
        testroot='ext-ifconfig',
    )
    def test_build_html_default(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build html with default config
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check content
        r = re.compile(
            '(?ms)' + re.escape(r'<p>spam</p>')
        )
        self.assertRegex(c, r)

        r = re.compile(
            '(?ms)' + re.escape(r'<p>egg</p>')
        )
        self.assertNotRegex(c, r)

    @fixtures.with_html_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': True,
            'confval2': False,
        },
    )
    def test_build_html_set_confval1(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build html with confval1
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'<p>spam</p>')
        )
        self.assertRegex(c, r)

        r = re.compile(
            '(?ms)' + re.escape(r'<p>egg</p>')
        )
        self.assertNotRegex(c, r)

    @fixtures.with_html_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': False,
            'confval2': True,
        },
    )
    def test_build_html_set_confval2(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build html with confval2
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'<p>spam</p>')
        )
        self.assertNotRegex(c, r)

        r = re.compile(
            '(?ms)' + re.escape(r'<p>egg</p>')
        )
        self.assertRegex(c, r)

    @fixtures.with_html_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': True,
            'confval2': True,
        },
    )
    def test_build_html_set_confval2_and_confval1(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build html with confval2 and confval1
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'<p>spam</p>') + '.*' + re.escape(r'<p>egg</p>')
        )
        self.assertRegex(c, r)

    @fixtures.with_html_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': False,
            'confval2': False,
        },
    )
    def test_build_html_unset(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build html without confval2 and confval1
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'<p>spam</p>') + '.*' + re.escape(r'<p>egg</p>')
        )
        self.assertNotRegex(c, r)

    @fixtures.with_latex_app(
        testroot='ext-ifconfig',
    )
    def test_build_latex_default(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build latex with default config
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check content
        r = re.compile(
            '(?ms)' + re.escape(r'spam')
        )
        self.assertRegex(c, r)

        r = re.compile(
            '(?ms)' + re.escape(r'egg')
        )
        self.assertNotRegex(c, r)

    @fixtures.with_latex_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': True,
            'confval2': False,
        },
    )
    def test_build_latex_set_confval1(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build latex with confval1
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'spam')
        )
        self.assertRegex(c, r)

        r = re.compile(
            '(?ms)' + re.escape(r'egg')
        )
        self.assertNotRegex(c, r)

    @fixtures.with_latex_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': False,
            'confval2': True,
        },
    )
    def test_build_latex_set_confval2(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build latex with confval2
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        r = re.compile(
            '(?ms)' + re.escape(r'spam')
        )
        self.assertNotRegex(c, r)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'egg')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': True,
            'confval2': True,
        },
    )
    def test_build_latex_set_confval2_and_confval1(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build latex with confval2 and confval1
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'spam') + '.*' + re.escape(r'egg')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': False,
            'confval2': False,
        },
    )
    def test_build_latex_unset(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build latex without confval2 and confval1
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'spam') + '.*' + re.escape(r'egg')
        )
        self.assertNotRegex(c, r)

    @fixtures.with_text_app(
        testroot='ext-ifconfig',
    )
    def test_build_text_default(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build text with default config
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check content
        r = re.compile(
            '(?ms)' + re.escape(r'spam')
        )
        self.assertRegex(c, r)

        r = re.compile(
            '(?ms)' + re.escape(r'egg')
        )
        self.assertNotRegex(c, r)

    @fixtures.with_text_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': True,
            'confval2': False,
        },
    )
    def test_build_text_set_confval1(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build text with confval1
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'spam')
        )
        self.assertRegex(c, r)

        r = re.compile(
            '(?ms)' + re.escape(r'egg')
        )
        self.assertNotRegex(c, r)

    @fixtures.with_text_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': False,
            'confval2': True,
        },
    )
    def test_build_text_set_confval2(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build text with confval2
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'spam')
        )
        self.assertNotRegex(c, r)

        r = re.compile(
            '(?ms)' + re.escape(r'egg')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': True,
            'confval2': True,
        },
    )
    def test_build_text_set_confval2_and_confval1(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build text with confval2 and confval1
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'spam') + '.*' + re.escape(r'egg')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
        testroot='ext-ifconfig',
        confoverrides={
            'confval1': False,
            'confval2': False,
        },
    )
    def test_build_text_unset(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.ifconfig: can build text without confval2 and confval1
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check external links
        r = re.compile(
            '(?ms)' + re.escape(r'spam') + '.*' + re.escape(r'egg')
        )
        self.assertNotRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
