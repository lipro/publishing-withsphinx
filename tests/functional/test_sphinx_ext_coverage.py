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
test_sphinx_ext_coverage
~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinx.ext.coverage
extension as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

import re
from tests import util


class TestCaseSphinxExtCoverage(util.TestCasePublishingSphinx):

    @util.with_coverage_app(
        testroot='ext-coverage',
    )
    def test_build_coverage(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.coverage: can collect from sample
        '''
        app.builder.build_all()
        print(status.getvalue())
        print(warning.getvalue())

        # check file for C/C++ coverage results
        p = util.path(app.outdir / 'c.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # validate C/C++ coverage results
        r = re.compile(
            '(?ms)' '^Undocumented C API elements$'
            '.*'    '^===========================$'
        )
        self.assertRegex(c, r)

        r = re.compile(
            '(?ms)' '^hello$'
        )
        self.assertNotRegex(c, r)

        # check file for Python coverage results
        p = util.path(app.outdir / 'python.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # validate Python coverage results
        r = re.compile(
            '(?ms)' '^Undocumented Python objects$'
            '.*'    '^===========================$'
            '.*'    '^hello$'
            '.*'    '^-----$'
            '.*'    '^Functions:$'
            '.*'    '^ \* hello$'
        )
        self.assertRegex(c, r)

        # FIXME: disable the false positive test here because of unknown
        # race conditions or any other side effencts with
        # TestCaseSphinxBasics:test_build_coverage()
        # - only observed inside some isolated tox environments with
        #   Sphinx 1.2 and 1.3
        # - only observed when TestCaseSphinxBasics will be executed before
        #   TestCaseSphinxExtCoverage
        if self.is_sphinx_coverage_not_affected():
            r = re.compile(
                '(?ms)' '^an_example_pypi_project$'
                '.*'    '^an_example_pypi_project\.useful_1$'
                '.*'    '^an_example_pypi_project\.useful_2$'
            )
            self.assertNotRegex(c, r)


if __name__ == "__main__":
    util.main()
