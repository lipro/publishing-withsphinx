.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

.. _compatibility:

******************************************************************************
Compatibility
******************************************************************************

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
==============================================================================

.. index:: ! Sphinx toward Python


Compatibility Matrix
------------------------------------------------------------------------------

Within the tox configuration file :literal:`tox.ini` the folloging
compatibility matrix is defined:

.. only:: html

   .. raw:: latex

      \begin{minipage}[t]{0.75\textwidth}

   .. traceable-matrix::
      :filter-primaries: category == "compatibility-sphinx"
      :filter-secondaries: category == "compatibility-python"
      :relationship: children
      :format: table

   .. raw:: latex

      \end{minipage}

.. only:: latex

   .. error:: Mal formatted LaTeX sequence in :code:`traceable-matrix`

      See issue #24 for details an ongoing fixes.

Compatibility Traces
------------------------------------------------------------------------------

The compatibility matrix has the following traces into the tox test
environments:

.. raw:: latex

   \begin{minipage}[t]{0.65\textwidth}

.. traceable-graph::
    :tags: sphinx1.3, sphinx1.4, sphinx1.5, sphinx1.6, sphinx1.7, sphinx1.8
    :caption: Traces of the tox test environments
    :relationships: children

.. raw:: latex

   \end{minipage}


Tox test environments
==============================================================================

.. index:: ! Tox test environments
   pair: Tox test environments; Sphinx
   pair: Tox test environments; Python


The compatibility matrix is an result of the following tox test environments:

.. traceable:: py27-sphinx1.8
   :title: Python 2.7 with Sphinx 1.8
   :category: compatibility-matrix
   :parents: py27

   .. command-output:: tox --showconfig -e py27-sphinx1.8

.. raw:: latex

   \newpage

.. traceable:: py27-sphinx1.7
   :title: Python 2.7 with Sphinx 1.7
   :category: compatibility-matrix
   :parents: py27

   .. command-output:: tox --showconfig -e py27-sphinx1.7

.. raw:: latex

   \newpage

.. traceable:: py27-sphinx1.6
   :title: Python 2.7 with Sphinx 1.6
   :category: compatibility-matrix
   :parents: py27

   .. command-output:: tox --showconfig -e py27-sphinx1.6

.. raw:: latex

   \newpage

.. traceable:: py27-sphinx1.5
   :title: Python 2.7 with Sphinx 1.5
   :category: compatibility-matrix
   :parents: py27

   .. command-output:: tox --showconfig -e py27-sphinx1.5

.. raw:: latex

   \newpage

.. traceable:: py27-sphinx1.4
   :title: Python 2.7 with Sphinx 1.4
   :category: compatibility-matrix
   :parents: py27

   .. command-output:: tox --showconfig -e py27-sphinx1.4

.. raw:: latex

   \newpage

.. traceable:: py27-sphinx1.3
   :title: Python 2.7 with Sphinx 1.3
   :category: compatibility-matrix
   :parents: py27

   .. command-output:: tox --showconfig -e py27-sphinx1.3

.. ----------------------------------------------------------------------------

.. raw:: latex

   \newpage

.. traceable:: py37-sphinx1.8
   :title: Python 3.7 with Sphinx 1.8
   :category: compatibility-matrix
   :parents: py37

   .. command-output:: tox --showconfig -e py37-sphinx1.8

.. raw:: latex

   \newpage

.. traceable:: py37-sphinx1.7
   :title: Python 3.7 with Sphinx 1.7
   :category: compatibility-matrix
   :parents: py37

   .. command-output:: tox --showconfig -e py37-sphinx1.7

.. raw:: latex

   \newpage

.. traceable:: py37-sphinx1.6
   :title: Python 3.7 with Sphinx 1.6
   :category: compatibility-matrix
   :parents: py37

   .. command-output:: tox --showconfig -e py37-sphinx1.6

.. raw:: latex

   \newpage

.. traceable:: py37-sphinx1.5
   :title: Python 3.7 with Sphinx 1.5
   :category: compatibility-matrix
   :parents: py37

   .. command-output:: tox --showconfig -e py37-sphinx1.5

