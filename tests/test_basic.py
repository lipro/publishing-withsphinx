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
This modules contains basic functional tests for the publishing.withsphinx module.
'''

import sys
from sphinx_testing import with_app
from sphinx_testing.path import path

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

if sys.version_info < (3,):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
    unittest.TestCase.assertRegex = unittest.TestCase.assertRegexpMatches
    unittest.TestCase.assertNotRegex = unittest.TestCase.assertNotRegexpMatches

with_spell_app = with_app(
    buildername='spelling',
    srcdir='tests/docs/basic/',
)

with_doctest_app = with_app(
    buildername='doctest',
    srcdir='tests/docs/basic/',
)

with_coverage_app = with_app(
    buildername='coverage',
    srcdir='tests/docs/basic/',
)

with_text_app = with_app(
    buildername='text',
    srcdir='tests/docs/basic/',
)

with_html_app = with_app(
    buildername='html',
    srcdir='tests/docs/basic/',
)

with_singlehtml_app = with_app(
    buildername='singlehtml',
    srcdir='tests/docs/basic/',
)

with_latex_app = with_app(
    buildername='latex',
    srcdir='tests/docs/basic/',
)


with_json_app = with_app(
    buildername='json',
    srcdir='tests/docs/basic/',
)


class TestSphinxcontribPublishingBasicHTML(unittest.TestCase):

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

    @with_spell_app
    def test_build_spell(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can test spelling of documentation
        '''
        app.builder.build_all()

        # check file
        p = path(app.outdir / 'output.txt')
        self.assertTrue(p.isfile())

        # fetch content
        r = p.read_text(encoding='utf-8')

        # validate content
        self.assertRegex(r, 'tikz\.rst:[0-9]:\s+\(TikZ\)')
        self.assertNotRegex(r, 'todo\.rst:[0-9]:\s+\(Todo\)')

    @with_doctest_app
    def test_build_doctest(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can run embedded tests in documentation
        '''
        app.builder.build_all()

        # check file
        p = path(app.outdir / 'output.txt')
        self.assertTrue(p.isfile())

        # fetch content
        r = p.read_text(encoding='utf-8')

        # validate content
        self.assertRegex(r, 'Document:\s+autodoc')
        self.assertRegex(r, 'Document:\s+doctest')
        self.assertNotRegex(r, '0\s+tests')
        self.assertRegex(r, '[1-9][0-9]*\s+tests')
        self.assertRegex(r, '0\s+failures\s+in\s+tests')
        self.assertRegex(r, '0\s+failures\s+in\s+setup\s+code')
        self.assertRegex(r, '0\s+failures\s+in\s+cleanup\s+code')

    @with_coverage_app
    def test_build_coverage(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can test coverag of documentation
        '''
        app.builder.build_all()

        # check file for C/C++ coverage results
        p = path(app.outdir / 'c.txt')
        self.assertTrue(p.isfile())

        # fetch content
        # r = p.read_text(encoding='utf-8')

        # check file for Python coverage results
        p = path(app.outdir / 'python.txt')
        self.assertTrue(p.isfile())

        # fetch content
        # r = p.read_text(encoding='utf-8')

    @with_text_app
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build text from documentation
        '''
        app.builder.build_all()

    @with_html_app
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build html from documentation
        '''
        app.builder.build_all()

    @with_singlehtml_app
    def test_build_singlehtml(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build singlehtml from documentation
        '''
        app.builder.build_all()

        # check file
        p = path(app.outdir / 'index.html')
        self.assertTrue(p.isfile())

        # fetch content
        # r = p.read_text(encoding='utf-8')

    @with_latex_app
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build latex from documentation
        '''
        app.builder.build_all()

        # check file
        p = path(app.outdir / 'basic-functional-tests.tex')
        self.assertTrue(p.isfile())

        # fetch content
        # r = p.read_text(encoding='utf-8')

    @with_json_app
    def test_build_json(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build json from documentation
        '''
        app.builder.build_all()


if __name__ == "__main__":
    unittest.main()
