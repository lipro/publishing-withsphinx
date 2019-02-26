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
test_sphinx_ext_doctest
~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinx.ext.doctest extension
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests.functional import fixtures

import re


class TestCaseSphinxExtDocTest(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_doctest_app(
        testroot='ext-doctest',
    )
    def test_build_doctest(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.doctest: can run and summarize embedded tests
        '''
        app.builder.build_all()
        print(status.getvalue())
        print(warning.getvalue())

        # check file for doctest results
        p = fixtures.path(app.outdir / 'output.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # validate doctest results
        r = re.compile(
            '(?ms)' r'^Document: index$'
            '.*'    r'^---------------$'
            '.*'    r'^Doctest summary$'
            '.*'    r'^===============$'
            '.*'    r'[1-9][0-9]*\s+tests'
            '.*'    r'0\s+failures\s+in\s+tests'
            '.*'    r'0\s+failures\s+in\s+setup\s+code'
            '.*'    r'0\s+failures\s+in\s+cleanup\s+code'
        )
        self.assertRegex(c, r)

        r = re.compile(
            '(?ms)' r'0\s+tests'
        )
        self.assertNotRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
