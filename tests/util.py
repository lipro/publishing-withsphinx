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
# Unit testing and logging:
# http://plumberjack.blogspot.de/2010/09/unit-testing-and-logging.html
#

'''
Publishing with Sphinx test suite utilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains test suite utilities as part of the
publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

import os
import sys

from sphinx_testing import with_app
from sphinx_testing.path import path
from sphinx_testing.util import sphinx_version

import logging
import logging.handlers

import mock
import nose

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

assert mock  # silence pyflake
assert nose  # silence pyflake

rootdir = path(os.path.dirname(__file__) or '.').abspath()


def with_testroot_app(*args, **kw):
    default_kw = {
        'verbosity': 2,
    }
    if 'testroot' not in kw:
        default_kw['srcdir'] = rootdir / 'roots'
    else:
        default_kw['srcdir'] = rootdir / 'roots' / ('test-' + kw['testroot'])
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


if sys.version_info < (3,):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
    unittest.TestCase.assertRegex = unittest.TestCase.assertRegexpMatches
    unittest.TestCase.assertNotRegex = unittest.TestCase.assertNotRegexpMatches


class TestCasePublishingSphinx(unittest.TestCase):

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
        before calling the test method; other than AssertionError() or
        SkipTest(), any exception raised by this method will be considered
        an error rather than a test failure. The default implementation does
        nothing.
        '''
        self.handler = h = TestHandler(Matcher())
        self.logger = l = logging.getLogger()
        l.addHandler(h)

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
        self.logger.removeHandler(self.handler)
        self.handler.close()

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
    def get_latex_admonition(self):
        if sphinx_version < '1.5':
            return r'notice'
        else:
            return r'sphinxadmonition'

    @classmethod
    def get_latex_bfcode(self):
        if sphinx_version < '1.4.5':
            return r'\bfcode'
        else:
            return r'\sphinxbfcode'

    @classmethod
    def get_latex_code(self):
        if sphinx_version < '1.4.5':
            return r'\code'
        else:
            return r'\sphinxcode'

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
    def get_latex_idescape(self, id):
        if sphinx_version < '1.5.1':
            return id
        else:
            return r'\detokenize{' + id + r'}'

    @classmethod
    def get_latex_protect(self):
        if sphinx_version < '1.3.4':
            return r''
        else:
            return r'\protect'

    @classmethod
    def get_latex_strong(self):
        if sphinx_version < '1.4.5':
            return r'\strong'
        else:
            return r'\sphinxstrong'

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


# Logging already provides a BufferingHandler() [1]_ class which allows you
# to capture LogRecords() generated by logging activity. You can, for example,
# subclass this to store the LogRecord.__dict__ values rather than the
# LogRecords() themselves – this will facilitate checking whether expectations
# are met. You typically don’t want to flush anything until the end of the
# test, though, so a handler which facilitates testing might look like this
# below (without the matches handler). Now let’s consider the checking of
# expectations about what’s been logged. We could implement this in the
# TestHandler() class directly, but it’s the sort of area where different
# people may want to do different things. The bare minimum we need in
# TestHandler() would be something that looks for some kind of match between
# what’s been logged (the buffer of dictionaries) and the expected values. So
# as an idea, let’s delegate the details of matching to a separate Matcher()
# class, which must have a matches() method. Because matching of dictionaries
# is likely to crop up in tests other than to do with logging, creating a
# separate Matcher() class allows us to deploy the functionality in other
# scenarios.
#
# _[1]: https://docs.python.org/3/library/logging.html#logging.handlers.BufferingHandler
#
class TestHandler(logging.handlers.BufferingHandler):

    def __init__(self, matcher):
        # BufferingHandler takes a "capacity" argument
        # so as to know when to flush. As we're overriding
        # shouldFlush anyway, we can set a capacity of zero.
        # You can call flush() manually to clear out the
        # buffer.
        logging.handlers.BufferingHandler.__init__(self, 0)
        self.matcher = matcher

    def shouldFlush(self):
        return False

    def emit(self, record):
        self.format(record)
        self.buffer.append(record.__dict__)

    def matches(self, **kwargs):
        '''
        Look for a saved dict whose keys/values match the supplied arguments.
        '''
        result = False
        for d in self.buffer:
            if self.matcher.matches(d, **kwargs):
                result = True
                break
        return result


class Matcher(object):

    _partial_matches = ('msg', 'message')

    def matches(self, d, **kwargs):
        '''
        Try to match a single dict with the supplied arguments.

        Keys whose values are strings and which are in self._partial_matches
        will be checked for partial (i.e. substring) matches. You can extend
        this scheme to (for example) do regular expression matching, etc.
        '''
        result = True
        for k in kwargs:
            v = kwargs[k]
            dv = d.get(k)
            if not self.match_value(k, dv, v):
                result = False
                break
        return result

    def match_value(self, k, dv, v):
        '''
        Try to match a single stored value (dv) with a supplied value (v).
        '''
        if type(v) != type(dv):
            result = False
        elif type(dv) is not str or k not in self._partial_matches:
            result = (v == dv)
        else:
            result = dv.find(v) >= 0
        return result


def main():
    '''
    Wrap to unittest main function.
    '''
    unittest.main()


if __name__ == "__main__":
    main()
