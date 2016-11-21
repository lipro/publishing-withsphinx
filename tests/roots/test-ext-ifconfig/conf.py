# -*- coding: utf-8 -*-

needs_sphinx = '1.2'
needs_extensions = {'sphinx.ext.ifconfig': '1.2'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]

confval1 = True


def setup(app):
    app.add_config_value('confval1', False, None)
    app.add_config_value('confval2', False, None)
