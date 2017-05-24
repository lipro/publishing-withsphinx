.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

wrapping test for sphinx.ext.autosummary
========================================

This wraps the real test fixture because of a well known bug with missing
toctree caption. It is already fixed on latest Sphinx 1.4 releases but
was never backported to Sphinx 1.3:

- `issue #2465 <https://github.com/sphinx-doc/sphinx/issues/2465>`_
- `fix sha1:88322af <https://github.com/sphinx-doc/sphinx/commit/88322af>`_

Sphinx 1.2 is not affected because of missing support of toctree captions.

.. toctree::
   :maxdepth: 1

   autosummary
