.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

.. _dvvp:

*******************************************************************************
Design Verification and Validation Plan
*******************************************************************************


Introduction
===============================================================================

Document Purpose
-------------------------------------------------------------------------------

This Design Verification and Validation Plan document provides a detailed
process plan to verifiy and validate the detailed implementations of the
|publishing-withsphinx| extension.

This document's purpose is to provide aclear plan for verification and
validation of this extension and to ensure the extension meets its design
decisions' expectations.

Document Scope
-------------------------------------------------------------------------------

This part of document describes the |publishing-withsphinx| extension. It is
limited to verification-level aspects.

Document Structure
-------------------------------------------------------------------------------

The following chapters describe the nature of tests and the applied methods
and technologies to perform tests.


Execution of Verification and Validation
===============================================================================

.. todo:: Write more details about the execution of verification
   and validation. How we want do that?

   |section_being_continued|

Continuous Integration Test
-------------------------------------------------------------------------------

.. rubric:: What's about the continuous integration tests?

|section_being_continued|

System Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the continuous integration test the following system configuration
requirements should be verified:

.. traceable-list::
   :filter: category == "SysReq" and verification_method == "ci-test" and ( requirement_type == "configuration" or requirement_type == "configuration-python" or requirement_type == "configuration-sphinx" )
   :format: bullets

System Functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the continuous integration test the following system functional
requirements should be verified:

.. traceable-list::
   :filter: category == "SysReq" and verification_method == "ci-test" and requirement_type == "functional"
   :format: bullets

System Usability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the continuous integration test the following system usability
requirements should be verified:

.. traceable-list::
   :filter: category == "SysReq" and verification_method == "ci-test" and requirement_type == "usability"
   :format: bullets

.. System Documentation
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. With the continuous integration test the following system documentation
.. requirements should be verified:

.. .. traceable-list::
   :filter: category == "SysReq" and verification_method == "ci-test" and requirement_type == "documentation"
   :format: bullets

System Implementation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following implementations have to verify by the continuous integration
test:

.. traceable-list::
   :filter: category == "SysImpl" and verification_method == "ci-test"
   :attributes: parents

Continuous Integration Review
-------------------------------------------------------------------------------

.. rubric:: What's about the continuous integration review?

|section_being_continued|

.. System Configuration
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. With the continuous integration review the following system configuration
.. requirements should be verified:

.. .. traceable-list::
   :filter: category == "SysReq" and verification_method == "ci-review" and requirement_type == "configuration"
   :format: bullets

.. System Functionality
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. With the continuous integration review the following system functional
.. requirements should be verified:

.. .. traceable-list::
   :filter: category == "SysReq" and verification_method == "ci-review" and requirement_type == "functional"
   :format: bullets

.. System Usability
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. With the continuous integration review the following system usability
.. requirements should be verified:

.. .. traceable-list::
   :filter: category == "SysReq" and verification_method == "ci-review" and requirement_type == "usability"
   :format: bullets

.. System Documentation
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. With the continuous integration review the following system documentation
.. requirements should be verified:

.. .. traceable-list::
   :filter: category == "SysReq" and verification_method == "ci-review" and requirement_type == "documentation"
   :format: bullets

System Implementation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following implementations have to verify by the continuous integration
review:

.. traceable-list::
   :filter: category == "SysImpl" and verification_method == "ci-review"
   :attributes: parents

Documentation Review
-------------------------------------------------------------------------------

.. rubric:: What's about the documentation review?

|section_being_continued|

.. System Configuration
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. With the documentation review the following system configuration requirements
.. should be verified:

.. .. traceable-list::
   :filter: category == "SysReq" and verification_method == "doc-review" and requirement_type == "configuration"
   :format: bullets

.. System Functionality
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. With the documentation review the following system functional requirements
.. should be verified:

.. .. traceable-list::
   :filter: category == "SysReq" and verification_method == "doc-review" and requirement_type == "functional"
   :format: bullets

.. System Usability
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. With the documentation review the following system usability requirements
.. should be verified:

