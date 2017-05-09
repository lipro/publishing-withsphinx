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
test_sphinx_contrib_spelling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinxcontrib.spelling
extension as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

import re
from tests import util


class TestCaseSphinxContribSpelling(util.TestCasePublishingSphinx):

    @util.with_spelling_app(
        testroot='contrib-spelling',
        confoverrides={
            'spelling_lang': 'en_US',
            'spelling_word_list_filename': 'spelling_wordlist.txt',
            'spelling_show_suggestions': True,
        },
    )
    def test_build_spelling(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinxcontrib.spelling: can test and summarize text spelling
        '''
        app.builder.build_all()
        print(status.getvalue())
        print(warning.getvalue())

        # check file for spelling results
        p = util.path(app.outdir / 'output.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # validate expected misspelled words
        #   re.escape(r'\(mispelled\)' '.*' '"misspelled"') +
        #   '.*' +
        #   re.escape(r'\(txt\)' '.*' '"text"') +
        #   '.*' +
        r = re.compile(
            '(?ms)' +
            re.escape(r'(mispelled)') + '.*' + re.escape(r'"misspelled"') + '.*' +
            re.escape(r'(txt)') + '.*' + re.escape(r'"text"') + '.*' +
            re.escape(r'(Speeling)') + '.*' + re.escape(r'"Spelling"')
        )
        self.assertRegex(c, r)

        # validate misspelled words expected to ignore
        r = re.compile(
            '(?ms)' +
            re.escape(r'(ignoreed)') + '.*' + re.escape(r'(litterals)')
        )
        self.assertNotRegex(c, r)

        # validate unknown words expected to set valid by word list
        r = re.compile(re.escape('(sphinxcontrib)'))
        self.assertNotRegex(c, r)
        r = re.compile(re.escape('(Inline)'))
        self.assertNotRegex(c, r)


if __name__ == "__main__":
    util.main()
