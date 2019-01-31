.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

.. _syrs:

*******************************************************************************
System Requirements Specification
*******************************************************************************


Introduction
===============================================================================

Document Purpose
-------------------------------------------------------------------------------

This System Requirements Specification document identifies the technical
needs, combines the diverse needs in several concepts, and derives system
requirements.

This document's purpose is to provide clear requirements for development of
this extension and to ensure the extension meets its developer's expectations.

Document Scope
-------------------------------------------------------------------------------

This part of document describes the |publishing-withsphinx| extension. It is
limited to system-level aspects.

Document Structure
-------------------------------------------------------------------------------

The following chapters describe the system and their needs, combine those
needs into several concepts, and derives system requirements.


Stakeholder Requirements
===============================================================================

The |StRS| defined the following stakeholder requirements:

.. traceable-list::
   :filter: category == "StakeholderReq"


System Requirements
===============================================================================

Configuration Requirements
-------------------------------------------------------------------------------

.. traceable:: REQ-TESTS-CI
   :title: All requirements can be verified on a CI infrastructure
   :category: SysReq
   :parents: STRQ-TESTS, STRQ-CONTINTEGR
   :requirement_type: configuration
   :verification_method: ci-test

It must be possible to run all unit and functional tests in a suitable
continuous integration infrastructure. The unit and functional tests
have to protect all requirements against any malfunction or any wrong
or unexpected implementation.

The selected CI infrastructure must be able to support a build and test
matrix over all required Python and Sphinx versions. The test matrix should
run unit and functional tests and collect all informations over the code
coverage. The build matrix should run usual Python source packaging and
generate documentation. The CI infrastructure can be used to release and
upload distribution packages and the documentation.

The coverage of the build matrix have to be documented in the compatibility
matrix as part of the :traceable:`STRQ-DEVDOCS`
(see: :traceable:`REQ-COMPMATRIX`).

The |SyRS| defines the following required Python versions:

.. traceable-list::
   :filter: requirement_type == "configuration-python"
   :format: bullets

The |SyRS| defines the following required Sphinx versions:

.. traceable-list::
   :filter: requirement_type == "configuration-sphinx"
   :format: bullets

.. traceable-graph::
   :tags: REQ-TESTS-CI
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-TESTS-CI

Python Version Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. traceable:: REQ-WORKSON-PY27
   :title: Python version 2.7.x can be used to install this extension
   :category: SysReq
   :parents: STRQ-PIPINSTALL
   :sibling: REQ-TESTS-CI
   :requirement_type: configuration-python
   :verification_method: ci-test

.. .. index::
      single: Python; Python 2; REQ-WORKSON-PY27

It must be possible to install this |publishing-withsphinx| extension in a
Python 2.7.x environment and write documentation with one of the required
Sphinx versions.

.. traceable-graph::
   :tags: REQ-WORKSON-PY27
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-WORKSON-PY27

.. ----------------------------------------------------------------------------

.. traceable:: REQ-WORKSON-PY37
   :title: Python version 3.7.x can be used to install this extension
   :category: SysReq
   :parents: STRQ-PIPINSTALL
   :sibling: REQ-TESTS-CI
   :requirement_type: configuration-python
   :verification_method: ci-test

.. .. index::
      single: Python; Python 3; REQ-WORKSON-PY37

It must be possible to install this |publishing-withsphinx| extension in a
Python 3.7.x environment and write documentation with one of the required
Sphinx versions.

.. traceable-graph::
   :tags: REQ-WORKSON-PY37
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-WORKSON-PY37

.. ----------------------------------------------------------------------------

.. traceable:: REQ-WORKSON-PY36
   :title: Python version 3.6.x can be used to install this extension
   :category: SysReq
   :parents: STRQ-PIPINSTALL
   :sibling: REQ-TESTS-CI
   :requirement_type: configuration-python
   :verification_method: ci-test

.. .. index::
      single: Python; Python 3; REQ-WORKSON-PY36

It must be possible to install this |publishing-withsphinx| extension in a
Python 3.6.x environment and write documentation with one of the required
Sphinx versions.

.. traceable-graph::
   :tags: REQ-WORKSON-PY36
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-WORKSON-PY36

.. ----------------------------------------------------------------------------

.. traceable:: REQ-WORKSON-PY35
   :title: Python version 3.5.x can be used to install this extension
   :category: SysReq
   :parents: STRQ-PIPINSTALL
   :sibling: REQ-TESTS-CI
   :requirement_type: configuration-python
   :verification_method: ci-test

.. .. index::
      single: Python; Python 3; REQ-WORKSON-PY35