.. raw:: latex

   \newpage

.. traceable:: py37-sphinx1.4
   :title: Python 3.7 with Sphinx 1.4
   :category: compatibility-matrix
   :parents: py37

   .. command-output:: tox --showconfig -e py37-sphinx1.4

.. raw:: latex

   \newpage

.. traceable:: py37-sphinx1.3
   :title: Python 3.7 with Sphinx 1.3
   :category: compatibility-matrix
   :parents: py37

   .. command-output:: tox --showconfig -e py37-sphinx1.3

.. ----------------------------------------------------------------------------

.. raw:: latex

   \newpage

.. traceable:: py36-sphinx1.8
   :title: Python 3.6 with Sphinx 1.8
   :category: compatibility-matrix
   :parents: py36

   .. command-output:: tox --showconfig -e py36-sphinx1.8

.. raw:: latex

   \newpage

.. traceable:: py36-sphinx1.7
   :title: Python 3.6 with Sphinx 1.7
   :category: compatibility-matrix
   :parents: py36

   .. command-output:: tox --showconfig -e py36-sphinx1.7

.. raw:: latex

   \newpage

.. traceable:: py36-sphinx1.6
   :title: Python 3.6 with Sphinx 1.6
   :category: compatibility-matrix
   :parents: py36

   .. command-output:: tox --showconfig -e py36-sphinx1.6

.. raw:: latex

   \newpage

.. traceable:: py36-sphinx1.5
   :title: Python 3.6 with Sphinx 1.5
   :category: compatibility-matrix
   :parents: py36

   .. command-output:: tox --showconfig -e py36-sphinx1.5

.. raw:: latex

   \newpage

.. traceable:: py36-sphinx1.4
   :title: Python 3.6 with Sphinx 1.4
   :category: compatibility-matrix
   :parents: py36

   .. command-output:: tox --showconfig -e py36-sphinx1.4

.. raw:: latex

   \newpage

.. traceable:: py36-sphinx1.3
   :title: Python 3.6 with Sphinx 1.3
   :category: compatibility-matrix
   :parents: py36

   .. command-output:: tox --showconfig -e py36-sphinx1.3

.. ----------------------------------------------------------------------------

.. raw:: latex

   \newpage

.. traceable:: py35-sphinx1.8
   :title: Python 3.5 with Sphinx 1.8
   :category: compatibility-matrix
   :parents: py35

   .. command-output:: tox --showconfig -e py35-sphinx1.8

.. raw:: latex

   \newpage

.. traceable:: py35-sphinx1.7
   :title: Python 3.5 with Sphinx 1.7
   :category: compatibility-matrix
   :parents: py35

   .. command-output:: tox --showconfig -e py35-sphinx1.7

.. raw:: latex

   \newpage

.. traceable:: py35-sphinx1.6
   :title: Python 3.5 with Sphinx 1.6
   :category: compatibility-matrix
   :parents: py35

   .. command-output:: tox --showconfig -e py35-sphinx1.6

.. raw:: latex

   \newpage

.. traceable:: py35-sphinx1.5
   :title: Python 3.5 with Sphinx 1.5
   :category: compatibility-matrix
   :parents: py35

   .. command-output:: tox --showconfig -e py35-sphinx1.5

.. raw:: latex

   \newpage

.. traceable:: py35-sphinx1.4
   :title: Python 3.5 with Sphinx 1.4
   :category: compatibility-matrix
   :parents: py35

   .. command-output:: tox --showconfig -e py35-sphinx1.4

.. raw:: latex

   \newpage

.. traceable:: py35-sphinx1.3
   :title: Python 3.5 with Sphinx 1.3
   :category: compatibility-matrix
   :parents: py35

   .. command-output:: tox --showconfig -e py35-sphinx1.3

.. ----------------------------------------------------------------------------

.. raw:: latex

   \newpage

.. traceable:: py34-sphinx1.8
   :title: Python 3.4 with Sphinx 1.8
   :category: compatibility-matrix
   :parents: py34

   .. command-output:: tox --showconfig -e py34-sphinx1.8

