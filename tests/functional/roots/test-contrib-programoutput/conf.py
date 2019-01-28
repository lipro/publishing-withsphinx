# -*- coding: utf-8 -*-

import os

os.environ["TEST_FIXTURES_ROOTS"] = os.path.abspath('..')

needs_sphinx = '1.2'
# FIXME: needs_extensions = {'sphinxcontrib.programoutput': '0.10'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
latex_engine = 'xelatex'