It must be possible to install this |publishing-withsphinx| extension in a
Python 3.5.x environment and write documentation with one of the required
Sphinx versions.

.. traceable-graph::
   :tags: REQ-WORKSON-PY35
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-WORKSON-PY35

.. ----------------------------------------------------------------------------

.. traceable:: REQ-WORKSON-PY34
   :title: Python version 3.4.x can be used to install this extension
   :category: SysReq
   :parents: STRQ-PIPINSTALL
   :sibling: REQ-TESTS-CI
   :requirement_type: configuration-python
   :verification_method: ci-test

.. .. index::
      single: Python; Python 3; REQ-WORKSON-PY34

It must be possible to install this |publishing-withsphinx| extension in a
Python 3.4.x environment and write documentation with one of the required
Sphinx versions.

.. traceable-graph::
   :tags: REQ-WORKSON-PY34
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-WORKSON-PY34

Sphinx Version Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. traceable:: REQ-WORKSON-SP15
   :title: Sphinx version 1.5.x can be used to write documentation
   :category: SysReq
   :parents: STRQ-EXTSETUP
   :sibling: REQ-TESTS-CI
   :requirement_type: configuration-sphinx
   :verification_method: ci-test

.. .. index::
      single: Sphinx; Sphinx 1.x; REQ-WORKSON-SP15

It must be possible to install this |publishing-withsphinx| extension in a
Sphinx 1.5.x environment and write documentation with this version of Sphinx.

