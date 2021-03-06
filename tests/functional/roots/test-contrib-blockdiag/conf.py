# -*- coding: utf-8 -*-

import os

needs_sphinx = '1.3'
needs_extensions = {'sphinxcontrib.blockdiag': '1.5'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
latex_engine = 'xelatex'

# FIXME: avoid local copy of DejaVuSans core font
blockdiag_fontpath = os.path.abspath('../_static/DejaVuSans.ttf')
