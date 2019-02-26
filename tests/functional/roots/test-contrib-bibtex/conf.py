# -*- coding: utf-8 -*-

needs_sphinx = '1.3'
# FIXME: needs_extensions = {'sphinxcontrib.bibtex': '0.3'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
latex_engine = 'xelatex'
