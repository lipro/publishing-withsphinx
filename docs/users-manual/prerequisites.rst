.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

.. _prerequisites:

******************************************************************************
Prerequisites and Configuration
******************************************************************************

.. index::
   pair: Prerequisites; Configuration
   pair: Prerequisites; Install

This section contains some information about extension installation and
how to configure Sphinx to use it.

.. contents:: In this section:
   :local:
   :depth: 1
   :backlinks: none


Prerequisites
==============================================================================

.. index:: ! Prerequisites

This extension relies on some software packages being installed on your
computer:

A. Python 2.7 or 3.6

B. Sphinx 1.3 or greater

C. LaTeX with the :literal:`tikz` package and native PDF support
   (ex. :literal:`xelatex`).


Install
==============================================================================

.. index:: ! Install

To install the package with :program:`pip`:

.. code-block:: bash

   pip install publishing-withsphinx

To install the package from source archive:

.. code-block:: bash

   cd publishing-withsphinx
   python setup.py install


Configure Sphinx
==============================================================================

.. index:: ! Configuration

To enable this extension, add :code:`publishing.withsphinx` module to
extensions option at :file:`conf.py`.

.. code-block:: python

   # Enabled extensions
   extensions = ['publishing.withsphinx']
