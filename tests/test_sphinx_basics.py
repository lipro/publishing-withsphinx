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
test_sphinx_basics
~~~~~~~~~~~~~~~~~~

This module contains basic functional tests over all supported extensions
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

import re
from tests import util


class TestCaseSphinxBasics(util.TestCasePublishingSphinx):

    @util.with_epub_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_epub(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build epub2 from all test fixtures
        '''
        app.builder.build_all()

        # check file
        for f in [
                'index.epub',
        #       'index.xhtml',  # NOQA
        #       'genindex.xhtml',  # NOQA
        #       'py-modindex.xhtml',  # NOQA
        #       'test-contrib-ansi/index.xhtml',  # NOQA
        #       'test-contrib-argparse/index.xhtml',  # NOQA
        #       'test-contrib-argparse/main.xhtml',  # NOQA
        #       'test-contrib-argparse/subcommand.xhtml',  # NOQA
        #       'test-contrib-autoprogram/index.xhtml',  # NOQA
        #       'test-contrib-bibtex/index.xhtml',  # NOQA
        #       'test-contrib-blockdiag/index.xhtml',  # NOQA
        #       'test-contrib-email/index.xhtml',  # NOQA
        #       'test-contrib-embedly/index.xhtml',  # NOQA
        #       'test-contrib-inlinesyntaxhighlight/index.xhtml',  # NOQA
        #       'test-contrib-programoutput/index.xhtml',  # NOQA
        #       'test-contrib-spelling/index.xhtml',  # NOQA
        #       'test-contrib-spelling/test_body.xhtml',  # NOQA
        #       'test-contrib-spelling/test_ignore_literals.xhtml',  # NOQA
        #       'test-contrib-spelling/test_title.xhtml',  # NOQA
        #       'test-contrib-tikz/index.xhtml',  # NOQA
        #       'test-ext-autodoc/index.xhtml',  # NOQA
        #       'test-ext-autosummary/index.xhtml',  # NOQA
        #       'test-ext-autosummary/autosummary.xhtml',  # NOQA
        #       'test-ext-autosummary/autosummary/an_example_pypi_project.xhtml',  # NOQA
        #       'test-ext-autosummary/autosummary/an_example_pypi_project.useful_1.xhtml',  # NOQA
        #       'test-ext-autosummary/autosummary/an_example_pypi_project.useful_2.xhtml',  # NOQA
        #       'test-ext-coverage/index.xhtml',  # NOQA
        #       'test-ext-doctest/index.xhtml',  # NOQA
        #       'test-ext-extlinks/index.xhtml',  # NOQA
        #       'test-ext-ifconfig/index.xhtml',  # NOQA
        #       'test-ext-math/index.xhtml',  # NOQA
        #       'test-ext-math/math.xhtml',  # NOQA
        #       'test-ext-todo/index.xhtml',  # NOQA
        #       'test-ext-todo/foo.xhtml',  # NOQA
        #       'test-ext-todo/bar.xhtml',  # NOQA
        ]:
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_devhelp_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_devhelp(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build devhelp from all test fixtures
        '''
        app.builder.build_all()

        # check file
        for f in [
                'index.devhelp.gz',
                'index.html',
                'genindex.html',
                'py-modindex.html',
                'search.html',
                'test-contrib-ansi/index.html',
                'test-contrib-argparse/index.html',
                'test-contrib-argparse/main.html',
                'test-contrib-argparse/subcommand.html',
                'test-contrib-autoprogram/index.html',
                'test-contrib-bibtex/index.html',
                'test-contrib-blockdiag/index.html',
                'test-contrib-email/index.html',
                'test-contrib-embedly/index.html',
                'test-contrib-inlinesyntaxhighlight/index.html',
                'test-contrib-programoutput/index.html',
                'test-contrib-spelling/index.html',
                'test-contrib-spelling/test_body.html',
                'test-contrib-spelling/test_ignore_literals.html',
                'test-contrib-spelling/test_title.html',
                'test-contrib-tikz/index.html',
                'test-ext-autodoc/index.html',
                'test-ext-autosummary/index.html',
                'test-ext-autosummary/autosummary.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_1.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_2.html',
                'test-ext-coverage/index.html',
                'test-ext-doctest/index.html',
                'test-ext-extlinks/index.html',
                'test-ext-ifconfig/index.html',
                'test-ext-math/index.html',
                'test-ext-math/math.html',
                'test-ext-todo/index.html',
                'test-ext-todo/foo.html',
                'test-ext-todo/bar.html',
        ]:
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_testroot_app(
        buildername='html',
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build html from all test fixtures
        '''
        app.builder.build_all()

        # check file
        for f in [
                'index.html',
                'genindex.html',
                'py-modindex.html',
                'search.html',
                'searchindex.js',
                'test-contrib-ansi/index.html',
                'test-contrib-argparse/index.html',
                'test-contrib-argparse/main.html',
                'test-contrib-argparse/subcommand.html',
                'test-contrib-autoprogram/index.html',
                'test-contrib-bibtex/index.html',
                'test-contrib-blockdiag/index.html',
                'test-contrib-email/index.html',
                'test-contrib-embedly/index.html',
                'test-contrib-inlinesyntaxhighlight/index.html',
                'test-contrib-programoutput/index.html',
                'test-contrib-spelling/index.html',
                'test-contrib-spelling/test_body.html',
                'test-contrib-spelling/test_ignore_literals.html',
                'test-contrib-spelling/test_title.html',
                'test-contrib-tikz/index.html',
                'test-ext-autodoc/index.html',
                'test-ext-autosummary/index.html',
                'test-ext-autosummary/autosummary.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_1.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_2.html',
                'test-ext-coverage/index.html',
                'test-ext-doctest/index.html',
                'test-ext-extlinks/index.html',
                'test-ext-ifconfig/index.html',
                'test-ext-math/index.html',
                'test-ext-math/math.html',
                'test-ext-todo/index.html',
                'test-ext-todo/foo.html',
                'test-ext-todo/bar.html',

        ]:
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_htmlhelp_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_htmlhelp(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build htmlhelp from all test fixtures
        '''
        app.builder.build_all()

        # check file
        for f in [
                'index.hhc',
                'index.hhk',
                'index.hhp',
                'index.html',
                'genindex.html',
                'py-modindex.html',
                'test-contrib-ansi/index.html',
                'test-contrib-argparse/index.html',
                'test-contrib-argparse/main.html',
                'test-contrib-argparse/subcommand.html',
                'test-contrib-autoprogram/index.html',
                'test-contrib-bibtex/index.html',
                'test-contrib-blockdiag/index.html',
                'test-contrib-email/index.html',
                'test-contrib-embedly/index.html',
                'test-contrib-inlinesyntaxhighlight/index.html',
                'test-contrib-programoutput/index.html',
                'test-contrib-spelling/index.html',
                'test-contrib-spelling/test_body.html',
                'test-contrib-spelling/test_ignore_literals.html',
                'test-contrib-spelling/test_title.html',
                'test-contrib-tikz/index.html',
                'test-ext-autodoc/index.html',
                'test-ext-autosummary/index.html',
                'test-ext-autosummary/autosummary.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_1.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_2.html',
                'test-ext-coverage/index.html',
                'test-ext-doctest/index.html',
                'test-ext-extlinks/index.html',
                'test-ext-ifconfig/index.html',
                'test-ext-math/index.html',
                'test-ext-math/math.html',
                'test-ext-todo/index.html',
                'test-ext-todo/foo.html',
                'test-ext-todo/bar.html',
        ]:
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_json_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_json(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build json from all test fixtures
        '''
        app.builder.build_all()

        # check file
        for f in [
                'index.fjson',
                'genindex.fjson',
                'py-modindex.fjson',
                'search.fjson',
                'searchindex.json',
                'test-contrib-ansi/index.fjson',
                'test-contrib-argparse/index.fjson',
                'test-contrib-argparse/main.fjson',
                'test-contrib-argparse/subcommand.fjson',
                'test-contrib-autoprogram/index.fjson',
                'test-contrib-bibtex/index.fjson',
                'test-contrib-blockdiag/index.fjson',
                'test-contrib-email/index.fjson',
                'test-contrib-embedly/index.fjson',
                'test-contrib-inlinesyntaxhighlight/index.fjson',
                'test-contrib-programoutput/index.fjson',
                'test-contrib-spelling/index.fjson',
                'test-contrib-spelling/test_body.fjson',
                'test-contrib-spelling/test_ignore_literals.fjson',
                'test-contrib-spelling/test_title.fjson',
                'test-contrib-tikz/index.fjson',
                'test-ext-autodoc/index.fjson',
                'test-ext-autosummary/index.fjson',
                'test-ext-autosummary/autosummary.fjson',
                'test-ext-autosummary/autosummary/an_example_pypi_project.fjson',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_1.fjson',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_2.fjson',
                'test-ext-coverage/index.fjson',
                'test-ext-doctest/index.fjson',
                'test-ext-extlinks/index.fjson',
                'test-ext-ifconfig/index.fjson',
                'test-ext-math/index.fjson',
                'test-ext-math/math.fjson',
                'test-ext-todo/index.fjson',
                'test-ext-todo/foo.fjson',
                'test-ext-todo/bar.fjson',
        ]:
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_latex_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build latex from all test fixtures
        '''
        app.builder.build_all()

        # check files
        for f in [
                'index.tex',
                'sphinx.sty',
                'Makefile',
        ]:
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_manpage_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_manpage(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build manpage from all test fixtures
        '''
        app.builder.build_all()

        # check files
        p = util.path(app.outdir / 'index.7')
        self.logger.debug('check is file: %r', p)
        self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_pseudoxml_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_pseudoxml(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build pseudoxml from all test fixtures
        '''
        app.builder.build_all()

        # check file
        for f in [
                'index.pseudoxml',
                'test-contrib-ansi/index.pseudoxml',
                'test-contrib-argparse/index.pseudoxml',
                'test-contrib-argparse/main.pseudoxml',
                'test-contrib-argparse/subcommand.pseudoxml',
                'test-contrib-autoprogram/index.pseudoxml',
                'test-contrib-bibtex/index.pseudoxml',
                'test-contrib-blockdiag/index.pseudoxml',
                'test-contrib-email/index.pseudoxml',
                'test-contrib-embedly/index.pseudoxml',
                'test-contrib-inlinesyntaxhighlight/index.pseudoxml',
                'test-contrib-programoutput/index.pseudoxml',
                'test-contrib-spelling/index.pseudoxml',
                'test-contrib-spelling/test_body.pseudoxml',
                'test-contrib-spelling/test_ignore_literals.pseudoxml',
                'test-contrib-spelling/test_title.pseudoxml',
                'test-contrib-tikz/index.pseudoxml',
                'test-ext-autodoc/index.pseudoxml',
                'test-ext-autosummary/index.pseudoxml',
                'test-ext-autosummary/autosummary.pseudoxml',
                'test-ext-autosummary/autosummary/an_example_pypi_project.pseudoxml',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_1.pseudoxml',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_2.pseudoxml',
                'test-ext-coverage/index.pseudoxml',
                'test-ext-doctest/index.pseudoxml',
                'test-ext-extlinks/index.pseudoxml',
                'test-ext-ifconfig/index.pseudoxml',
                'test-ext-math/index.pseudoxml',
                'test-ext-math/math.pseudoxml',
                'test-ext-todo/index.pseudoxml',
                'test-ext-todo/foo.pseudoxml',
                'test-ext-todo/bar.pseudoxml',
        ]:
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_qthelp_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_qthelp(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build qthelp from all test fixtures
        '''
        app.builder.build_all()

        # check file
        for f in filter(self.can_found_this_qthelp_file, [
                'index.qhcp',
                'index.qhp',
                'index.html',
                'genindex.html',
                'py-modindex.html',
                'search.html',
                'test-contrib-ansi/index.html',
                'test-contrib-argparse/index.html',
                'test-contrib-argparse/main.html',
                'test-contrib-argparse/subcommand.html',
                'test-contrib-autoprogram/index.html',
                'test-contrib-bibtex/index.html',
                'test-contrib-blockdiag/index.html',
                'test-contrib-email/index.html',
                'test-contrib-embedly/index.html',
                'test-contrib-inlinesyntaxhighlight/index.html',
                'test-contrib-programoutput/index.html',
                'test-contrib-spelling/index.html',
                'test-contrib-spelling/test_body.html',
                'test-contrib-spelling/test_ignore_literals.html',
                'test-contrib-spelling/test_title.html',
                'test-contrib-tikz/index.html',
                'test-ext-autodoc/index.html',
                'test-ext-autosummary/index.html',
                'test-ext-autosummary/autosummary.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_1.html',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_2.html',
                'test-ext-coverage/index.html',
                'test-ext-doctest/index.html',
                'test-ext-extlinks/index.html',
                'test-ext-ifconfig/index.html',
                'test-ext-math/index.html',
                'test-ext-math/math.html',
                'test-ext-todo/index.html',
                'test-ext-todo/foo.html',
                'test-ext-todo/bar.html',
        ]):
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_texinfo_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_texinfo(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build texinfo from all test fixtures
        '''
        app.builder.build_all()

        # check files
        for f in [
                'index.texi',
                'Makefile',
        ]:
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_text_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build text from all test fixtures
        '''
        app.builder.build_all()

        # check files
        for f in [
                'index.txt',
                'test-contrib-ansi/index.txt',
                'test-contrib-argparse/index.txt',
                'test-contrib-argparse/main.txt',
                'test-contrib-argparse/subcommand.txt',
                'test-contrib-autoprogram/index.txt',
                'test-contrib-bibtex/index.txt',
                'test-contrib-blockdiag/index.txt',
                'test-contrib-email/index.txt',
                'test-contrib-embedly/index.txt',
                'test-contrib-inlinesyntaxhighlight/index.txt',
                'test-contrib-programoutput/index.txt',
                'test-contrib-spelling/index.txt',
                'test-contrib-spelling/test_body.txt',
                'test-contrib-spelling/test_ignore_literals.txt',
                'test-contrib-spelling/test_title.txt',
                'test-contrib-tikz/index.txt',
                'test-ext-autodoc/index.txt',
                'test-ext-autosummary/index.txt',
                'test-ext-autosummary/autosummary.txt',
                'test-ext-autosummary/autosummary/an_example_pypi_project.txt',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_1.txt',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_2.txt',
                'test-ext-coverage/index.txt',
                'test-ext-doctest/index.txt',
                'test-ext-extlinks/index.txt',
                'test-ext-ifconfig/index.txt',
                'test-ext-math/index.txt',
                'test-ext-math/math.txt',
                'test-ext-todo/index.txt',
                'test-ext-todo/foo.txt',
                'test-ext-todo/bar.txt',
        ]:
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_xml_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_build_xml(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can build xml from all test fixtures
        '''
        app.builder.build_all()

        # check file
        for f in [
                'index.xml',
                'test-contrib-ansi/index.xml',
                'test-contrib-argparse/index.xml',
                'test-contrib-argparse/main.xml',
                'test-contrib-argparse/subcommand.xml',
                'test-contrib-autoprogram/index.xml',
                'test-contrib-bibtex/index.xml',
                'test-contrib-blockdiag/index.xml',
                'test-contrib-email/index.xml',
                'test-contrib-embedly/index.xml',
                'test-contrib-inlinesyntaxhighlight/index.xml',
                'test-contrib-programoutput/index.xml',
                'test-contrib-spelling/index.xml',
                'test-contrib-spelling/test_body.xml',
                'test-contrib-spelling/test_ignore_literals.xml',
                'test-contrib-spelling/test_title.xml',
                'test-contrib-tikz/index.xml',
                'test-ext-autodoc/index.xml',
                'test-ext-autosummary/index.xml',
                'test-ext-autosummary/autosummary.xml',
                'test-ext-autosummary/autosummary/an_example_pypi_project.xml',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_1.xml',
                'test-ext-autosummary/autosummary/an_example_pypi_project.useful_2.xml',
                'test-ext-coverage/index.xml',
                'test-ext-doctest/index.xml',
                'test-ext-extlinks/index.xml',
                'test-ext-ifconfig/index.xml',
                'test-ext-math/index.xml',
                'test-ext-math/math.xml',
                'test-ext-todo/index.xml',
                'test-ext-todo/foo.xml',
                'test-ext-todo/bar.xml',
        ]:
            p = util.path(app.outdir / f)
            self.logger.debug('check is file: %r', p)
            self.assertTrue(p.isfile(), 'missing file ' + p)

    @util.with_coverage_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_doc_coverage(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can collect coverage from all test fixtures
        '''
        app.builder.build_all()
        print(status.getvalue())
        print(warning.getvalue())

        # check file for C/C++ coverage results
        p = util.path(app.outdir / 'c.txt')
        self.logger.debug('check is file: %r', p)
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
        self.logger.debug('check is file: %r', p)
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # validate Python coverage results
        r = re.compile(
            '(?ms)' '^Undocumented Python objects$'
            '.*'    '^===========================$'
            '.*'    '^an_example_pypi_project$'
            '.*'    '^-----------------------$'
            '.*'    '^Functions:$'
            '.*'    '^ \* start$'
            '.*'    '^an_example_pypi_project\.useful_1$'
            '.*'    '^--------------------------------$'
            '.*'    '^Functions:$'
            '.*'    '^ \* public_fn_without_docstring$'
            '.*'    '^an_example_pypi_project\.useful_2$'
            '.*'    '^--------------------------------$'
            '.*'    '^Functions:$'
            '.*'    '^ \* public_fn_with_googley_docstring$'
            '.*'    '^ \* public_fn_without_docstring$'
            '.*'    '^hello$'
            '.*'    '^-----$'
            '.*'    '^Functions:$'
            '.*'    '^ \* hello$'
            '.*'    '^useful_1$'
            '.*'    '^--------$'
            '.*'    '^Classes:$'
            '.*'    '^ \* MyPublicClass'
        )
        self.assertRegex(c, r)

        r = re.compile(
            '(?ms)' '^useful_2$'
        )
        self.assertNotRegex(c, r)

    @util.with_doctest_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
        },
    )
    def test_doc_doctest(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can run and summarize embedded tests in all test fixtures
        '''
        app.builder.build_all()
        print(status.getvalue())
        print(warning.getvalue())

        # check file for doctest results
        p = util.path(app.outdir / 'output.txt')
        self.logger.debug('check is file: %r', p)
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # validate doctest results
        r = re.compile(
            '(?ms)' '^Document: test-ext-autodoc/index$'
            '.*'    '^--------------------------------$'
            '.*'    '^Document: test-ext-doctest/index$'
            '.*'    '^--------------------------------$'
            '.*'    '^Doctest summary$'
            '.*'    '^===============$'
            '.*'    '[1-9][0-9]*\s+tests'
            '.*'    '0\s+failures\s+in\s+tests'
            '.*'    '0\s+failures\s+in\s+setup\s+code'
            '.*'    '0\s+failures\s+in\s+cleanup\s+code'
        )
        self.assertRegex(c, r)

        r = re.compile(
            '(?ms)' '0\s+tests'
        )
        self.assertNotRegex(c, r)

    @util.with_spelling_app(
        confoverrides={
            'autosummary_generate': True,
            'embedly_key': '899ef656b46c11e099364040d3dc5c07',
            'embedly_timeout': 120,
            'tikz_tikzlibraries': 'arrows,matrix,calendar,folding',
            'spelling_lang': 'en_US',
            'spelling_word_list_filename': 'test-contrib-spelling/spelling_wordlist.txt',
            'spelling_show_suggestions': True,
        },
    )
    def test_doc_spelling(self, app, status, warning):
        '''
        FUNCTIONAL TEST: can test and summarize text spelling in all test fixtures
        '''
        app.builder.build_all()
        print(status.getvalue())
        print(warning.getvalue())

        # check file for doctest results
        p = util.path(app.outdir / 'output.txt')
        self.logger.debug('check is file: %r', p)
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # validate expected misspelled words
        r = re.compile(
            '(?ms)' '\(mispelled\)' '.*' '"misspelled"'
            '.*'    '\(txt\)' '.*' '"text"'
            '.*'    '\(Speeling\)' '.*' '"Spelling"'
        )
        self.assertRegex(c, r)

        # validate misspelled words expected to ignore
        r = re.compile(
            '(?ms)' '\(ignoreed\)'
            '.*'    '\(litterals\)'
        )
        self.assertNotRegex(c, r)

        # validate unknown words expected to set valid by word list
        r = re.compile('\(sphinxcontrib\)')
        self.assertNotRegex(c, r)
        r = re.compile('\(Inline\)')
        self.assertNotRegex(c, r)


if __name__ == "__main__":
    util.main()
