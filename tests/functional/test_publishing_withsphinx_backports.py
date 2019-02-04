# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Stephan Linz
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
test_publishing_withsphinx_backports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests over all supported backports
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2017 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests.functional import fixtures

from sphinx import __version__ as SphinxVersion
from sphinx.errors import SphinxError

from distutils.version import LooseVersion
SPHINX_GT_17 = LooseVersion(SphinxVersion) >= LooseVersion('1.8')
SPHINX_GT_14 = LooseVersion(SphinxVersion) >= LooseVersion('1.5')
SPHINX_LT_15 = LooseVersion(SphinxVersion) < LooseVersion('1.5')

_EXPECT_LATEX_ENGINE_DEFAULT_LANG_NONE = 'pdflatex'
_EXPECT_LATEX_ENGINE_DEFAULT_LANG_JA = 'platex'
_EXPECT_LATEX_ENGINE_CONFOVERRIDES = 'xelatex'
_EXPECT_LATEX_ENGINE_VALIDS = [
    _EXPECT_LATEX_ENGINE_DEFAULT_LANG_NONE,
    _EXPECT_LATEX_ENGINE_DEFAULT_LANG_JA,
    _EXPECT_LATEX_ENGINE_CONFOVERRIDES,
    'lualatex',
]


class TestPublishingWithSphinxBackports(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_coverage_app(
        testroot='module-backports',
    )
    def test_latex_engine_defaults(self, app, status, warning):
        '''
        FUNCTIONAL TEST: backport 'latex_engine' defaults
        '''
        self.assertTrue(isinstance(app.config.latex_engine, str))
        self.assertEqual(app.config.latex_engine, _EXPECT_LATEX_ENGINE_DEFAULT_LANG_NONE)

    @fixtures.util.unittest.skipIf(SPHINX_GT_17, 'for Sphinx ' + SphinxVersion + ' > 1.7, due of language side effects')
    @fixtures.with_coverage_app(
        testroot='module-backports',
        confoverrides={
            'language': 'ja',
        },
    )
    def test_latex_engine_defaults_lang_ja(self, app, status, warning):
        '''
        FUNCTIONAL TEST: backport 'latex_engine' with 'language' set to 'ja'
        '''
        self.assertTrue(isinstance(app.config.latex_engine, str))
        self.assertEqual(app.config.latex_engine, _EXPECT_LATEX_ENGINE_DEFAULT_LANG_JA)

    @fixtures.with_coverage_app(
        testroot='module-backports',
        confoverrides={
            'latex_engine': _EXPECT_LATEX_ENGINE_CONFOVERRIDES,
        },
    )
    def test_latex_engine_valid(self, app, status, warning):
        '''
        FUNCTIONAL TEST: backport 'latex_engine' with valid setup from confoverrides
        '''
        self.assertTrue(isinstance(app.config.latex_engine, str))
        self.assertEqual(app.config.latex_engine, _EXPECT_LATEX_ENGINE_CONFOVERRIDES)

    @fixtures.util.unittest.skipIf(SPHINX_GT_14, 'for Sphinx ' + SphinxVersion + ' > 1.4')
    @fixtures.util.nose.tools.raises(SphinxError)
    @fixtures.with_coverage_app(
        testroot='module-backports',
        confoverrides={
            'latex_engine': 'invalid latex engine',
        },
    )
    def test_latex_engine_invalid_raise_error(self, app, status, warning):
        '''
        FUNCTIONAL TEST: backport 'latex_engine' with invalid setup raises error
        '''
        pass

    @fixtures.util.unittest.skipIf(SPHINX_LT_15, 'for Sphinx ' + SphinxVersion + ' < 1.5')
    @fixtures.with_coverage_app(
        testroot='module-backports',
        confoverrides={
            'latex_engine': 'invalid latex engine',
        },
    )
    def test_latex_engine_invalid_unchanged(self, app, status, warning):
        '''
        FUNCTIONAL TEST: backport 'latex_engine' with invalid setup keep unchanged
        '''
        self.assertTrue(isinstance(app.config.latex_engine, str))
        self.assertEqual(app.config.latex_engine, 'invalid latex engine')


if __name__ == "__main__":
    fixtures.main()
