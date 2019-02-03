.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

.. _syds:

*******************************************************************************
System Design Specification
*******************************************************************************


Introduction
===============================================================================

Document Purpose
-------------------------------------------------------------------------------

This System Design Specification document identifies the design decisions
for the implementation of the |publishing-withsphinx| extension and describes
their detailed implementations.

This document's purpose is to ensure the implementation of the extention meets
its system requirements.

Document Scope
-------------------------------------------------------------------------------

This part of document describes the |publishing-withsphinx| extension design.
It is limited to system-level aspects.

Document Structure
-------------------------------------------------------------------------------

The following chapters describe the system design decisions and their
implementations.


System Design Decisions
===============================================================================

The |SyRS| defined the following system requirements:

.. traceable-list::
   :filter: category == "SysReq"


Configuration Implementations
-------------------------------------------------------------------------------

.. traceable:: IMP-TESTS-TRAVIS-CI
   :title: Use Travis-CI for tests
   :category: SysImpl
   :parents: REQ-TESTS-CI,
             REQ-WORKSON-PY27,
             REQ-WORKSON-PY37, REQ-WORKSON-PY36, REQ-WORKSON-PY35, REQ-WORKSON-PY34
   :implementation_type: configuration
   :verification_method: ci-review

This |publishing-withsphinx| extension uses the |Travis-CI_dsc| to process
test jobs on demand.

- This |publishing-withsphinx| extension provides the Travis-CI configuration
  file :literal:`.travis.yml` ready to use for development, so that a
  :traceable:`STKH-DEVS` needs no further configuration or administration
  (see: :traceable:`STRQ-CONTINTEGR`).
- The Travis-CI configuration file provides the CI job description and all
  addons needed to process the jobs. 
- The CI job description introduce different Python runtime envionments for
  each required Python version.
- All CI jobs will be triggerd by the online Git repository service on each
  new push for the latest change (HEAD of the branch that where pushed).

.. traceable-graph::
   :tags: IMP-TESTS-TRAVIS-CI
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement IMP-TESTS-TRAVIS-CI

.. ----------------------------------------------------------------------------

.. traceable:: IMP-TESTS-TOX
   :title: Use tox for automate and standardize testing
   :category: SysImpl
   :parents: REQ-TESTS-CI,
             REQ-WORKSON-SP16, REQ-WORKSON-SP15,
             REQ-WORKSON-SP14, REQ-WORKSON-SP13
   :sibling: IMP-TESTS-TRAVIS-CI
   :implementation_type: configuration
   :verification_method: ci-review

This |publishing-withsphinx| extension uses |tox_dsc| to process test jobs
under different conditions and configurations.

- The |tox| package name is part of the list of Python packages required to
  install before this |publishing-withsphinx| extension can be used for
  development (see: :traceable:`STRQ-PIPINSTALL`).
- This |publishing-withsphinx| extension provides the tox configuration file
  :literal:`tox.ini` ready to use for development, so that a
  :traceable:`STKH-DEVS` needs no further configuration or administration
  (see: :traceable:`STRQ-CONTINTEGR`).
- The tox configuration file provides the matrix description to process all
  required tests and verifications.
- The tox matrix description introduce different Python runtime envionments
  for each required Python version.
- The tox matrix description introduce different Sphinx runtime envionments
  for each required Sphinx version.
- All tox jobs will be triggerd by the Travis-CI processing.

The tox configuration file covers the following test tools:

- check-manifest
- flake8
- nosetests

.. traceable-graph::
   :tags: IMP-TESTS-TOX
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement IMP-TESTS-TOX

Functional Implementations
-------------------------------------------------------------------------------

.. traceable:: IMP-SPHINXCONTRIB-BIBTEX
   :title: Import sphinxcontrib-bibtex
   :category: SysImpl
   :parents: REQ-BIBTEX, REQ-BIBLIOGRAPHY, REQ-BIBCITATION
   :implementation_type: functional
   :verification_method: ci-test

- This |publishing-withsphinx| extension provides the full functionality of
  the |sphinxcontrib-bibtex_dsc| extension.
- The |sphinxcontrib-bibtex| package name is part of the list of Python
  packages required to install before this |publishing-withsphinx| extension
  can be installed (see: :traceable:`STRQ-PIPINSTALL`).
- This |publishing-withsphinx| extension setup the |sphinxcontrib-bibtex|
  extension in each Sphinx context, so that a :traceable:`STKH-USERS` needs
  no further configuration or administration (see: :traceable:`STRQ-EXTSETUP`).

.. traceable-graph::
   :tags: IMP-SPHINXCONTRIB-BIBTEX
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement IMP-SPHINXCONTRIB-BIBTEX

.. ----------------------------------------------------------------------------

.. todo:: Define more functional implementations derived from SysReq.

   |functionality_being_continued|

Usability Implementations
-------------------------------------------------------------------------------

.. todo:: Define more usability implementations derived from SysReq.

   |usability_being_continued|

Documentation Implementations
-------------------------------------------------------------------------------

.. todo:: Define more documentation implementations derived from SysReq.

   |documentation_being_continued|

.. traceable:: IMP-USERMAN
   :title: Write the user's manual
   :category: SysImpl
   :parents: REQ-INSTALLINSTR
   :implementation_type: documentation
   :verification_method: doc-review

.. todo:: |documentation_being_continued|

.. traceable-graph::
   :tags: IMP-USERMAN
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement IMP-USERMAN

.. ----------------------------------------------------------------------------

.. traceable:: IMP-CHEATSHEET
   :title: Write the users's cheat sheet
   :category: SysImpl
   :parents: REQ-USAGEINSTR
   :implementation_type: documentation
   :verification_method: doc-review

.. todo:: |documentation_being_continued|

.. traceable-graph::
   :tags: IMP-CHEATSHEET
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement IMP-CHEATSHEET

.. ----------------------------------------------------------------------------

.. traceable:: IMP-DEVMAN
   :title: Write the developer's manual
   :category: SysImpl
   :parents: REQ-COMPMATRIX
   :implementation_type: documentation
   :verification_method: doc-review

.. todo:: |documentation_being_continued|

- The developer's manual covers the compatibility matrix with the following
  elements:

  - Python versions:

    .. traceable-list::
       :filter: category == "compatibility-python"
       :format: bullets

  - Sphinx versions:

    .. traceable-list::
       :filter: category == "compatibility-sphinx"
       :format: bullets

.. traceable-graph::
   :tags: IMP-DEVMAN
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement IMP-DEVMAN


Traceability
===============================================================================

The following system implementations (:literal:`IMP-*`) fulfill the related
system requirements (:literal:`REQ-*`):

.. only:: html

   .. raw:: latex

      \begin{minipage}[t]{0.5\textwidth}\scriptsize

   .. traceable-matrix::
      :filter-primaries: category == "SysReq"
      :filter-secondaries: category == "SysImpl"
      :split-primaries: 25
      :split-secondaries: 10
      :relationship: children
      :format: table

   .. raw:: latex

      \end{minipage}

.. only:: latex

   .. error:: Mal formatted LaTeX sequence in :code:`traceable-matrix`

      See issue #24 for details an ongoing fixes.

List of system implementations
-------------------------------------------------------------------------------

.. traceable-list::
   :filter: category == "SysImpl"
   :attributes: verification_method
   :format: table