.. .. traceable-list::
   :filter: category == "SysReq" and verification_method == "doc-review" and requirement_type == "usability"
   :format: bullets

System Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the documentation review the following system documentation requirements
should be verified:

.. traceable-list::
   :filter: category == "SysReq" and verification_method == "doc-review" and requirement_type == "documentation"
   :format: bullets

System Implementation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following implementations have to verify by the documentation review:

.. traceable-list::
   :filter: category == "SysImpl" and verification_method == "doc-review"
   :attributes: parents


Tests
===============================================================================

The |SyDS| defined the following system implementations that have to test:

.. traceable-list::
   :filter: category == "SysImpl" and verification_method == "ci-test"

Module unit test cases
-------------------------------------------------------------------------------

.. todo:: Add more common unit test cases of the
   |publishing-withsphinx| extension.

   |verification_being_continued|

.. .. automodule:: test_module_meta
   :members:
   :undoc-members:

Functional test cases
-------------------------------------------------------------------------------

.. todo:: Add more common functional test cases of the
   |publishing-withsphinx| extension.

   |verification_being_continued|

.. .. automodule:: test_sphinx_basics
   :members:
   :undoc-members:

Functional test cases of original Sphinx extensions
-------------------------------------------------------------------------------

.. todo:: Add more functional test cases of original Sphinx extensions.

   |verification_being_continued|

.. .. automodule:: test_sphinx_ext_autodoc
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_ext_autosummary
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_ext_coverage
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_ext_doctest
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_ext_extlinks
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_ext_ifconfig
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_ext_mathjax
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_ext_todo
   :members:
   :undoc-members:

Functional test cases of contributed Sphinx extensions
-------------------------------------------------------------------------------

.. todo:: Add more functional test cases of contributed Sphinx extensions.

   |verification_being_continued|

.. .. automodule:: test_sphinx_contrib_ansi
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_contrib_argparse
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_contrib_autoprogram
   :members:
   :undoc-members:

.. automodule:: functional.test_sphinx_contrib_bibtex
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_contrib_blockdiag
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_contrib_email
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_contrib_inlinesyntaxhighlight
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_contrib_programoutput
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_contrib_spelling
   :members:
   :undoc-members:

.. .. automodule:: test_sphinx_contrib_tikz
   :members:
   :undoc-members:


Reviews
===============================================================================

The |SyDS| defined the following system implementations that have to review:

.. traceable-list::
   :filter: category == "SysImpl" and ( verification_method == "ci-review" or verification_method == "doc-review" )

Module configuration
-------------------------------------------------------------------------------

.. todo:: Add more review cases of the |publishing-withsphinx| extension.

   |verification_being_continued|

.. traceable:: VFY-TESTS-CI
   :title: Verify CI infrastructure
   :category: SysVerify
   :parents: IMP-TESTS-TRAVIS-CI, IMP-TESTS-TOX
   :verification_type: configuration
   :verification_method: ci-review

The verification of the continuous integration infrastructure is a manual
process to ensure all runtime aspects of this |publishing-withsphinx|
extension will run without any error or failur inside the specified range
of the build matrix. It must be ensured that the :ref:`compatibility` covers
the build matrix as specified by Travis-CI and tox.

The following tox environments have to verify as the build matrix:

.. command-output:: tox --listenvs

.. traceable-graph::
   :tags: VFY-TESTS-CI
   :relationships: parents:2, children
   :caption: Traces to the system requirement VFY-TESTS-CI



Traceability
===============================================================================

The following system verifications (:literal:`VFY-*`) fulfill the related
system implementations (:literal:`IMP-*`):

.. raw:: latex

   \begin{minipage}[t]{0.5\textwidth}\scriptsize

.. traceable-matrix::
   :filter-primaries: category == "SysImpl"
   :filter-secondaries: category == "SysVerify"
   :split-primaries: 25
   :split-secondaries: 10
   :relationship: children
   :format: table

.. raw:: latex

   \end{minipage}

List of system verifications
-------------------------------------------------------------------------------

.. traceable-list::
   :filter: category == "SysVerify"
   :attributes: verification_method
   :format: table
