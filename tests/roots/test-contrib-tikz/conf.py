# -*- coding: utf-8 -*-

from sphinx.errors import SphinxError

needs_sphinx = '1.2'
# FIXME: needs_extensions = {'sphinxcontrib.tikz': '0.4'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
latex_engine = 'xelatex'


def default_latex_engine(config):
    # type: (Config) -> unicode
    """ Better default latex_engine settings for specific languages. """
    if config.language == 'ja':
        return 'platex'
    else:
        return 'pdflatex'


def check_latex_engine(app):
    app.builder.warn('latex_engine backported for compatibility with Sphinx < 1.5')
    if 'latex_engine' not in app.config.values:
        raise SphinxError('latex_engine not found')
    else:
        if app.config.latex_engine not in ('pdflatex', 'xelatex', 'lualatex', 'platex'):
            raise SphinxError('invalid latex_engine: %s' % app.config.latex_engine)


def setup(app):
    if 'latex_engine' not in app.config.values:
        app.add_config_value('latex_engine', default_latex_engine, None)
        app.connect('builder-inited', check_latex_engine)
