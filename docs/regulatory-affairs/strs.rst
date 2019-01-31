.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

.. _strs:

*******************************************************************************
Stakeholders Requirements Specification
*******************************************************************************


Introduction
===============================================================================

Document Purpose
-------------------------------------------------------------------------------

This Stakeholders Requirements Specification document identifies the parties
interested in the |publishing-withsphinx| extension, describes their needs,
combines the diverse needs in an |OpsCon|, and derives stakeholder
requirements.

This document's purpose is to ensure the extension meets its stakeholders'
expectations.

Document Scope
-------------------------------------------------------------------------------

This part of document describes the |publishing-withsphinx| extension. It is
limited to stakeholder-level aspects and therefore doesn't cover technical
details.

Document Structure
-------------------------------------------------------------------------------

The following chapters describe the stakeholders and their needs, combine those
needs into a single |OpsCon|, and derive stakeholder requirements.


Stakeholders and Their Needs
===============================================================================

Extension users
-------------------------------------------------------------------------------

.. traceable:: STKH-USERS
   :title: Extension users
   :category: Stakeholder

   This stakeholder represents users of the |publishing-withsphinx|
   extension, i.e. people who write |Sphinx|-based documentation.

This extension adds fancy publishing functionality to |Sphinx|. Its users can
start to write and publish online or printed documentation without
time-consuming configuration and setup procedure for various different
purposes, such as for example:

*Technical documentation*
   In engineering, technical documentation refers to any type of documentation
   that describes handling, functionality and architecture of a technical
   product or a product under development or use. Technical documentation may
   include:

   - :emphasis:`patents`
   - :emphasis:`specifications` of item or of components/materials
   - :emphasis:`data sheets` of item or of components/materials
   - :emphasis:`test methods`
   - :emphasis:`manufacturing standards`
   - :emphasis:`system requirements`
   - :emphasis:`system design`
   - :emphasis:`system architecture`

*Academic writing*
   In research and development, academic writing consists of a number of text
   types and genres, what they have in common, the conventions that academic
   writers traditionally follow, has been a subject of debate. Academic writing
   may include:

   - :emphasis:`thesis`
   - :emphasis:`dissertation`
   - :emphasis:`research paper`
   - :emphasis:`essay`

The users' needs are that this extension provides the functionality they want
and is easy to use:

- Desired functionality

  - Define references to a self managed bibliography.
  - Define content with syntax highlighting based on generic ANSI codec.
  - Define content with syntax highlighting based on self managed classes.
  - Define inline vector graphics based on the Blockdiag SDL.
  - Define inline vector graphics based on the PGF/TikZ SDL.
  - Define all content within |Sphinx| documentation without dependency to any
    external workflow.
  - Ganerate self managed bibliography in document's appendix.
  - Generate documentation test, coverage, and spelling reports.
  - Generate online and printed documentation from the same source of content.
  - Generate online and printed documentation with conformance to national or
    international standards.

- Ease-of-use

  - Easy installation
  - Intuitive usage
  - Informative error messages

These user needs are captured in the |OpsCon| and stakeholder requirements
below.

.. todo:: |user_needs_being_continued|

.. traceable-graph::
   :tags: STKH-USERS
   :relationships: children
   :caption: Stakeholders involved with user needs STKH-USERS
             and requirements derived from it

Extension developers
-------------------------------------------------------------------------------

.. traceable:: STKH-DEVS
   :title: Extension developers
   :category: Stakeholder

   This stakeholder represents developers of the |publishing-withsphinx|
   extension, i.e. people who create, expand, and maintain it.

