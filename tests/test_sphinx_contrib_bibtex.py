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
.. traceable:: VFY-SPHINXCONTRIB-BIBTEX
   :title: Verify sphinxcontrib-bibtex
   :category: SysVerify
   :parents: IMP-SPHINXCONTRIB-BIBTEX
   :verification_type: functional
   :verification_method: ci-test

This module contains basic functional tests of the sphinxcontrib.bibtex
extension as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.

.. traceable-graph::
   :tags: VFY-SPHINXCONTRIB-BIBTEX
   :relationships: parents:2, children
   :caption: Traces to the system requirement VFY-SPHINXCONTRIB-BIBTEX
'''

from __future__ import absolute_import

import re
from tests import util


class TestCaseSphinxContribBibTeX(util.TestCasePublishingSphinx):

    @util.with_html_app(
        testroot='contrib-bibtex',
    )
    def test_build_html(self, app, status, warning):
        '''
        .. traceable:: TST-SPHINXCONTRIB-BIBTEX-HTML
           :title: Test sphinxcontrib-bibtex can build html
           :category: SysTest
           :parents: VFY-SPHINXCONTRIB-BIBTEX
           :verification_type: functional
           :verification_method: ci-test
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check BibTeX entry
        # FIXME: avoid &nbsp; as whitespace character: 'Jan&nbsp;Ulrich'
        r = re.compile(
            '(?ms)' '<tr><td class="label">\[HB14\]</td>'
            '.*'    'Jan.*Ulrich Hasecke and Georg Brandl'
            '.*'    'ISBN 1497448689'
            '.*'    '<a class="reference external" href="http://www\.amazon\.com/dp/1497448689">'
            '.*'    'http://www\.amazon\.com/dp/1497448689</a>'
            '.*'    '</td></tr>'
        )
        self.assertRegex(c, r)

    @util.with_latex_app(
        testroot='contrib-bibtex',
    )
    def test_build_latex(self, app, status, warning):
        '''
        .. traceable:: TST-SPHINXCONTRIB-BIBTEX-LATEX
           :title: Test sphinxcontrib-bibtex can build latex
           :category: SysTest
           :parents: VFY-SPHINXCONTRIB-BIBTEX
           :verification_type: functional
           :verification_method: ci-test
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check BibTeX entry
        # FIXME: avoid \xa0 as whitespace character: 'Jan\xa0Ulrich'
        r = re.compile(
            '(?ms)' '.begin\{' + self.get_latex_thebibliography() + '\}\{HB14\}'
            '.*'    '.bibitem\[HB14\]\{' + re.escape(self.get_latex_idescape('HB14')) + '\}'
            '.*'    'Jan.*Ulrich Hasecke and Georg Brandl'
            '.*'    'Software-\s*Dokumentation mit Sphinx'
            '.*'    'ISBN 1497448689'
            '.*'    '..*\{http://www\.amazon\.com/dp/1497448689\}'
            '.*'    '.end\{' + self.get_latex_thebibliography() + '\}'
        )
        self.assertRegex(c, r)

    @util.with_text_app(
        testroot='contrib-bibtex',
    )
    def test_build_text(self, app, status, warning):
        '''
        .. traceable:: TST-SPHINXCONTRIB-BIBTEX-TEXT
           :title: Test sphinxcontrib-bibtex can build text
           :category: SysTest
           :parents: VFY-SPHINXCONTRIB-BIBTEX
           :verification_type: functional
           :verification_method: ci-test
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = util.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check BibTeX entry
        # FIXME: avoid \xa0 as whitespace character: 'Jan\xa0Ulrich'
        r = re.compile(
            '(?ms)' '\[HB14\]'
            '.*'    'Jan.*Ulrich Hasecke and Georg Brandl'
            '.*'    'Software-\s*Dokumentation mit Sphinx'
            '.*'    'ISBN 1497448689'
            '.*'    'http://www\.amazon\.com/dp/1497448689'
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    util.main()
