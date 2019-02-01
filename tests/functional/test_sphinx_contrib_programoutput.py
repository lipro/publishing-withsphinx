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
test_sphinx_contrib_programoutput
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinxcontrib.programoutput
extension as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests.functional import fixtures

import re


class TestCaseSphinxContribProgramOutput(fixtures.TestCaseFunctionalPublishingSphinx):

    # TODO: Remove ANSI code sequencies when programoutput will
    #       support the Sphinx extension sphinxcontrib-ansi again.
    #
    # sphinxcontrib-programoutput v0.8.0 with ANSI supported:
    #   'ANSI'
    #
    # sphinxcontrib-programoutput v0.10.0 w/o ANSI support anymore:
    #   '\x1b\[31;1mANSI\x1b\[0m'
    #
    def _get_ansi_string(self):
        if fixtures.sphinx_version < '1.3.5':
            return r'ANSI'
        else:
            return r'\x1b\[31;1mANSI\x1b\[0m'

    # TODO: Evaluate the specific option 'programoutput_use_ansi'
    #       when programoutput will support the Sphinx extension
    #       sphinxcontrib-ansi again.
    @fixtures.with_html_app(
        testroot='contrib-programoutput',
        confoverrides={
            'programoutput_use_ansi': True,
        },
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.programoutput: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check program output documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'<p>Include the output of command in the documentation:</p>') + '.*'
            + re.escape(r'<pre>') + '.*' + re.escape(r'.. ansi-block::') + '.*'
            + re.escape(r'This is a ') + self._get_ansi_string() + re.escape(r' control sequence.') + '.*'
            + re.escape(r'</pre>') + '.*' + re.escape(r'usage: python') + '.*'
            + re.escape(r'Options and arguments') + '.*'
            + re.escape(r'<p>Same, but with enabled prompt option:</p>') + '.*' + re.escape(r'<pre>') + '.*'
            + re.escape(r'$ cat ${TEST_FIXTURES_ROOTS}/test-contrib-ansi/index.rst') + '.*'
            + re.escape(r'.. ansi-block::') + '.*'
            + re.escape(r'This is a ') + self._get_ansi_string() + re.escape(r' control sequence.') + '.*'
            + re.escape(r'</pre>') + '.*' + re.escape(r'<pre>') + '.*' + re.escape(r'$ python --help') + '.*'
            + re.escape(r'usage: python') + '.*' + re.escape(r'Options and arguments') + '.*' + re.escape(r'</pre>')
        )
        self.assertRegex(c, r)

    # TODO: Evaluate the specific option 'programoutput_use_ansi'
    #       when programoutput will support the Sphinx extension
    #       sphinxcontrib-ansi again.
    @fixtures.with_latex_app(
        testroot='contrib-programoutput',
        confoverrides={
            'programoutput_use_ansi': True,
        },
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.programoutput: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check program output documentation
        # TODO: add support for latex backend of this extention
        r = re.compile(
            '(?ms)'
            + re.escape(r'Include the output of command in the documentation:') + '.*'
            + re.escape(r'\begin{' + self.get_latex_verbatim() + r'}[commandchars=\\\{\}]') + '.*'
            + re.escape(r'.. ansi\PYGZhy{}block::') + '.*'
            + re.escape(r'This is a ') + self._get_ansi_string() + re.escape(r' control sequence.') + '.*'
            + re.escape(r'\end{' + self.get_latex_verbatim() + r'}') + '.*' + re.escape(r'usage: python') + '.*'
            + re.escape(r'Options and arguments') + '.*' + re.escape(r'Same, but with enabled prompt option:') + '.*'
            + re.escape(r'\begin{' + self.get_latex_verbatim() + r'}[commandchars=\\\{\}]') + '.*'
            + re.escape(r'\PYGZdl{} cat \PYGZdl{}\PYGZob{}TEST\PYGZus{}FIXTURES\PYGZus{}ROOTS\PYGZcb{}')
            + re.escape(r'/test\PYGZhy{}contrib\PYGZhy{}ansi/index.rst') + '.*'
            + re.escape(r'.. ansi\PYGZhy{}block::') + '.*'
            + re.escape(r'This is a ') + self._get_ansi_string() + re.escape(r' control sequence.') + '.*'
            + re.escape(r'\end{' + self.get_latex_verbatim() + r'}') + '.*'
            + re.escape(r'\begin{' + self.get_latex_verbatim() + r'}[commandchars=\\\{\}]') + '.*'
            + re.escape(r'\PYGZdl{} python \PYGZhy{}\PYGZhy{}help') + '.*'
            + re.escape(r'usage: python') + '.*' + re.escape(r'Options and arguments') + '.*'
            + re.escape(r'\end{' + self.get_latex_verbatim() + r'}')
        )
        self.assertRegex(c, r)

    # TODO: Evaluate the specific option 'programoutput_use_ansi'
    #       when programoutput will support the Sphinx extension
    #       sphinxcontrib-ansi again.
    @fixtures.with_text_app(
        testroot='contrib-programoutput',
        confoverrides={
            'programoutput_use_ansi': True,
        },
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.programoutput: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check program output documentation
        r = re.compile(
            '(?ms)'
            + re.escape(r'Include the output of command in the documentation:') + '.*'
            + re.escape(r'   .. ansi-block::') + '.*'
            + re.escape(r'      This is a ') + self._get_ansi_string() + re.escape(r' control sequence.') + '.*'
            + re.escape(r'   usage: python') + '.*'
            + re.escape(r'   Options and arguments') + '.*'
            + re.escape(r'Same, but with enabled prompt option:') + '.*'
            + re.escape(r'   $ cat ${TEST_FIXTURES_ROOTS}/test-contrib-ansi/index.rst') + '.*'
            + re.escape(r'   .. ansi-block::') + '.*'
            + re.escape(r'      This is a ') + self._get_ansi_string() + re.escape(r' control sequence.') + '.*'
            + re.escape(r'   $ python --help') + '.*'
            + re.escape(r'   usage: python') + '.*'
            + re.escape(r'   Options and arguments')
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
