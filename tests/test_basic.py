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
        r = p.read_text(encoding='utf-8')

        # validate content
        # TODO: self.assertRegex(r, 'hello')

        # check file for Python coverage results
        p = path(app.outdir / 'python.txt')
        self.assertTrue(p.isfile())

        # fetch content
        r = p.read_text(encoding='utf-8')

        # validate content
        self.assertRegex(r, 'an_example_pypi_project')
        self.assertRegex(r, 'an_example_pypi_project\.useful_1')
        self.assertRegex(r, 'an_example_pypi_project\.useful_2')
        self.assertRegex(r, 'hello')
        self.assertRegex(r, 'useful_1')

    @with_text_app
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build text from documentation
        '''
        app.builder.build_all()

        # sphinx.ext.autodoc
        p = path(app.outdir / 'autodoc.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'A\s+pypi\s+demonstration\s+vehicle\.')
        self.assertRegex(r, 'class\s+an_example_pypi_project\.useful_1\.MyPublicClass')
        self.assertRegex(r, 'an_example_pypi_project\.useful_1\.public_fn_with_googley_docstring')
        self.assertRegex(r, 'an_example_pypi_project\.useful_1\.public_fn_with_sphinxy_docstring')
        self.assertRegex(r, 'an_example_pypi_project\.useful_2\.public_fn_with_sphinxy_docstring')
        self.assertRegex(r, 'an_example_pypi_project\.useful_2\._private_fn_with_docstring')
        self.assertRegex(r, 'class\s+an_example_pypi_project\.useful_2\.MyPublicClass')

        # sphinx.ext.autosummary
        p = path(app.outdir / 'autosummary.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'A\s+pypi\s+demonstration\s+vehicle\.')
        self.assertRegex(r, 'A\s+very\s+useful\s+module\s+indeed\.')
        self.assertRegex(r, 'an_example_pypi_project')
        self.assertRegex(r, 'an_example_pypi_project\.useful_1')
        self.assertRegex(r, 'an_example_pypi_project\.useful_2')

        p = path(app.outdir / 'autosummary' / 'an_example_pypi_project.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'This\s+starts\s+this\s+module\s+running\s+\.\.\.')

        p = path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_1.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'We\s+use\s+this\s+as\s+a\s+public\s+class\s+example\s+class\.')

        p = path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_2.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'We\s+use\s+this\s+as\s+a\s+public\s+class\s+example\s+class\.')

        # sphinx.ext.extlinks
        p = path(app.outdir / 'extlinks.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'Datasheet\s+Archive\s+\(IDXF\):\s+Scans-048\/DSAGER000371')
        self.assertNotRegex(r, 'http:\/\/datasheet\.datasheetarchive\.com\/originals\/scans\/'
                               'Scans-048\/DSAGER000371\.pdf.*')
        self.assertRegex(r, 'Datasheet\s+Archive\s+\(MAIN\):\s+Datasheets-AE\/DSA5GERT0000353')
        self.assertNotRegex(r, 'http:\/\/datasheet\.datasheetarchive\.com\/originals\/distributors\/'
                               'Datasheets-AE\/DSA5GERT0000353\.pdf.*')

        # sphinx.ext.mathjax
        p = path(app.outdir / 'mathjax.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'Since\s+Pythagoras,\s+we\s+know\s+that\s+a\^2\s+\+\s+b\^2\s+=\s+c\^2\.')

        # sphinx.ext.todo
        p = path(app.outdir / 'todo.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'Todo:\s+Something to do\.')

        # sphinxcontrib.blockdiag
        p = path(app.outdir / 'blockdiag.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '[image]\s*[image]')

        # sphinxcontrib.email
        p = path(app.outdir / 'email.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'A\s+Bc\s+<a@bc.de>')

        # sphinxcontrib.embedly
        p = path(app.outdir / 'embedly.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'Monty\s+Python\s+<http:\/\/www\.montypython\.com\/>')
        self.assertRegex(r, 'Monty\s+Python\s+<http:\/\/www\.montypython\.net\/sounds\/lob\/16done\.wav>')
        self.assertRegex(r, 'Monty\s+Python\s+<http:\/\/www\.montypython\.com\/himg\/_0\.png>')
        self.assertRegex(r, 'Monty\s+Python.*\s+.*SPAM\s+<http:\/\/www\.youtube\.com/watch.*M_eYSuPKP3Y>')

        # sphinxcontrib.inlinesyntaxhighlight
        p = path(app.outdir / 'inlinesyntaxhighlight.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'This\s+is\s+a\s+address:\s+"40h"')
        self.assertRegex(r, 'This\s+is\s+a\s+code:\s+"0C"')
        self.assertRegex(r, 'This\s+is\s+a\s+port:\s+"20"')
        self.assertRegex(r, 'This\s+is\s+a\s+console\s+output:\s+"ERROR:\s+not\s+found\."')
        self.assertRegex(r, 'This\s+is\s+a\s+assembler\s+mnemonic:\s+"NOP"')

        # sphinxcontrib.programoutput
        p = path(app.outdir / 'programoutput.txt')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '\s*\$\s+cat\s+ansi\.rst')
        self.assertRegex(r, '\s*\.\.\s+ansi-block::')
        self.assertRegex(r, '\s*This\s+is\s+a\s+ANSI\s+control\s+sequence\.')

        # sphinxcontrib.tikz
        self.assertNotRegex(r, 'A\s+new\s+year\s+is\s+coming\s+soon\s+\.\.\.')

    @with_html_app
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build html from documentation
        '''
        app.builder.build_all()

        # sphinx.ext.autodoc
        p = path(app.outdir / 'autodoc.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'A\s+pypi\s+demonstration\s+vehicle\.')
        self.assertRegex(r, 'class\s+.*<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
                            '<(code|tt).*>MyPublicClass<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
                            '<(code|tt).*>public_fn_with_googley_docstring<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
                            '<(code|tt).*>public_fn_with_sphinxy_docstring<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
                            '<(code|tt).*>public_fn_with_sphinxy_docstring<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
                            '<(code|tt).*>_private_fn_with_docstring<\/(code|tt)>')
        self.assertRegex(r, 'class\s+.*<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
                            '<(code|tt).*>MyPublicClass<\/(code|tt)>')

        # sphinx.ext.autosummary
        p = path(app.outdir / 'autosummary.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'A\s+pypi\s+demonstration\s+vehicle\.')
        self.assertRegex(r, 'A\s+very\s+useful\s+module\s+indeed\.')
        self.assertRegex(r, 'an_example_pypi_project')
        self.assertRegex(r, 'an_example_pypi_project\.useful_1')
        self.assertRegex(r, 'an_example_pypi_project\.useful_2')

        p = path(app.outdir / 'autosummary' / 'an_example_pypi_project.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'This\s+starts\s+this\s+module\s+running\s+\.\.\.')

        p = path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_1.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'We\s+use\s+this\s+as\s+a\s+public\s+class\s+example\s+class\.')

        p = path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_2.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'We\s+use\s+this\s+as\s+a\s+public\s+class\s+example\s+class\.')

        # sphinx.ext.extlinks
        p = path(app.outdir / 'extlinks.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'http:\/\/datasheet\.datasheetarchive\.com\/originals\/scans\/'
                            'Scans-048\/DSAGER000371\.pdf.*'
                            'Datasheet\s+Archive\s+\(IDXF\):\s+Scans-048\/DSAGER000371')
        self.assertRegex(r, 'http:\/\/datasheet\.datasheetarchive\.com\/originals\/distributors\/'
                            'Datasheets-AE\/DSA5GERT0000353\.pdf.*'
                            'Datasheet\s+Archive\s+\(MAIN\):\s+Datasheets-AE\/DSA5GERT0000353')

        # sphinx.ext.mathjax
        p = path(app.outdir / 'mathjax.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<script\s+type="text\/javascript"\s+'
                            'src="http.*:\/\/cdn.mathjax.org\/mathjax\/latest\/MathJax\.js\?'
                            'config=TeX-AMS-MML_HTMLorMML"><\/script>')
        self.assertRegex(r, '<p>Since\s+Pythagoras,\s+we\s+know\s+that\s+<span\s+class="math">'
                            '\\\\\(a\^2\s+\+\s+b\^2\s+=\s+c\^2\\\\\)<\/span>\.<\/p>')

        # sphinx.ext.todo
        p = path(app.outdir / 'todo.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<p\s+class="first\s+admonition-title">Todo<\/p>')

        # sphinxcontrib.blockdiag
        p = path(app.outdir / 'blockdiag.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<svg\s+.*\s+xmlns="http:\/\/www.w3.org\/2000\/svg"')
        self.assertRegex(r, '<title>blockdiag<\/title>')

        # sphinxcontrib.email
        p = path(app.outdir / 'email.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'A\s+Bc\s+&lt;.*href="mailto:a&#37;&#52;&#48;bc&#46;de".*a.*bc.*de.*&gt;')

        # sphinxcontrib.embedly
        p = path(app.outdir / 'embedly.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<a\s+href="http:\/\/www\.montypython\.com\/"\s+.*>')
        self.assertRegex(r, '<a\s+href="http:\/\/www\.montypython\.net\/sounds\/lob\/16done\.wav"\s+.*>')
        self.assertRegex(r, 'src="https:\/\/i\.embed\.ly\/.*'
                            'url=http%3A%2F%2Fwww\.montypython\.com%2Fhimg%2F_0\.png&key=.*"\s+.*>')
        self.assertRegex(r, 'src="https:\/\/cdn\.embedly\.com\/.*'
                            'url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DM_eYSuPKP3Y.*&key=.*"\s+.*>')

        # sphinxcontrib.inlinesyntaxhighlight
        p = path(app.outdir / 'inlinesyntaxhighlight.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<p>This\s+is\s+a\s+address:\s+.*\s+class=".*hexdump.*".*40h.*<\/p>')
        self.assertRegex(r, '<p>This\s+is\s+a\s+code:\s+.*\s+class=".*hexdump.*".*0C.*<\/p>')
        self.assertRegex(r, '<p>This\s+is\s+a\s+port:\s+.*\s+class=".*hexdump.*".*20.*<\/p>')
        self.assertRegex(r, '<p>This\s+is\s+a\s+console\s+output:\s+.*\s+class=".*console.*".*'
                            'ERROR:\s+not\s+found\..*<\/p>')
        self.assertRegex(r, '<p>This\s+is\s+a\s+assembler\s+mnemonic:\s+.*\s+class=".*nasm.*".*NOP.*<\/p>')

        # sphinxcontrib.programoutput
        p = path(app.outdir / 'programoutput.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '\s*\$\s+cat\s+ansi\.rst')
        self.assertRegex(r, '\s*\.\.\s+ansi-block::')
        self.assertRegex(r, '\s*This\s+is\s+a\s+<span\s+class="ansi-red\s+ansi-bold">'
                            'ANSI<\/span>\s+control\s+sequence\.')

        # sphinxcontrib.tikz
        p = path(app.outdir / 'tikz.html')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<img\s+src=".*images\/tikz-.*\.svg"\s+alt="\[transform\s+shape,')
        self.assertRegex(r, 'A\s+new\s+year\s+is\s+coming\s+soon\s+\.\.\.')

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
        r = p.read_text(encoding='utf-8')

        # sphinx.ext.autodoc / sphinx.ext.autosummary
        self.assertRegex(r, 'A\s+pypi\s+demonstration\s+vehicle\.')
        self.assertRegex(r, 'A\s+very\s+useful\s+module\s+indeed\.')
        self.assertRegex(r, 'We\s+use\s+this\s+as\s+a\s+public\s+class\s+example\s+class\.')
        self.assertRegex(r, 'class\s+.*<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
                            '<(code|tt).*>MyPublicClass<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
                            '<(code|tt).*>public_fn_with_googley_docstring<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
                            '<(code|tt).*>public_fn_with_sphinxy_docstring<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
                            '<(code|tt).*>public_fn_with_sphinxy_docstring<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
                            '<(code|tt).*>_private_fn_with_docstring<\/(code|tt)>')
        self.assertRegex(r, 'class\s+.*<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
                            '<(code|tt).*>MyPublicClass<\/(code|tt)>')
        self.assertNotRegex(r, 'This\s+starts\s+this\s+module\s+running\s+\.\.\.')

        # sphinx.ext.extlinks
        self.assertRegex(r, 'http:\/\/datasheet\.datasheetarchive\.com\/originals\/scans\/'
                            'Scans-048\/DSAGER000371\.pdf.*'
                            'Datasheet\s+Archive\s+\(IDXF\):\s+Scans-048\/DSAGER000371')
        self.assertRegex(r, 'http:\/\/datasheet\.datasheetarchive\.com\/originals\/distributors\/'
                            'Datasheets-AE\/DSA5GERT0000353\.pdf.*'
                            'Datasheet\s+Archive\s+\(MAIN\):\s+Datasheets-AE\/DSA5GERT0000353')

        # sphinx.ext.mathjax
        self.assertRegex(r, '<script\s+type="text\/javascript"\s+'
                            'src="http.*:\/\/cdn.mathjax.org\/mathjax\/latest\/MathJax\.js\?'
                            'config=TeX-AMS-MML_HTMLorMML"><\/script>')
        self.assertRegex(r, '<p>Since\s+Pythagoras,\s+we\s+know\s+that\s+<span\s+class="math">'
                            '\\\\\(a\^2\s+\+\s+b\^2\s+=\s+c\^2\\\\\)<\/span>\.<\/p>')

        # sphinx.ext.todo
        self.assertRegex(r, '<p\s+class="first\s+admonition-title">Todo<\/p>')

        # sphinxcontrib.blockdiag
        self.assertRegex(r, '<svg\s+.*\s+xmlns="http:\/\/www.w3.org\/2000\/svg"')
        self.assertRegex(r, '<title>blockdiag<\/title>')

        # sphinxcontrib.email
        self.assertRegex(r, 'A\s+Bc\s+&lt;.*href="mailto:a&#37;&#52;&#48;bc&#46;de".*a.*bc.*de.*&gt;')

        # sphinxcontrib.embedly
        self.assertRegex(r, '<a\s+href="http:\/\/www\.montypython\.com\/"\s+.*>')
        self.assertRegex(r, '<a\s+href="http:\/\/www\.montypython\.net\/sounds\/lob\/16done\.wav"\s+.*>')
        self.assertRegex(r, 'src="https:\/\/i\.embed\.ly\/.*'
                            'url=http%3A%2F%2Fwww\.montypython\.com%2Fhimg%2F_0\.png&key=.*"\s+.*>')
        self.assertRegex(r, 'src="https:\/\/cdn\.embedly\.com\/.*'
                            'url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DM_eYSuPKP3Y.*&key=.*"\s+.*>')

        # sphinxcontrib.inlinesyntaxhighlight
        self.assertRegex(r, '<p>This\s+is\s+a\s+address:\s+.*\s+class=".*hexdump.*".*40h.*<\/p>')
        self.assertRegex(r, '<p>This\s+is\s+a\s+code:\s+.*\s+class=".*hexdump.*".*0C.*<\/p>')
        self.assertRegex(r, '<p>This\s+is\s+a\s+port:\s+.*\s+class=".*hexdump.*".*20.*<\/p>')
        self.assertRegex(r, '<p>This\s+is\s+a\s+console\s+output:\s+.*\s+class=".*console.*".*'
                            'ERROR:\s+not\s+found\..*<\/p>')
        self.assertRegex(r, '<p>This\s+is\s+a\s+assembler\s+mnemonic:\s+.*\s+class=".*nasm.*".*'
                            'NOP.*<\/p>')

        # FIXME: sphinxcontrib.programoutput
        self.assertRegex(r, '\s*\$\s+cat\s+ansi\.rst')
        self.assertRegex(r, '\s*\.\.\s+ansi-block::')
        self.assertRegex(r, '\s*This\s+is\s+a\s+ANSI\s+control\s+sequence\.')
        self.assertNotRegex(r, '\s*This\s+is\s+a\s+<span\s+class="ansi-red\s+ansi-bold">'
                               'ANSI<\/span>\s+control\s+sequence\.')

        # sphinxcontrib.tikz
        self.assertRegex(r, '<img\s+src=".*images\/tikz-.*\.svg"\s+alt="\[transform\s+shape,')
        self.assertRegex(r, 'A\s+new\s+year\s+is\s+coming\s+soon\s+\.\.\.')

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
        r = p.read_text(encoding='utf-8')

        # sphinx.ext.autodoc / sphinx.ext.autosummary
        self.assertRegex(r, 'A\s+pypi\s+demonstration\s+vehicle\.')
        self.assertRegex(r, 'A\s+very\s+useful\s+module\s+indeed\.')
        self.assertRegex(r, 'This\s+starts\s+this\s+module\s+running\s+\.\.\.')
        self.assertRegex(r, 'We\s+use\s+this\s+as\s+a\s+public\s+class\s+example\s+class\.')
        self.assertRegex(r, '\\\\.*strong\{class\s+\}'
                            '\\\\.*code\{an\\\\_example\\\\_pypi\\\\_project\.useful\\\\_1\.\}'
                            '\\\\.*bfcode\{MyPublicClass\}')
        self.assertRegex(r, '\\\\.*code\{an\\\\_example\\\\_pypi\\\\_project\.useful\\\\_1\.\}'
                            '\\\\.*bfcode\{public\\\\_fn\\\\_with\\\\_googley\\\\_docstring\}')
        self.assertRegex(r, '\\\\.*code\{an\\\\_example\\\\_pypi\\\\_project\.useful\\\\_1\.\}'
                            '\\\\.*bfcode\{public\\\\_fn\\\\_with\\\\_sphinxy\\\\_docstring\}')
        self.assertRegex(r, '\\\\.*code\{an\\\\_example\\\\_pypi\\\\_project\.useful\\\\_2\.\}'
                            '\\\\.*bfcode\{public\\\\_fn\\\\_with\\\\_sphinxy\\\\_docstring\}')
        self.assertRegex(r, '\\\\.*code\{an\\\\_example\\\\_pypi\\\\_project\.useful\\\\_2\.\}'
                            '\\\\.*bfcode\{\\\\_private\\\\_fn\\\\_with\\\\_docstring\}')
        self.assertRegex(r, '\\\\.*strong\{class\s+\}'
                            '\\\\.*code\{an\\\\_example\\\\_pypi\\\\_project\.useful\\\\_2\.\}'
                            '\\\\.*bfcode\{MyPublicClass\}')

        # sphinx.ext.extlinks
        self.assertRegex(r, '\\\\href\{http:\/\/datasheet\.datasheetarchive\.com\/originals\/scans\/'
                            'Scans-048\/DSAGER000371\.pdf\}\{'
                            'Datasheet\s+Archive\s+\(IDXF\):\s+Scans-048\/DSAGER000371\}')
        self.assertRegex(r, '\\\\href\{http:\/\/datasheet\.datasheetarchive\.com\/originals\/distributors\/'
                            'Datasheets-AE\/DSA5GERT0000353\.pdf\}\{'
                            'Datasheet\s+Archive\s+\(MAIN\):\s+Datasheets-AE\/DSA5GERT0000353\}')

        # sphinx.ext.mathjax
        self.assertRegex(r, 'Since\s+Pythagoras,\s+we\s+know\s+that\s+.*a\^2\s+\+\s+b\^2\s+=\s+c\^2.*\.')

        # sphinx.ext.todo
        self.assertRegex(r, '\\\\begin\{notice\}\{note\}\{Todo\}')

        # sphinxcontrib.blockdiag
        self.assertRegex(r, '\\\\.*includegraphics\{.*blockdiag-.*\\..*\}')

        # sphinxcontrib.email
        self.assertRegex(r, 'A\s+Bc\s+.*\\\\href\{mailto:a@bc\.de\}\{a@bc\.de\}')

        # sphinxcontrib.embedly
        self.assertRegex(r, 'Monty\s+Python\s+.*http:\/\/www\.montypython\.com\/')
        self.assertRegex(r, 'Monty\s+Python\s+.*http:\/\/www\.montypython\.net\/sounds\/lob\/16done\.wav')
        self.assertRegex(r, 'Monty\s+Python\s+.*http:\/\/www\.montypython\.com\/himg\/\\\\_0\.png')
        self.assertRegex(r, 'Monty\s+Python.*\s+.*SPAM\s+.*http:\/\/www\.youtube\.com/watch.*M\\\\_eYSuPKP3Y')

        # sphinxcontrib.inlinesyntaxhighlight
        self.assertRegex(r, 'This\s+is\s+a\s+address:\s+\\\\.*code\{40h\}')
        self.assertRegex(r, 'This\s+is\s+a\s+code:\s+\\\\.*code\{0C\}')
        self.assertRegex(r, 'This\s+is\s+a\s+port:\s+\\\\.*code\{20\}')
        self.assertRegex(r, 'This\s+is\s+a\s+console\s+output:\s+\\\\.*code\{ERROR:\s+not\s+found\.\}')
        self.assertRegex(r, 'This\s+is\s+a\s+assembler\s+mnemonic:\s+\\\\.*code\{NOP\}')

        # TODO: sphinxcontrib.programoutput

        # sphinxcontrib.tikz
        self.assertRegex(r, '\\\\begin\{figure\}\[.*\]\\\\centering\\\\begin\{tikzpicture\}')
        self.assertRegex(r, '\[transform\s+shape,')
        self.assertRegex(r, '\\\\end\{tikzpicture\}\\\\caption\{A\s+new\s+year\s+is\s+coming\s+soon\s+\.\.\.\}'
                            '\\\\end\{figure\}')

    @with_json_app
    def test_build_json(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build json from documentation
        '''
        app.builder.build_all()

        # sphinx.ext.autodoc
        p = path(app.outdir / 'autodoc.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'A\s+pypi\s+demonstration\s+vehicle\.')
        self.assertRegex(r, 'class\s+.*<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
                            '<(code|tt).*>MyPublicClass<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
                            '<(code|tt).*>public_fn_with_googley_docstring<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_1\.<\/(code|tt)>'
                            '<(code|tt).*>public_fn_with_sphinxy_docstring<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
                            '<(code|tt).*>public_fn_with_sphinxy_docstring<\/(code|tt)>')
        self.assertRegex(r, '<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
                            '<(code|tt).*>_private_fn_with_docstring<\/(code|tt)>')
        self.assertRegex(r, 'class\s+.*<(code|tt).*>an_example_pypi_project\.useful_2\.<\/(code|tt)>'
                            '<(code|tt).*>MyPublicClass<\/(code|tt)>')

        # sphinx.ext.autosummary
        p = path(app.outdir / 'autosummary.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'A\s+pypi\s+demonstration\s+vehicle\.')
        self.assertRegex(r, 'A\s+very\s+useful\s+module\s+indeed\.')
        self.assertRegex(r, 'an_example_pypi_project')
        self.assertRegex(r, 'an_example_pypi_project\.useful_1')
        self.assertRegex(r, 'an_example_pypi_project\.useful_2')

        p = path(app.outdir / 'autosummary' / 'an_example_pypi_project.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'This\s+starts\s+this\s+module\s+running\s+\.\.\.')

        p = path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_1.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'We\s+use\s+this\s+as\s+a\s+public\s+class\s+example\s+class\.')

        p = path(app.outdir / 'autosummary' / 'an_example_pypi_project.useful_2.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'We\s+use\s+this\s+as\s+a\s+public\s+class\s+example\s+class\.')

        # sphinx.ext.extlinks
        p = path(app.outdir / 'extlinks.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'http:\/\/datasheet\.datasheetarchive\.com\/originals\/scans\/'
                            'Scans-048\/DSAGER000371\.pdf.*'
                            'Datasheet\s+Archive\s+\(IDXF\):\s+Scans-048\/DSAGER000371')
        self.assertRegex(r, 'http:\/\/datasheet\.datasheetarchive\.com\/originals\/distributors\/'
                            'Datasheets-AE\/DSA5GERT0000353\.pdf.*'
                            'Datasheet\s+Archive\s+\(MAIN\):\s+Datasheets-AE\/DSA5GERT0000353')

        # sphinx.ext.mathjax
        p = path(app.outdir / 'mathjax.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<p>Since\s+Pythagoras,\s+we\s+know\s+that\s+<span\s+class=\\\\"math\\\\">'
                            '\\\\\\\\\(a\^2\s+\+\s+b\^2\s+=\s+c\^2\\\\\\\\\)<\/span>\.<\/p>')

        # sphinx.ext.todo
        p = path(app.outdir / 'todo.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<p\s+class=\\\\"first\s+admonition-title\\\\">Todo<\/p>')

        # sphinxcontrib.blockdiag
        p = path(app.outdir / 'blockdiag.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<svg\s+.*\s+xmlns=\\\\"http:\/\/www.w3.org\/2000\/svg\\\\"\s+.*'
                            '<title>blockdiag<\/title>')

        # sphinxcontrib.email
        p = path(app.outdir / 'email.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, 'A\s+Bc\s+&lt;.*href=\\\\"mailto:a&#37;&#52;&#48;bc&#46;de\\\\".*a.*bc.*de.*&gt;')

        # sphinxcontrib.embedly
        p = path(app.outdir / 'embedly.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<a\s+href=\\\\"http:\/\/www\.montypython\.com\/\\\\"\s+.*>')
        self.assertRegex(r, '<a\s+href=\\\\"http:\/\/www\.montypython\.net\/sounds\/lob\/16done\.wav\\\\"\s+.*>')
        self.assertRegex(r, 'src=\\\\"https:\/\/i\.embed\.ly\/.*'
                            'url=http%3A%2F%2Fwww\.montypython\.com%2Fhimg%2F_0\.png&key=.*\\\\"\s+.*>')
        self.assertRegex(r, 'src=\\\\"https:\/\/cdn\.embedly\.com\/.*'
                            'url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DM_eYSuPKP3Y.*&key=.*\\\\"\s+.*>')

        # sphinxcontrib.inlinesyntaxhighlight
        p = path(app.outdir / 'inlinesyntaxhighlight.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<p>This\s+is\s+a\s+address:\s+.*\s+class=\\\\".*hexdump.*\\\\".*40h.*<\/p>.*'
                            '<p>This\s+is\s+a\s+code:\s+.*\s+class=\\\\".*hexdump.*\\\\".*0C.*<\/p>.*'
                            '<p>This\s+is\s+a\s+port:\s+.*\s+class=\\\\".*hexdump.*\\\\".*20.*<\/p>.*'
                            '<p>This\s+is\s+a\s+console\s+output:\s+.*\s+class=\\\\".*console.*\\\\".*'
                            'ERROR:\s+not\s+found\..*<\/p>.*'
                            '<p>This\s+is\s+a\s+assembler\s+mnemonic:\s+.*\s+class=\\\\".*nasm.*\\\\".*'
                            'NOP.*<\/p>')

        # FIXME: sphinxcontrib.programoutput
        p = path(app.outdir / 'programoutput.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '\$\s+cat\s+ansi\.rst.*'
                            '\.\.\s+ansi-block::.*'
                            '\s*This\s+is\s+a\s+ANSI\s+control\s+sequence\.')
        self.assertNotRegex(r, 'This\s+is\s+a\s+<span\s+class=\\\\"ansi-red\s+ansi-bold\\\\">'
                               'ANSI<\/span>\s+control\s+sequence\.')

        # sphinxcontrib.tikz
        p = path(app.outdir / 'tikz.fjson')
        self.assertTrue(p.isfile())

        r = p.read_text(encoding='utf-8')
        self.assertRegex(r, '<img\s+src=\\\\".*images\/tikz-.*\.svg\\\\"\s+alt=\\\\"\[transform\s+shape,.*'
                            'A\s+new\s+year\s+is\s+coming\s+soon\s+\.\.\.')


if __name__ == "__main__":
    unittest.main()
