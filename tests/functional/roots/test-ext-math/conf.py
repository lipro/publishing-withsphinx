# -*- coding: utf-8 -*-

needs_sphinx = '1.3'
needs_extensions = {'sphinx.ext.mathjax': '1.3'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
latex_engine = 'xelatex'
