# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('../../samples'))

needs_sphinx = '1.2'
# FIXME: needs_extensions = {'sphinxarg.ext': '0.1'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
