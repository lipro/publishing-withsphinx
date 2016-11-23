.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

test for sphinx.ext.doctest
===========================

.. testsetup::

   import publishing.withsphinx

The Sphinx extension to help document publishing.

Doctest example:

.. doctest::

   >>> print(publishing.withsphinx.__name__)
   publishing.withsphinx

Test-Output example:

.. testcode::

   print(publishing.withsphinx.__name__)

This would output:

.. testoutput::

   publishing.withsphinx
