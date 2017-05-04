# -*- coding: utf-8 -*-
#
# publishing-withsphinx documentation build configuration file
#
# the monkey patch to suppress the image nonlocal uri warning comes from:
# http://stackoverflow.com/questions/12772927/
#

import os
import sys

import sphinx.environment
from docutils.utils import get_source_line

from pkg_resources import get_distribution  # to get the raw metadata content
from email import message_from_string       # to parse it using email.Parser
from webob.multidict import MultiDict       # to convert it to a MultiDict


def _warn_node(self, msg, node, **kwargs):
    if not msg.startswith('nonlocal image URI found:'):
        self._warnfunc(msg, '%s:%s' % get_source_line(node), **kwargs)

sphinx.environment.BuildEnvironment.warn_node = _warn_node

try:
    pkg_metadata = get_distribution('publishing-withsphinx').get_metadata('METADATA')
except:
    pkg_metadata = get_distribution('publishing-withsphinx').get_metadata('PKG-INFO')

pkg_messages = message_from_string(pkg_metadata)
prj_metadata = MultiDict(pkg_messages)

sys.path.insert(0, os.path.abspath('..'))        # fount local util modules
sys.path.insert(0, os.path.abspath('../tests'))  # found local test modules

# -- General configuration ------------------------------------------------

needs_sphinx = '1.2'
extensions = [
    'publishing.withsphinx',
    'sphinxcontrib.traceables',
    'sphinxcontrib.traceability',
    'sphinx.ext.graphviz',
]
needs_extensions = {'publishing.withsphinx': '0.0'}

# -- Specific configuration -----------------------------------------------

# General information about the project.
project = prj_metadata.get('Name')
version = prj_metadata.get('Version')
release = version
license = prj_metadata.get('License')
summary = prj_metadata.get('Summary')
author = prj_metadata.get('Author')
author_email = prj_metadata.get('Author-email')
url = prj_metadata.get('Home-page')
download_url = prj_metadata.get('Download-URL')
# copyright = '2016, ' + author + ' <' + author_email + '>'
copyright = '2016, ' + author

# General content behaviors.
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
language = 'en'
templates_path = ['_templates']
exclude_patterns = [
    '_build',
    '_templates',
    'global.rst',
    'Thumbs.db',
    '.DS_Store',
]
pygments_style = 'sphinx'
rst_prolog = '''
.. include:: <isoamsa.txt>
'''
rst_epilog = ('''
.. |summary| replace:: %s
.. include:: /%s/global.rsti
''') % (summary, os.path.abspath('.'))

# General extension behaviors.
todo_include_todos = True
todo_link_only = True
autodoc_default_flags = [
    'members',
    'no-undoc-members',
]
tikz_transparent = True
tikz_proc_suite = 'pdf2svg'
tikz_tikzlibraries = 'arrows,matrix,calendar,folding'

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
}
html_title = 'Publishing with Sphinx'
html_use_index = True
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
html_search_language = language

# -- Options for HTML help output -----------------------------------------

htmlhelp_basename = 'publishing-withsphinxdoc'

# -- Options for LaTeX output ---------------------------------------------

f = open('_templates/preamble.tex', 'r+')
latex_custom = f.read()

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'figure_align': 'H',
    'preamble': latex_custom,
}

latex_documents = [
    (master_doc, 'publishing-withsphinx.tex', 'Publishing with Sphinx',
     author, 'manual', False),
]

latex_engine = 'xelatex'

# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'publishing-withsphinx', 'Publishing with Sphinx',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, 'publishing-withsphinx', 'Publishing with Sphinx',
     author, 'publishing-withsphinx', summary,
     'Miscellaneous'),
]
