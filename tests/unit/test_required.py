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
test_required
~~~~~~~~~~~~~

This module contains basic unit tests over all handled requirements
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2017 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests import util

_EXPECT_REQUIRED = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.extlinks',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinxarg.ext',
    'sphinxcontrib.ansi',
    'sphinxcontrib.autoprogram',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.email',
    'sphinxcontrib.embedly',
    'sphinxcontrib.inlinesyntaxhighlight',
    'sphinxcontrib.programoutput',
    'sphinxcontrib.spelling',
    'sphinxcontrib.tikz',
]


class TestRequired(util.TestCasePublishingSphinx):

    def test_package_has_list_of_required_extensions(self):
        '''
        UNIT TEST: package has list of required extensions
        '''
        import publishing.withsphinx.required as pwsr
        self.assertTrue(isinstance(pwsr._REQUIRED, list))
        self.assertCountEqual(pwsr._REQUIRED, _EXPECT_REQUIRED)

    def test_package_has_load_all_required_extensions(self):
        '''
        UNIT TEST: package has load all required extensions
        '''
        import publishing.withsphinx.required as pwsr
        self.assertTrue(callable(pwsr.extensions))
        app = util.mock.MagicMock()
        pwsr.extensions(app)
        for ext in _EXPECT_REQUIRED:
            app.setup_extension.assert_any_call(ext)


if __name__ == "__main__":
    util.main()
