# -*- coding: utf-8 -*-

needs_sphinx = '1.2'
needs_extensions = {'sphinx.ext.doctest': '1.2'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
latex_engine = 'xelatex'