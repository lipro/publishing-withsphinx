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
test_module_meta
~~~~~~~~~~~~~~~~

This module contains meta data units tests for the publishing.withsphinx
extensions as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests import util

_EXPECT_NAME = 'publishing.withsphinx'

_EXPECT_VERSION = '0.0.1'
_EXPECT_DATE = '2016-10-11'

_EXPECT_AUTHOR = 'Stephan Linz'
_EXPECT_AUTHOR_EMAIL = 'linz@li-pro.net'

_EXPECT_SPHINX_EXTENSION_METADATA = {
    'version': _EXPECT_VERSION,
    'parallel_read_safe': True,
    'parallel_write_safe': True,
}


class TestPublishingWithSphinxMetaData(util.TestCasePublishingSphinx):

    def test_package_has_extension_name_string(self):
        '''
        UNIT TEST: package has name string
        '''
        import publishing.withsphinx as pws
        self.assertTrue(isinstance(pws.__name__, str))
        self.assertEqual(pws.__name__, _EXPECT_NAME)

    def test_package_has_extension_version_string(self):
        '''
        UNIT TEST: package has version string
        '''
        import publishing.withsphinx as pws
        self.assertTrue(isinstance(pws.__version__, str))
        self.assertEqual(pws.__version__, _EXPECT_VERSION)

    def test_package_has_extension_date_string(self):
        '''
        UNIT TEST: package has date string
        '''
        import publishing.withsphinx as pws
        self.assertTrue(isinstance(pws.__date__, str))
        self.assertEqual(pws.__date__, _EXPECT_DATE)

    def test_package_has_extension_author_string(self):
        '''
        UNIT TEST: package has author string
        '''
        import publishing.withsphinx as pws
        self.assertTrue(isinstance(pws.__author__, str))
        self.assertEqual(pws.__author__, _EXPECT_AUTHOR)

    def test_package_has_extension_author_email_string(self):
        '''
        UNIT TEST: package has author email string
        '''
        import publishing.withsphinx as pws
        self.assertTrue(isinstance(pws.__author_email__, str))
        self.assertEqual(pws.__author_email__, _EXPECT_AUTHOR_EMAIL)

    def test_package_has_setup_returns_with_meta(self):
        '''
        UNIT TEST: package has setup returns with meta data
        '''
        import publishing.withsphinx as pws
        app = util.mock.MagicMock()
        self.assertEqual(pws.setup(app), _EXPECT_SPHINX_EXTENSION_METADATA)


if __name__ == "__main__":
    util.main()