.. raw:: latex

   \newpage

.. traceable:: py34-sphinx1.7
   :title: Python 3.4 with Sphinx 1.7
   :category: compatibility-matrix
   :parents: py34

   .. command-output:: tox --showconfig -e py34-sphinx1.7

.. raw:: latex

   \newpage

.. traceable:: py34-sphinx1.6
   :title: Python 3.4 with Sphinx 1.6
   :category: compatibility-matrix
   :parents: py34

   .. command-output:: tox --showconfig -e py34-sphinx1.6

.. raw:: latex

   \newpage

.. traceable:: py34-sphinx1.5
   :title: Python 3.4 with Sphinx 1.5
   :category: compatibility-matrix
   :parents: py34

   .. command-output:: tox --showconfig -e py34-sphinx1.5

.. raw:: latex

   \newpage

.. traceable:: py34-sphinx1.4
   :title: Python 3.4 with Sphinx 1.4
   :category: compatibility-matrix
   :parents: py34

   .. command-output:: tox --showconfig -e py34-sphinx1.4

.. raw:: latex

   \newpage

.. traceable:: py34-sphinx1.3
   :title: Python 3.4 with Sphinx 1.3
   :category: compatibility-matrix
   :parents: py34

   .. command-output:: tox --showconfig -e py34-sphinx1.3

.. ----------------------------------------------------------------------------
.. --- hidden traceable items for Sphinx compatibility
.. ----------------------------------------------------------------------------

.. traceable:: sphinx1.8
   :title: Sphinx 1.8
   :category: compatibility-sphinx
   :sibling: REQ-WORKSON-SP18
   :format: hidden

.. traceable:: sphinx1.7
   :title: Sphinx 1.7
   :category: compatibility-sphinx
   :sibling: REQ-WORKSON-SP17
   :format: hidden

.. traceable:: sphinx1.6
   :title: Sphinx 1.6
   :category: compatibility-sphinx
   :sibling: REQ-WORKSON-SP16
   :format: hidden

.. traceable:: sphinx1.5
   :title: Sphinx 1.5
   :category: compatibility-sphinx
   :sibling: REQ-WORKSON-SP15
   :format: hidden

.. traceable:: sphinx1.4
   :title: Sphinx 1.4
   :category: compatibility-sphinx
   :sibling: REQ-WORKSON-SP14
   :format: hidden

.. traceable:: sphinx1.3
   :title: Sphinx 1.3
   :category: compatibility-sphinx
   :sibling: REQ-WORKSON-SP13
   :format: hidden

.. ----------------------------------------------------------------------------
.. --- hidden traceable items for Python compatibility
.. ----------------------------------------------------------------------------

.. traceable:: py27
   :title: Python 2.7
   :category: compatibility-python
   :sibling: REQ-WORKSON-PY27
   :parents: sphinx1.3, sphinx1.4, sphinx1.5, sphinx1.6, sphinx1.7, sphinx1.8
   :format: hidden

.. traceable:: py37
   :title: Python 3.7
   :category: compatibility-python
   :sibling: REQ-WORKSON-PY37
   :parents: sphinx1.3, sphinx1.4, sphinx1.5, sphinx1.6, sphinx1.7, sphinx1.8
   :format: hidden

.. traceable:: py36
   :title: Python 3.6
   :category: compatibility-python
   :sibling: REQ-WORKSON-PY36
   :parents: sphinx1.3, sphinx1.4, sphinx1.5, sphinx1.6, sphinx1.7, sphinx1.8
   :format: hidden

.. traceable:: py35
   :title: Python 3.5
   :category: compatibility-python
   :sibling: REQ-WORKSON-PY35
   :parents: sphinx1.3, sphinx1.4, sphinx1.5, sphinx1.6, sphinx1.7, sphinx1.8
   :format: hidden

.. traceable:: py34
   :title: Python 3.4
   :category: compatibility-python
   :sibling: REQ-WORKSON-PY34
   :parents: sphinx1.3, sphinx1.4, sphinx1.5, sphinx1.6, sphinx1.7, sphinx1.8
   :format: hidden