Refer to the prerequisites [#sp15-pr]_ of the Sphinx 1.5 documentation builder:

   "Sphinx needs at least Python 2.7 or Python 3.4 to run, ..."

.. traceable-graph::
   :tags: REQ-WORKSON-SP15
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-WORKSON-SP15

.. ----------------------------------------------------------------------------

.. traceable:: REQ-WORKSON-SP14
   :title: Sphinx version 1.4.x can be used to write documentation
   :category: SysReq
   :parents: STRQ-EXTSETUP
   :sibling: REQ-TESTS-CI
   :requirement_type: configuration-sphinx
   :verification_method: ci-test

.. .. index::
      single: Sphinx; Sphinx 1.x; REQ-WORKSON-SP14

It must be possible to install this |publishing-withsphinx| extension in a
Sphinx 1.4.x environment and write documentation with this version of Sphinx.

Refer to the prerequisites [#sp14-pr]_ of the Sphinx 1.4 documentation builder:

   "Sphinx needs at least Python 2.6 or Python 3.3 to run, ..."

.. traceable-graph::
   :tags: REQ-WORKSON-SP14
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-WORKSON-SP14

.. ----------------------------------------------------------------------------

.. traceable:: REQ-WORKSON-SP13
   :title: Sphinx version 1.3.x can be used to write documentation
   :category: SysReq
   :parents: STRQ-EXTSETUP
   :sibling: REQ-TESTS-CI
   :requirement_type: configuration-sphinx
   :verification_method: ci-test

.. .. index::
      single: Sphinx; Sphinx 1.x; REQ-WORKSON-SP13

It must be possible to install this |publishing-withsphinx| extension in a
Sphinx 1.3.x environment and write documentation with this version of Sphinx.

Refer to the prerequisites [#sp13-pr]_ of the Sphinx 1.3 documentation builder:

   "Sphinx needs at least Python 2.6 or Python 3.3 to run, ..."

.. traceable-graph::
   :tags: REQ-WORKSON-SP13
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-WORKSON-SP13

.. ----------------------------------------------------------------------------

.. traceable:: REQ-WORKSON-SP12
   :title: Sphinx version 1.2.x can be used to write documentation
   :category: SysReq
   :parents: STRQ-EXTSETUP
   :sibling: REQ-TESTS-CI
   :requirement_type: configuration-sphinx
   :verification_method: ci-test

.. .. index::
      single: Sphinx; Sphinx 1.x; REQ-WORKSON-SP12

It must be possible to install this |publishing-withsphinx| extension in a
Sphinx 1.2.x environment and write documentation with this version of Sphinx.

Refer to the prerequisites [#sp12-pr]_ of the Sphinx 1.2 documentation builder:

   "Sphinx needs at least Python 2.5 or Python 3.1 to run, ..."

.. traceable-graph::
   :tags: REQ-WORKSON-SP12
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-WORKSON-SP12

Functional Requirements
-------------------------------------------------------------------------------

.. traceable:: REQ-BIBCITATION
   :title: Citation to a bibliographic entry can be defined using reST
           inline markup
   :category: SysReq
   :parents: STRQ-DEFBIB
   :requirement_type: functional
   :verification_method: ci-test

It must be possible to define a citation to a bibliographic entry using a
|reST| inline markup.

Inline markup is an implementation similar to the
`Cross-referencing arbitrary locations`_ and has no further options.

.. _Cross-referencing arbitrary locations:
   http://www.sphinx-doc.org/en/latest/markup/inline.html#cross-referencing-arbitrary-locations

.. traceable-graph::
   :tags: REQ-BIBCITATION
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-BIBCITATION

.. ----------------------------------------------------------------------------

.. traceable:: REQ-BIBTEX
   :title: Bibliography entry can be defined using BibTeX type
   :category: SysReq
   :parents: STRQ-DEFBIB
   :requirement_type: functional
   :verification_method: ci-test

It must be possible to define a bibliography entry using a |BibTeX| type.

Type options define the bibliography entry's tags. Certain option tags have
special meaning following the `BibTeX Format Description`_

.. _BibTeX Format Description: http://www.bibtex.org/Format/

.. traceable-graph::
   :tags: REQ-BIBTEX
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-BIBTEX

.. ----------------------------------------------------------------------------

.. traceable:: REQ-BIBLIOGRAPHY
   :title: Bibliography for citations can be defined using reST directive
   :category: SysReq
   :parents: STRQ-SHOWBIB
   :requirement_type: functional
   :verification_method: ci-test

It must be possible to define a bibliography using a |reST| directive.

Directive options define the bibliography's attributes. Certain option keys
have special meaning:

- sets the bibliography style how to sort and order all bibliography entries
- filter for local bibliographies

.. traceable-graph::
   :tags: REQ-BIBLIOGRAPHY
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-BIBLIOGRAPHY

.. ----------------------------------------------------------------------------

.. .. traceable:: REQ-TRACEDIRECTIVE
..    :title: Traceables can be defined using reST directive
..    :category: SysReq
..    :parents: STRQ-DEFINETRCBLS
..    :requirement_type: functional
..    :verification_method: ci-test
.. 
.. It must be possible to define a traceable using a |reST| directive.
.. 
.. Directive options define the traceable's attributes. Certain option keys
.. have special meaning:
.. 
.. - :literal:`:title:` sets the traceable's title attribute
.. - Options with the name of a valid relationship define the traceable's
..   relationships with other traceables
.. 
.. Directive content defines arbitrary information that is associated with
.. the traceable. It is shown in line where the traceable is displayed
.. in full, but otherwise not used in traceable processing, filtering, etc.
.. The content is parsed as |reST| code.
.. 
.. .. traceable-graph::
..    :tags: REQ-TRACEDIRECTIVE
..    :relationships: parents:2, children:1
..    :caption: Traces to the system requirement REQ-TRACEDIRECTIVE

.. ----------------------------------------------------------------------------

.. .. traceable:: REQ-TRACELISTS
..    :title: Lists can be generated showing traceables and their attributes
..    :category: SysReq
..    :parents: STRQ-SHOWTRACES
..    :requirement_type: functional
..    :verification_method: ci-test
.. 
.. It must be possible to generate lists of traceables using a |reST|
.. directive. The directive's options allow filtering and formatting of
.. the output.
.. 
.. .. traceable-graph::
..    :tags: REQ-TRACELISTS
..    :relationships: parents:2, children:1
..    :caption: Traces to the system requirement REQ-TRACELISTS
    
.. ----------------------------------------------------------------------------

.. .. traceable:: REQ-TRACEMATRICES
..    :title: Matrices can be generated showing relationships between traceables
..    :category: SysReq
..    :parents: STRQ-SHOWTRACES
..    :requirement_type: functional
..    :verification_method: ci-test
.. 
.. It must be possible to generate matrices of traceables using a |reST|
.. directive. The directive's options allow filtering and formatting of
.. the output.
.. 
.. .. traceable-graph::
..    :tags: REQ-TRACEMATRICES
..    :relationships: parents:2, children:1
..    :caption: Traces to the system requirement REQ-TRACEMATRICES
    
.. ----------------------------------------------------------------------------

.. .. traceable:: REQ-TRACEGRAPHS
..    :title: Graphs can be generated showing relationships between traceables
..    :category: SysReq
..    :parents: STRQ-SHOWTRACES
..    :requirement_type: functional
..    :verification_method: ci-test
.. 
.. It must be possible to generate graphs of traceables using a |reST|
.. directive. The directive's options allow filtering and formatting of
.. the output.
.. 
.. .. traceable-graph::
..    :tags: REQ-TRACEGRAPHS
..    :relationships: parents:2, children:1
..    :caption: Traces to the system requirement REQ-TRACEGRAPHS
    
.. ----------------------------------------------------------------------------

.. .. traceable:: REQ-
   :title:
   :category: SysReq
   :parents: STRQ-
   :requirement_type: functional
   :verification_method: ci-test

.. .. todo:: |functionality_being_continued|

.. .. traceable-graph::
   :tags: REQ-
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-

Usability Requirements
-------------------------------------------------------------------------------

.. traceable:: REQ-AUTOINSTSET
   :title: Install and setup all supported Sphinx extensions automatically
   :category: SysReq
   :parents: STRQ-PIPINSTALL, STRQ-EXTSETUP
   :requirement_type: usability
   :verification_method: ci-test
    
.. todo:: |usability_being_continued|

.. traceable-graph::
   :tags: REQ-AUTOINSTSET
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-AUTOINSTSET
    
.. ----------------------------------------------------------------------------

.. traceable:: REQ-ERRORMESSAGES
   :title: Helpful error messages are generated upon incorrect usage
           of this extension
   :category: SysReq
   :parents: STRQ-CLEARERRMSG
   :requirement_type: usability
   :verification_method: ci-test
    
.. todo:: |usability_being_continued|

.. traceable-graph::
   :tags: REQ-ERRORMESSAGES
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-ERRORMESSAGES

Documentation Requirements
-------------------------------------------------------------------------------

.. traceable:: REQ-INSTALLINSTR
   :title: User documents contain installation instructions
   :category: SysReq
   :parents: STRQ-USERDOCS
   :requirement_type: documentation
   :verification_method: doc-review

The user documentation must describe how to install this extension and all
needed depndencies. The documentaion must give a full informations about
all prerequisites and configuration options to start to write documentation.

.. traceable-graph::
   :tags: REQ-INSTALLINSTR
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-INSTALLINSTR

.. ----------------------------------------------------------------------------

.. traceable:: REQ-USAGEINSTR
   :title: User documents contain usage instructions
   :category: SysReq
   :parents: STRQ-USERDOCS
   :requirement_type: documentation
   :verification_method: doc-review
    
The user documentation must describe how to use the features provided by
this extension. It must cover at least all features as stated by the
functional requirements:

.. traceable-list::
   :filter: category == "SysReq" and requirement_type == "functional"
   :format: bullets
    
.. traceable-graph::
   :tags: REQ-USAGEINSTR
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-USAGEINSTR

.. ----------------------------------------------------------------------------

.. traceable:: REQ-COMPMATRIX
   :title: User documents contain usage instructions
   :category: SysReq
   :parents: STRQ-DEVDOCS
   :sibling: REQ-TESTS-CI
   :requirement_type: documentation
   :verification_method: doc-review
    
The developers documentation must cover a compatibility matrix over all
supported Python and Sphinx versions. The fulfilled relations have to
represent by detailed informations over setup and configuration of the
build matrix (see: :traceable:`REQ-TESTS-CI`). It must cover at least
all versions as stated by the configuration requirements:

.. traceable-list::
   :filter: category == "SysReq" and ( requirement_type == "configuration-python" or requirement_type == "configuration-sphinx" )
   :format: bullets
    
.. traceable-graph::
   :tags: REQ-COMPMATRIX
   :relationships: parents:2, children:1
   :caption: Traces to the system requirement REQ-COMPMATRIX


Traceability
===============================================================================

The following system requirements (:literal:`REQ-*`) fulfill the related
stakeholder requirements (:literal:`STRQ-*`):

.. raw:: latex

   \begin{minipage}[t]{0.5\textwidth}\scriptsize

.. traceable-matrix::
   :filter-primaries: category == "StakeholderReq"
   :filter-secondaries: category == "SysReq"
   :split-primaries: 25
   :split-secondaries: 10
   :relationship: children
   :format: table

.. raw:: latex

   \end{minipage}

List of system requirements
-------------------------------------------------------------------------------

.. traceable-list::
   :filter: category == "SysReq"
   :attributes: verification_method
   :format: table


.. ----------------------------------------------------------------------------

.. rubric:: Footnotes

.. [#sp12-pr] :traceable:`REQ-WORKSON-SP12` prerequisites:
              http://www.sphinx-doc.org/en/1.2/intro.html#prerequisites

.. [#sp13-pr] :traceable:`REQ-WORKSON-SP13` prerequisites:
              http://www.sphinx-doc.org/en/1.3/intro.html#prerequisites

.. [#sp14-pr] :traceable:`REQ-WORKSON-SP14` prerequisites:
              http://www.sphinx-doc.org/en/1.4/intro.html#prerequisites

.. [#sp15-pr] :traceable:`REQ-WORKSON-SP15` prerequisites:
              http://www.sphinx-doc.org/en/1.5/intro.html#prerequisites
