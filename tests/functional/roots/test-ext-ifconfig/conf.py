# -*- coding: utf-8 -*-

needs_sphinx = '1.3'
needs_extensions = {'sphinx.ext.ifconfig': '1.3'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
latex_engine = 'xelatex'

confval1 = True


def setup(app):
    app.add_config_value('confval1', False, None)
    app.add_config_value('confval2', False, None)
