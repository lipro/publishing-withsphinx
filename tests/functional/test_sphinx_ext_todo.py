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
test_sphinx_ext_todo
~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinx.ext.todo extension
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests.functional import fixtures

import re


class TestCaseSphinxExtTodo(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_html_app(
        testroot='ext-todo',
        confoverrides={
            'todo_include_todos': True,
        },
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.todo: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check todolist
        r = re.compile(
            '(?ms)'
            + re.escape(r'<div class="admonition-todo admonition">') + '.*'
            + re.escape(r'<p class="first admonition-title">Todo</p>') + '.*'
            + re.escape(r'<p class="last">todo in bar</p>') + '.*'
            + re.escape(r'</div>') + '.*'
            + re.escape(r'<p class="todo-source">') + '.*' + re.escape(r'</p>') + '.*'
            + re.escape(r'<div class="admonition-todo admonition">') + '.*'
            + re.escape(r'<p class="first admonition-title">Todo</p>') + '.*'
            + re.escape(r'<p class="last">todo in foo</p>') + '.*'
            + re.escape(r'</div>') + '.*'
            + re.escape(r'<p class="todo-source">') + '.*' + re.escape(r'</p>')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
        testroot='ext-todo',
        confoverrides={
            'todo_include_todos': True,
        },
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.todo: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check todolist
        r = re.compile(
            '(?ms)'
            + re.escape(r'\begin{' + self.get_latex_admonition() + r'}{note}{Todo}') + '.*'
            + re.escape(r'todo in bar') + '.*' + re.escape(r'\end{' + self.get_latex_admonition() + r'}') + '.*'
            + re.escape(r'\begin{' + self.get_latex_admonition() + r'}{note}{Todo}') + '.*'
            + re.escape(r'todo in foo') + '.*' + re.escape(r'\end{' + self.get_latex_admonition() + r'}')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
        testroot='ext-todo',
        confoverrides={
            'todo_include_todos': True,
        },
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.todo: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check todolist
        r = re.compile(
            '(?ms)' + re.escape(r'Todo: todo in bar') + '.*' + re.escape(r'Todo: todo in foo')
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
