# -*- coding: utf-8 -*-

needs_sphinx = '1.2'
# FIXME: needs_extensions = {'sphinxcontrib.spelling': '2.3'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
latex_engine = 'xelatex'
