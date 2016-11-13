.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

.. _compatibility:

====================
Compatibility Matrix
====================

.. index:: Compatibility Matrix
   single: Development; Compatibility Matrix
   pair: Compatibility Matrix; Sphinx toward Python
   pair: Compatibility Matrix; Supported versions

This section contains some information about compatibilities of the extension.

.. contents:: In this section:
   :local:
   :depth: 1
   :backlinks: none


Sphinx toward Python
====================

.. index:: ! Sphinx toward Python

.. raw:: latex

   \begin{minipage}[t]{0.5\textwidth}

.. traceable-matrix::
   :filter-primaries: category == "Sphinx Compatibility"
   :filter-secondaries: category == "Python Compatibility"
   :relationship: children
   :format: table

.. raw:: latex

   \end{minipage}
   \begin{minipage}[t]{0.5\textwidth}

.. traceable-graph::
    :tags: CM-SP12, CM-SP13, CM-SP14
    :caption: Relations of Sphinx toward Python
    :relationships: parents, children

.. raw:: latex

   \end{minipage}


Supported versions
==================

.. index:: ! Supported versions
   pair: Supported versions; Sphinx
   pair: Supported versions; Python


Sphinx
------

.. index:: Sphinx

.. traceable:: CM-SP12
   :title: Sphinx 1.2
   :category: Sphinx Compatibility
   :format: admonition
   :children: CM-PY27, CM-PY33, CM-PY34, CM-PY35

   .. index::
      single: Sphinx; Sphinx 1.x; CM-SP12

   Refer to the prerequisites [#sp12-pr]_ of the Sphinx 1.2 documentation
   builder:

       "Sphinx needs at least Python 2.5 or Python 3.1 to run, ..."

.. .. traceable-graph::
       :tags: CM-SP12
       :caption: Relations of Sphinx 1.2
       :relationships: children

.. traceable:: CM-SP13
   :title: Sphinx 1.3
   :category: Sphinx Compatibility
   :format: admonition
   :children: CM-PY27, CM-PY33, CM-PY34, CM-PY35

   .. index::
      single: Sphinx; Sphinx 1.x; CM-SP13

   Refer to the prerequisites [#sp13-pr]_ of the Sphinx 1.3 documentation
   builder:

       "Sphinx needs at least Python 2.6 or Python 3.3 to run, ..."

.. .. traceable-graph::
       :tags: CM-SP13
       :caption: Relations of Sphinx 1.3
       :relationships: children

.. traceable:: CM-SP14
   :title: Sphinx 1.4
   :category: Sphinx Compatibility
   :format: admonition
   :children: CM-PY27, CM-PY33, CM-PY34, CM-PY35

   .. index::
      single: Sphinx; Sphinx 1.x; CM-SP14

   Refer to the prerequisites [#sp14-pr]_ of the Sphinx 1.4 documentation
   builder:

       "Sphinx needs at least Python 2.6 or Python 3.3 to run, ..."

.. .. traceable-graph::
       :tags: CM-SP14
       :caption: Relations of Sphinx 1.4
       :relationships: children


Python
------

.. index:: Python

.. traceable:: CM-PY27
   :title: Python 2.7
   :category: Python Compatibility
   :format: admonition

   .. index::
      single: Python; Python 2; CM-PY27

   This extension is compatible to the Python 2.7 interpreter.

.. .. traceable-graph::
       :tags: CM-PY27
       :caption: Relations of Python 2.7
       :relationships: parents

.. traceable:: CM-PY33
   :title: Python 3.3
   :category: Python Compatibility
   :format: admonition

   .. index::
      single: Python; Python 3; CM-PY33

   This extension is compatible to the Python 3.3 interpreter.

.. .. traceable-graph::
       :tags: CM-PY33
       :caption: Relations of Python 3.3
       :relationships: parents

.. traceable:: CM-PY34
   :title: Python 3.4
   :category: Python Compatibility
   :format: admonition

   .. index::
      single: Python; Python 3; CM-PY34

   This extension is compatible to the Python 3.4 interpreter.

.. .. traceable-graph::
       :tags: CM-PY34
       :caption: Relations of Python 3.4
       :relationships: parents

.. traceable:: CM-PY35
   :title: Python 3.5
   :category: Python Compatibility
   :format: admonition

   .. index::
      single: Python; Python 3; CM-PY35

   This extension is compatible to the Python 3.5 interpreter.

.. .. traceable-graph::
       :tags: CM-PY35
       :caption: Relations of Python 3.5
       :relationships: parents

.. rubric:: Footnotes

.. [#sp12-pr] :traceable:`CM-SP12` prerequisites:
              http://www.sphinx-doc.org/en/1.2/intro.html#prerequisites

.. [#sp13-pr] :traceable:`CM-SP13` prerequisites:
              http://www.sphinx-doc.org/en/1.3/intro.html#prerequisites

.. [#sp14-pr] :traceable:`CM-SP14` prerequisites:
              http://www.sphinx-doc.org/en/1.4/intro.html#prerequisites
