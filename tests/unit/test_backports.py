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
test_backports
~~~~~~~~~~~~~~

This module contains basic unit tests over all supported backports
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2017 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests import util

from sphinx.errors import SphinxError

_EXPECT_LATEX_ENGINE_DEFAULT_LANG_NONE = 'pdflatex'
_EXPECT_LATEX_ENGINE_DEFAULT_LANG_JA = 'platex'
_EXPECT_LATEX_ENGINE_CONFOVERRIDES = 'xelatex'
_EXPECT_LATEX_ENGINE_VALIDS = [
    _EXPECT_LATEX_ENGINE_DEFAULT_LANG_NONE,
    _EXPECT_LATEX_ENGINE_DEFAULT_LANG_JA,
    _EXPECT_LATEX_ENGINE_CONFOVERRIDES,
    'lualatex',
]


class TestBackports(util.TestCasePublishingSphinx):

    def test_package_has_return_latex_engine_defaults(self):
        '''
        UNIT TEST: package has return 'latex_engine' default
        '''
        import publishing.withsphinx.backports as pwsb
        self.assertTrue(callable(pwsb.default_latex_engine))
        cfg = util.mock.MagicMock()
        self.assertEqual(pwsb.default_latex_engine(cfg), 'pdflatex')

    def test_package_has_return_latex_engine_defaults_lang_ja(self):
        '''
        UNIT TEST: package has return 'latex_engine' with 'language' set to 'ja'
        '''
        import publishing.withsphinx.backports as pwsb
        self.assertTrue(callable(pwsb.default_latex_engine))
        cfg = util.mock.MagicMock()
        cfg.language = 'ja'
        self.assertEqual(pwsb.default_latex_engine(cfg), 'platex')

    def test_package_has_check_latex_engine_with_valid_content(self):
        '''
        UNIT TEST: package has check 'latex_engine' with valid content
        '''
        import publishing.withsphinx.backports as pwsb
        self.assertTrue(callable(pwsb.check_latex_engine))
        app = util.mock.MagicMock()
        app.config.values = dict(latex_engine=None)
        for latex_engine in _EXPECT_LATEX_ENGINE_VALIDS:
            app.config.latex_engine = latex_engine
            pwsb.check_latex_engine(app)

    @util.nose.tools.raises(SphinxError)
    def test_package_has_check_latex_engine_with_invalid_content(self):
        '''
        UNIT TEST: package has check 'latex_engine' with invalid content
        '''
        import publishing.withsphinx.backports as pwsb
        self.assertTrue(callable(pwsb.check_latex_engine))
        app = util.mock.MagicMock()
        app.config.values = dict(latex_engine=None)
        app.config.latex_engine = 'nonsens'
        pwsb.check_latex_engine(app)

    @util.nose.tools.raises(SphinxError)
    def test_package_has_check_latex_engine_not_in_config_values(self):
        '''
        UNIT TEST: package has check 'latex_engine' not in config values
        '''
        import publishing.withsphinx.backports as pwsb
        self.assertTrue(callable(pwsb.check_latex_engine))
        app = util.mock.MagicMock()
        app.config.values = dict(nothing=None)
        pwsb.check_latex_engine(app)

    def test_package_has_latex_engine_add_when_not_in_config_values(self):
        '''
        UNIT TEST: package has add 'latex_engine' when not in config values
        '''
        import publishing.withsphinx.backports as pwsb
        self.assertTrue(callable(pwsb.sphinx15))
        app = util.mock.MagicMock()
        app.config.values = dict(nothing=None)
        pwsb.sphinx15(app)
        app.add_config_value.assert_called_once_with('latex_engine', pwsb.default_latex_engine, None)
        app.connect.assert_called_once_with('builder-inited', pwsb.check_latex_engine)

    def test_package_has_latex_engine_add_when_is_in_config_values(self):
        '''
        UNIT TEST: package has add 'latex_engine' when is in config values
        '''
        import publishing.withsphinx.backports as pwsb
        self.assertTrue(callable(pwsb.sphinx15))
        app = util.mock.MagicMock()
        app.config.values = dict(latex_engine=None)
        pwsb.sphinx15(app)
        app.add_config_value.assert_not_called()
        app.connect.assert_not_called()


if __name__ == "__main__":
    util.main()
