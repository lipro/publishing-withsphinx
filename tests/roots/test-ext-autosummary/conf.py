# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('samples'))
sys.path.insert(0, os.path.abspath('samples/an_example_pypi_project'))

needs_sphinx = '1.2'
needs_extensions = {'sphinx.ext.autosummary': '1.2'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