The developers' needs are that this extension is designed well (easy to expand,
easy to maintain, fun to work on, etc.), well documented (easy to understand),
and well tested (easy to verify changes don't break it). Those needs are
captured in the |OpsCon| below.

.. traceable-graph::
   :tags: STKH-DEVS
   :relationships: children
   :caption: Stakeholders involved with user needs STKH-DEVS
             and requirements derived from it


Operational Concept
===============================================================================

Developer works on the extension
-------------------------------------------------------------------------------

.. traceable:: OPSCON-DEV
   :title: Developer works on the extension
   :category: OpsConScenario
   :parents: STKH-DEVS

This scenario covers a developer who works on this extension, expanding its
functionality, fixing bugs, writes documentation for it, etc.

.. todo:: |scenario_being_continued|

Developer releases the extension
-------------------------------------------------------------------------------

.. traceable:: OPSCON-RELEASE
   :title: Developer releases the extension
   :category: OpsConScenario
   :parents: STKH-DEVS

This scenario covers a developer who creates a formal release of this extension
and publishes that so that users can install the new release
(see :traceable:`OPSCON-INSTALL`).

.. todo:: |scenario_being_continued|

User installs the extension
-------------------------------------------------------------------------------

.. traceable:: OPSCON-INSTALL
   :title: User installs the extension
   :category: OpsConScenario
   :parents: STKH-USERS

This scenario covers a user who installs this extension. It consists of the
following activities:

#. A :traceable:`STKH-USERS` reads |publishing-withsphinx| user
   documentation, specifically the installation instructions.
#. The :traceable:`STKH-USERS` uses a standard method to install this extension;
   standard methods included here:

   - Python's built-in :literal:`pip` tool, i.e.
     :literal:`pip install publishing-withsphinx`

.. traceable-graph::
   :tags: OPSCON-INSTALL
   :relationships: parents:1, children:1
   :caption: Stakeholders involved with scenario OPSCON-INSTALL
             and requirements derived from it

User writes documentation
-------------------------------------------------------------------------------

.. traceable:: OPSCON-USAGE
   :title: User writes documentation for publishing
   :category: OpsConScenario
   :parents: STKH-USERS

This scenario covers a user who writes |Sphinx|-based documentation that must
be published online and/or as printed medium with support of functionality
provided by this extension. It consists of the following activities:

#. A :traceable:`STKH-USERS` reads |publishing-withsphinx| user
   documentation to learn how to use the extension's functionality.
#. The :traceable:`STKH-USERS` writes input for |Sphinx|.
   The |publishing-withsphinx| extension provides the following
   functionality:

   - Define references to a self managed bibliography.
   - Define content with syntax highlighting based on generic ANSI codec.
   - Define content with syntax highlighting based on self managed classes.
   - Define inline vector graphics based on the Blockdiag SDL.
   - Define inline vector graphics based on the PGF/TikZ SDL.
   - Define all content within |Sphinx| documentation without dependency to any
     external workflow.
   - Ganerate self managed bibliography in document's appendix.
   - Generate documentation test, coverage, and spelling reports.
   - Generate online and printed documentation from the same source of content.
   - Generate online and printed documentation with conformance to national or
     international standards.

#. The :traceable:`STKH-USERS` runs |Sphinx| and generates output.
#. If the input contains errors related to the extension, then this extension
   gives clear error messages helping the user to quickly understand and fix
   the error.

.. traceable-graph::
   :tags: OPSCON-USAGE
   :relationships: parents:1, children:1
   :caption: Stakeholders involved with scenario OPSCON-USAGE
             and requirements derived from it


Stakeholder Requirements
===============================================================================

Requirements for installation and running
-------------------------------------------------------------------------------

.. traceable:: STRQ-USERDOCS
   :title: High-quality documentation for users
   :category: StakeholderReq
   :parents: OPSCON-INSTALL, OPSCON-USAGE

Users require documentation to help them use this extension. That documentation
must cover at least the following topics:

- How to install the extension (see :traceable:`OPSCON-INSTALL`)
- How to use the functionalities in their documentations
  (see :traceable:`OPSCON-USAGE`)
- How to fix errors if the user incorrectly uses the functionalities
  (see :traceable:`OPSCON-USAGE`)

.. traceable-graph::
   :tags: STRQ-USERDOCS
   :relationships: parents
   :caption: Traces to the stakeholder requirement STRQ-USERDOCS

.. ----------------------------------------------------------------------------

.. traceable:: STRQ-PIPINSTALL
   :title: Easy installation using pip
   :category: StakeholderReq
   :parents: OPSCON-INSTALL

A very common way to install Python packages is to use the :literal:`pip` tool.
It must therefore be possible for users to easily install this extension using
the :literal:`pip` tool.

For all supported but foreign Sphinx extensions this |publishing-withsphinx|
extension should install additional Sphinx extensions and its dependent
Python packages automatically.

For all foreign Python packages needed for the extension development this
|publishing-withsphinx| extension should install additional Python packages
and its dependencies automatically.

The Python package installation with :literal:`pip` **should support** the
following current versions of Python:

- `Status of Python branches <https://devguide.python.org/#branchstatus>`_:

  - `Python 3.7.x <https://www.python.org/dev/peps/pep-0537/>`_ until June 2023
  - `Python 3.6.x <https://www.python.org/dev/peps/pep-0494/>`_ until December 2021
  - `Python 3.5.x <https://www.python.org/dev/peps/pep-0478/>`_ until September 2020
  - `Python 3.4.x <https://www.python.org/dev/peps/pep-0429/>`_ until March 2019
  - `Python 2.7.x <https://www.python.org/dev/peps/pep-0373/>`_,
    `Update Python 2.7 EOL date <https://github.com/python/devguide/pull/344>`_ until December 2019

The Python package installation with :literal:`pip` **have not to support** the
following current versions of Python:

- `End-of-life branches <https://devguide.python.org/#branchstatus>`_

  - `Python 3.3.x <https://www.python.org/dev/peps/pep-0398/>`_ since September 2017
  - `Python 3.2.x <https://www.python.org/dev/peps/pep-0392/>`_ since February 2016
  - `Python 3.1.x <https://www.python.org/dev/peps/pep-0375/>`_ since April 2012
  - `Python 3.0.x <https://www.python.org/dev/peps/pep-0361/>`_ since January 2009
  - `Python 2.6.x <https://www.python.org/dev/peps/pep-0361/>`_ since October 2013

.. traceable-graph::
   :tags: STRQ-PIPINSTALL
   :relationships: parents
   :caption: Traces to the stakeholder requirement STRQ-PIPINSTALL

.. ----------------------------------------------------------------------------

.. traceable:: STRQ-EXTSETUP
   :title: Easy configuration and setup of Sphinx
   :category: StakeholderReq
   :parents: OPSCON-USAGE

A :traceable:`STKH-USERS` should be protected from unnecessary configurations
and setups. The administrations should be hidden and run automatically. For
all supported but foreign Sphinx extensions this |publishing-withsphinx|
extension should:

- load Sphinx extensions automatically.
- set basic and additional configuration options to defaults as needed.

The Sphinx configuration and setup functionality should support the following
current versions of Sphinx:

- `Sphinx 1.5.x <http://www.sphinx-doc.org/en/latest/changes.html#release-1-5-5-released-apr-03-2017>`_
- `Sphinx 1.4.x <http://www.sphinx-doc.org/en/latest/changes.html#release-1-4-9-released-nov-23-2016>`_
- `Sphinx 1.3.x <http://www.sphinx-doc.org/en/latest/changes.html#release-1-3-6-released-feb-29-2016>`_
- `Sphinx 1.2.x <http://www.sphinx-doc.org/en/latest/changes.html#release-1-2-3-released-sep-1-2014>`_

.. traceable-graph::
   :tags: STRQ-EXTSETUP
   :relationships: parents
   :caption: Traces to the stakeholder requirement STRQ-EXTSETUP

.. ----------------------------------------------------------------------------

.. traceable:: STRQ-CLEARERRMSG
   :title: Clear error messages
   :category: StakeholderReq
   :parents: OPSCON-USAGE

If a user makes an error in his usage of this extension, then this extension
should give a clear error message that helps the user quickly find and fix the
error (see :traceable:`OPSCON-USAGE`).

|Sphinx| automatically reports on general syntax errors in its input files,
usually written in |reST| format. This extension therefore does not need to
handle such errors.

The error messages to be generated by this extension are mainly related to
invalid parameters given to its directives and invalid configuration settings.

.. traceable-graph::
   :tags: STRQ-CLEARERRMSG
   :relationships: parents
   :caption: Traces to the stakeholder requirement STRQ-CLEARERRMSG

Requirements for functionality when writing documents with this extension
-------------------------------------------------------------------------------

.. traceable:: STRQ-DEFBIB
   :title: Definition of a self managed bibliography
   :category: StakeholderReq
   :parents: OPSCON-USAGE

A user must ba able to define citations to a bibliographic entry
within |Sphinx| source files using standard |reST| constructs
(see :traceable:`OPSCON-USAGE`).

The definition of citation must:

- Give a unique tag to the bibliographic entry, so that it can be referenced
  throughout the rest of the documentation set.
- Give a entry type to the bibliographic entry, such as: article, book, manual.
- Give a title to the bibliographic entry.
- Give a author or editors to the bibliographic entry.
- Optionally arbitrary additional attributes can be defined for the
  bibliographic entry:

  - Examples of additional attributes are: the publisher's name, month and
    year of publication, edition of a book, ISBN or ISDN.
  - Such attributes can be used to render direct hyperlinks to common book
    stores or library database systems.

.. traceable-graph::
   :tags: STRQ-DEFBIB
   :relationships: parents
   :caption: Traces to the stakeholder requirement STRQ-DEFBIB

.. ----------------------------------------------------------------------------

.. traceable:: STRQ-SHOWBIB
   :title: Generate the self managed bibliography in appendix
   :category: StakeholderReq
   :parents: OPSCON-USAGE

A user must be able to define different bibliographies at arbitrary locations
within |Sphinx| source files using standard |reST| constructs
(see :traceable:`OPSCON-USAGE`).

The definition of a bibliography must:

- Lists of bibliographic entry definitions and their attributes.
- Lists of bibliographic entry definitions will generate a bibliography
  in the document's appendix.
- Show differnet information for bibliographic entries depending on
  their entry types.

.. traceable-graph::
   :tags: STRQ-SHOWBIB
   :relationships: parents
   :caption: Traces to the stakeholder requirement STRQ-SHOWBIB

.. ----------------------------------------------------------------------------

.. .. traceable:: STRQ-DEFINETRCBLS
..    :title: Definition of traceables
..    :category: StakeholderReq
..    :parents: OPSCON-USAGE
.. 
.. A user must be able to define traceables at arbitrary locations
.. within |Sphinx| source files using standard |reST| constructs
.. (see :traceable:`OPSCON-USAGE`).
.. 
.. The definition of a traceable must:
.. 
.. - Give a unique tag to the traceable, so that it can be referenced
..   throughout the rest of the documentation set
.. - Optionally give a title to the traceable
.. - Optionally define the traceable's relationships with other traceables
.. 
..   - A traceable can have zero or more relationships with other traceables
..   - Each pair of related traceables can be related by one or more
..     relationship types
.. 
.. - Optionally arbitrary additional attributes can be defined for
..   the traceable
.. 
..   - Examples of additional attributes are: the category, version, color,
..     or foo-value of the traceable
..   - Such attributes can be used to group, filter, arrange, etc. traceables
.. 
.. .. traceable-graph::
..    :tags: STRQ-DEFINETRCBLS
..    :relationships: parents
..    :caption: Traces to the stakeholder requirement STRQ-DEFINETRCBLS

.. ----------------------------------------------------------------------------

.. .. traceable:: STRQ-SHOWTRACES
..    :title: Generate overviews of traceables, their attributes, and their
..            relationships
..    :category: StakeholderReq
..    :parents: OPSCON-USAGE
.. 
.. A user must be able to define traceables at arbitrary locations
.. within |Sphinx| source files using standard |reST| constructs
.. (see :traceable:`OPSCON-USAGE`).
.. 
.. The definition of a traceable must:
.. 
.. - Lists of traceables and their attributes
.. - Tables and nested lists showing related traceables
.. - Graphs showing the relationships between traceables
.. 
.. .. traceable-graph::
..    :tags: STRQ-SHOWTRACES
..    :relationships: parents
..    :caption: Traces to the stakeholder requirement STRQ-SHOWTRACES

.. ----------------------------------------------------------------------------

.. .. traceable:: STRQ-CONFIGRELTYPES
..    :title: Configurable relationship types between traceables
..    :category: StakeholderReq
..    :parents: OPSCON-USAGE
.. 
.. It must be possible to configure the types of relationships that are valid
.. for a documentation set (see :traceable:`OPSCON-USAGE`).
.. 
.. The valid relationship types can be configured via |Sphinx|'s standard
.. configuration method, namely in the `build configuration file`_.
.. 
.. .. _build configuration file: http://www.sphinx-doc.org/en/stable/config.html
.. 
.. .. traceable-graph::
..    :tags: STRQ-CONFIGRELTYPES
..    :relationships: parents
..    :caption: Traces to the stakeholder requirement STRQ-CONFIGRELTYPES

Requirements for developers working on this extension
-------------------------------------------------------------------------------

.. traceable:: STRQ-DEVDOCS
   :title: High-quality documentation for developers
   :category: StakeholderReq
   :parents: OPSCON-DEV, OPSCON-RELEASE

Developers require documentation to help them understand and improve this
extension. That documentation must cover at least the following topics:

- How this extension is internally structured, so that its workings can easily
  be understood and so that modifications or improvements will be implemented
  in-line with its design philosophy (see :traceable:`OPSCON-DEV`)
- How to submit modifications, improvements or bug fixes for review and, if
  accepted, inclusion in the central repository (see :traceable:`OPSCON-DEV`)
- How to create and publish a formal release of this extension
  (see :traceable:`OPSCON-RELEASE`)

.. traceable-graph::
   :tags: STRQ-DEVDOCS
   :relationships: parents
   :caption: Traces to the stakeholder requirement STRQ-DEVDOCS

.. ----------------------------------------------------------------------------

.. traceable:: STRQ-TESTS
   :title: High-quality tests of this extension's functionality
   :category: StakeholderReq
   :parents: OPSCON-DEV, OPSCON-RELEASE

.. todo:: |functionality_being_continued|

.. traceable-graph::
   :tags: STRQ-TESTS
   :relationships: parents
   :caption: Traces to the stakeholder requirement STRQ-TESTS

.. ----------------------------------------------------------------------------

.. traceable:: STRQ-CONTINTEGR
   :title: Continuous integration setup for this extension
   :category: StakeholderReq
   :parents: OPSCON-DEV, OPSCON-RELEASE

.. todo:: |functionality_being_continued|

.. traceable-graph::
   :tags: STRQ-CONTINTEGR
   :relationships: parents
   :caption: Traces to the stakeholder requirement STRQ-CONTINTEGR
