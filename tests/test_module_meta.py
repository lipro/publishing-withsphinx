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
This modules contains meta data units tests for the publishing.withsphinx module.
'''

import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

if sys.version_info < (3,):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
    unittest.TestCase.assertRegex = unittest.TestCase.assertRegexpMatches

_EXPECT_NAME = 'publishing.withsphinx'

_EXPECT_VERSION = '0.0.1'
_EXPECT_DATE = '2016-10-11'

_EXPECT_AUTHOR = 'Stephan Linz'
_EXPECT_AUTHOR_EMAIL = 'linz@li-pro.net'


class TestSphinxcontribPublishingMetaData(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        A class method called before tests in an individual class run.
        setUpClass() is called with the class as the only argument and must
        be decorated as a classmethod().
        '''
        pass

    @classmethod
    def tearDownClass(self):
        '''
        A class method called after tests in an individual class have run.
        tearDownClass() is called with the class as the only argument and
        must be decorated as a classmethod().
        '''
        pass

    def setUpModule(self):
        '''
        Module level fixtures set up. If an exception is raised in a
        setUpModule() then none of the tests in the module will be run and
        the tearDownModule() will not be run. If the exception is a SkipTest()
        exception then the module will be reported as having been skipped
        instead of as an error.
        '''
        pass

    def tearDownModule(self):
        '''
        Module level fixtures tear down. When the test suite encounters a test
        from a different module from the previous test then tearDownModule()
        from the previous module is run, followed by setUpModule() from the
        new module.
        '''
        pass

    def setUp(self):
        '''
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest(),
        any exception raised by this method will be considered an error rather
        than a test failure. The default implementation does nothing.
        '''
        pass

    def tearDown(self):
        '''
        Method called immediately after the test method has been called and
        the result recorded. This is called even if the test method raised an
        exception, so the implementation in subclasses may need to be
        particularly careful about checking internal state. Any exception,
        other than AssertionError or SkipTest(), raised by this method will be
        considered an additional error rather than a test failure (thus
        increasing the total number of reported errors). This method will only
        be called if the setUp() succeeds, regardless of the outcome of the
        test method. The default implementation does nothing.
        '''
        pass

    def test_package_has_name_string(self):
        '''
        UNIT TEST: package has name string
        '''
        import publishing.withsphinx as pubwsphinx
        self.assertTrue(isinstance(pubwsphinx.__name__, str))
        self.assertEqual(pubwsphinx.__name__, _EXPECT_NAME)

    def test_package_has_version_string(self):
        '''
        UNIT TEST: package has version string
        '''
        import publishing.withsphinx as pubwsphinx
        self.assertTrue(isinstance(pubwsphinx.__version__, str))
        self.assertEqual(pubwsphinx.__version__, _EXPECT_VERSION)

    def test_package_has_date_string(self):
        '''
        UNIT TEST: package has date string
        '''
        import publishing.withsphinx as pubwsphinx
        self.assertTrue(isinstance(pubwsphinx.__date__, str))
        self.assertEqual(pubwsphinx.__date__, _EXPECT_DATE)

    def test_package_has_author_string(self):
        '''
        UNIT TEST: package has author string
        '''
        import publishing.withsphinx as pubwsphinx
        self.assertTrue(isinstance(pubwsphinx.__author__, str))
        self.assertEqual(pubwsphinx.__author__, _EXPECT_AUTHOR)

    def test_package_has_author_email_string(self):
        '''
        UNIT TEST: package has author email string
        '''
        import publishing.withsphinx as pubwsphinx
        self.assertTrue(isinstance(pubwsphinx.__author_email__, str))
        self.assertEqual(pubwsphinx.__author_email__, _EXPECT_AUTHOR_EMAIL)


if __name__ == "__main__":
    unittest.main()
