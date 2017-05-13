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

'''
publishing.withsphinx.backports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module provides all backports from newer |Sphinx| versions
as needed by other extensions when they will be used with older
versions of the |Sphinx_dsc|.

The backports are:

* New in |Sphinx| 1.5:

  * |app.config.latex_engine|_

.. |app.config.latex_engine| replace:: :literal:`app.config.latex_engine`
.. _app.config.latex_engine: http://www.sphinx-doc.org/en/stable/config.html#confval-latex_engine
'''

from __future__ import absolute_import
from sphinx.errors import SphinxError


def default_latex_engine(config):
    # type: (Config) -> unicode
    '''
    Better default |app.config.latex_engine| settings for specific languages.

    :param config: |Sphinx| configuration instance, representing the
                   Sphinx configuration base.
    :type config: class sphinx.config.Config

    :returns: *latex_engine* executable file name dependent on specific
              languages. Currently distinctions are:

              #. *JA*: ``platex`` for Japanese
              #. *default*: ``pdflatex`` for al other languages
    :rtype: ``str``
    '''

    if config.language == 'ja':
        return 'platex'
    else:
        return 'pdflatex'


def check_latex_engine(app):
    '''
    Check the presence of |app.config.latex_engine| and evaluate the
    content of validity.

    :param app: |Sphinx| application instance, representing the Sphinx process.
    :type app: class sphinx.application.Sphinx

    :returns: Nothing.
    :rtype: NoneType
    '''

    app.builder.warn('latex_engine backported for compatibility with Sphinx < 1.5')
    if 'latex_engine' not in app.config.values:
        raise SphinxError('latex_engine not found')
    else:
        if app.config.latex_engine not in ('pdflatex', 'xelatex', 'lualatex', 'platex'):
            raise SphinxError('invalid latex_engine: %s' % app.config.latex_engine)


def sphinx15(app):
    '''
    Load all backports from |Sphinx| 1.5 as needed by the
    :data:`publishing.withsphinx` extension. Currently that are:

    * |app.config.latex_engine|_

    :param app: |Sphinx| application instance, representing the Sphinx process.
    :type app: class sphinx.application.Sphinx

    :returns: Nothing.
    :rtype: NoneType
    '''

    if 'latex_engine' not in app.config.values:
        app.add_config_value('latex_engine', default_latex_engine, None)
        app.connect('builder-inited', check_latex_engine)
