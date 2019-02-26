# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Stephan Linz
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
# Unit testing and logging:
# http://plumberjack.blogspot.de/2010/09/unit-testing-and-logging.html
#

'''
Publishing with Sphinx test fixture utilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains test fixture utilities as part of the
publishing.withsphinx package.

:copyright: Copyright 2014-2017 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests import util

import os

from sphinx_testing import with_app
from sphinx_testing.path import path
from sphinx_testing.util import sphinx_version

rootdir = path(os.path.dirname(__file__) or '.').abspath()


def with_testroot_app(*args, **kw):
    default_kw = {
        'verbosity': 2,
    }
    if 'testroot' not in kw:
        default_kw['srcdir'] = os.path.normpath(os.path.join(rootdir, 'roots'))
    else:
        default_kw['srcdir'] = os.path.normpath(os.path.join(rootdir, 'roots', ('test-' + kw['testroot'])))
        del kw['testroot']
    default_kw.update(kw)
    return with_app(*args, **default_kw)


def with_coverage_app(*args, **kw):
    default_kw = {
        'buildername': 'coverage',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_doctest_app(*args, **kw):
    default_kw = {
        'buildername': 'doctest',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_devhelp_app(*args, **kw):
    default_kw = {
        'buildername': 'devhelp',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_epub_app(*args, **kw):
    default_kw = {
        'buildername': 'epub',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_html_app(*args, **kw):
    default_kw = {
        'buildername': 'singlehtml',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_htmlhelp_app(*args, **kw):
    default_kw = {
        'buildername': 'htmlhelp',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_json_app(*args, **kw):
    default_kw = {
        'buildername': 'json',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_latex_app(*args, **kw):
    default_kw = {
        'buildername': 'latex',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_manpage_app(*args, **kw):
    default_kw = {
        'buildername': 'man',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_pseudoxml_app(*args, **kw):
    default_kw = {
        'buildername': 'pseudoxml',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_qthelp_app(*args, **kw):
    default_kw = {
        'buildername': 'qthelp',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_spelling_app(*args, **kw):
    default_kw = {
        'buildername': 'spelling',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_texinfo_app(*args, **kw):
    default_kw = {
        'buildername': 'texinfo',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_text_app(*args, **kw):
    default_kw = {
        'buildername': 'text',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


def with_xml_app(*args, **kw):
    default_kw = {
        'buildername': 'xml',
    }
    default_kw.update(kw)
    return with_testroot_app(*args, **default_kw)


class TestCaseFunctionalPublishingSphinx(util.TestCasePublishingSphinx):

    @classmethod
    def is_sphinx_coverage_not_affected(self):
        if sphinx_version < '1.4':
            return False
        else:
            return True

    @classmethod
    def can_found_this_qthelp_file(self, file):
        if not sphinx_version < '1.5' and file == 'search.html':
            return False
        else:
            return True

    @classmethod
    def get_html_code(self, args='', close=False):
        if sphinx_version < '1.3':
            code = r'tt'
        else:
            code = r'code'
        if close:
            return r'</' + code + '>'
        else:
            return r'<' + code + args + '>'

    @classmethod
    def get_html_class_math(self):
        if sphinx_version < '1.7':
            return r'math'
        else:
            return r'math notranslate nohighlight'

    @classmethod
    def get_latex_admonition(self):
        if sphinx_version < '1.5':
            return r'notice'
        else:
            return r'sphinxadmonition'

    @classmethod
    def get_latex_bfcode(self):
        if sphinx_version < '1.4.5':
            return r'\bfcode'
        elif sphinx_version < '1.7':
            return r'\sphinxbfcode'
        else:
            return r'\sphinxbfcode{\sphinxupquote'

    @classmethod
    def get_latex_code(self):
        if sphinx_version < '1.4.5':
            return r'\code'
        elif sphinx_version < '1.7':
            return r'\sphinxcode'
        else:
            return r'\sphinxcode{\sphinxupquote'

    @classmethod
    def get_latex_code_strong(self):
        if sphinx_version < '1.4.5':
            return r'\strong'
        elif sphinx_version < '1.6':
            return r'\sphinxstrong'
        elif sphinx_version < '1.7':
            return r'\sphinxbfcode'
        else:
            return r'\sphinxbfcode{\sphinxupquote'

    @classmethod
    def get_latex_href(self):
        if sphinx_version < '1.5.4':
            return r'\href'
        else:
            return r'\sphinxhref'

    @classmethod
    def get_latex_includegraphics(self):
        if sphinx_version < '1.4.5':
            return r'\includegraphics'
        else:
            return r'\sphinxincludegraphics'

    @classmethod
    def get_latex_idescape(self, id, abbr):
        if sphinx_version < '1.5.1':
            return abbr
        elif sphinx_version < '1.8':
            return r'\detokenize{' + abbr + r'}'
        else:
            return r'index:' + id

    @classmethod
    def get_latex_protect(self):
        if sphinx_version < '1.3.4':
            return r''
        else:
            return r'\protect'

    @classmethod
    def get_latex_titleref(self):
        if sphinx_version < '1.4':
            return r'\emph'
        elif sphinx_version < '1.4.5':
            return r'\titleref'
        else:
            return r'\sphinxtitleref'

    @classmethod
    def get_latex_thebibliography(self):
        if sphinx_version < '1.5':
            return r'thebibliography'
        else:
            return r'sphinxthebibliography'

    @classmethod
    def get_latex_url(self):
        if sphinx_version < '1.4.5':
            return r'\href'
        elif sphinx_version < '1.5.4':
            return r'\url'
        else:
            return r'\sphinxurl'

    @classmethod
    def get_latex_verbatim(self, alltt=False):
        if alltt and sphinx_version < '1.3':
            return r'alltt'
        elif sphinx_version < '1.5':
            return r'Verbatim'
        else:
            return r'sphinxVerbatim'

    @classmethod
    def get_latex_autosummary_subsubnode(self):
        if sphinx_version < '1.8':
            return r'\paragraph'
        else:
            return r'\subsubsection*'

    @classmethod
    def get_latex_todo_node_text(self):
        if sphinx_version < '1.6':
            return r'Todo'
        else:
            return r'Todo:'

    @classmethod
    def get_hellipsis_text(self):
        if sphinx_version < '1.6':
            return r'...'
        else:
            return u'\u2026'


if __name__ == "__main__":
    util.main()
