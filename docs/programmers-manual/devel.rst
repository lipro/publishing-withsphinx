.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

.. _development:

******************************************************************************
Development
******************************************************************************

.. index:: ! Development
   single: Compatibility Matrix; Development
   pair: Development; Getting started
   pair: Development; Building
   pair: Development; Testing
   pair: Development; Releasing
   pair: Development; Install

This section contains some information about module development - in a case
you want to contribute to it. Which is welcome, btw.

.. contents:: In this section:
   :local:
   :depth: 1
   :backlinks: none


Getting started
==============================================================================

.. index:: ! Getting started

To get started with the development, you will need a proper Python 2.7 or
Python 3.6 runtime environment. Installing Python is generally easy, and
nowadays many Linux and UNIX distributions include a recent Python.

For development of this module it is recommended to use a Python Virtual
Environment. A Virtual Environment is a tool to keep the dependencies required
by different projects in separate places, by creating virtual Python
environments for them. It solves the “Project X depends on version 1.x but,
Project Y needs 4.x” dilemma, and keeps your global site-packages directory
clean and manageable.

As long as the development of this module needs different Python versions for
test purposes, the one version distributed by the system is not enought. The
next subsections will explain how to install all needed Python versions in
parallel including a functioning Virtual Environment on a recent Ubuntu LTS
standard Linux system.

Python 2 and 3 on Ubuntu 12.04 (and onwards LTS)
------------------------------------------------------------------------------

.. index:: Python
.. index:: Install
   pair: Python; Install

A third party launchpad
`PPA <https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes>`_,
the DeadSnakes PPA by
`Felix Krull <https://launchpad.net/~fkrull>`_,
maintains older and newer Python version for Ubuntu not included in the systems
package management. For Python 2.7 security and feature updates he is
maintainig a dedicated
`2.7 PPA <https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes-python2.7>`_
(see PPA home page for the reasons). All the needed Python releases are
available in the PPA for Ubuntu 16.04 and down to Ubuntu 12.04.

Python 3 Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Python; Python 3; Install

Add the DeadSnakes repository and run update:
   .. code-block:: bash

      sudo add-apt-repository ppa:fkrull/deadsnakes
      sudo apt-get update

   See: https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes

Install all versions of Python 3:
   .. code-block:: bash

      sudo apt-get install python-virtualenv
      sudo apt-get install python3.1 python3.1-dev
      sudo apt-get install python3.2 python3.2-dev
      sudo apt-get install python3.3 python3.3-dev
      sudo apt-get install python3.4 python3.4-dev python3.4-venv
      sudo apt-get install python3.5 python3.5-dev python3.5-venv
      sudo apt-get install python3.6 python3.6-dev python3.6-venv

   See: https://wiki.ubuntuusers.de/virtualenv/#Installation

Python 3.6 Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Python; Python 3; Virtual Environment
   single: Virtual Environment; Python 3

Activate Python 3.6 Virtual Environment:
   .. code-block:: bash

      python3.6 -m venv .py36env
      source .py36env/bin/activate

   See: https://wiki.ubuntuusers.de/virtualenv/#venv-aus-Python-3

   Python 3 (from Python 3.3) comes with an ready to use module for a Python
   Virtual Environment. The module is :literal:`venv` and has to be used.

Upgrade :program:`pip` and install required packages:
   .. code-block:: bash

      pip install --upgrade pip
      pip install --process-dependency-links -e .[dev,test]

   Within the virtual Python 3.6 runtime environment upgrade and install all
   required Python packages.

Python 2 Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Python; Python 2; Install

Add the DeadSnakes repository and run update:
   .. code-block:: bash

      sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7
      sudo apt-get update

   See: https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes-python2.7

Install all versions of Python 2:
   .. code-block:: bash

      sudo apt-get install python-virtualenv
      sudo apt-get install python2.6 python2.6-dev
      sudo apt-get install python2.7 python2.7-dev

   See: https://wiki.ubuntuusers.de/virtualenv/#Installation

Python 2.7 Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Python; Python 2; Virtual Environment
   single: Virtual Environment; Python 2

Activate Python 2.7 Virtual Environment:
   .. code-block:: bash

      virtualenv --no-site-packages .py27env
      source .py27env/bin/activate

   See: https://wiki.ubuntuusers.de/virtualenv/#virtualenv

   Python 2 needs to call the command line interface of the module
   :literal:`virtualenv`.

Upgrade :program:`pip` and install required packages:
   .. code-block:: bash

      pip install --upgrade pip
      pip install --process-dependency-links -e .[dev,test]

   Within the virtual Python 2.7 runtime environment upgrade and install all
   required Python packages.


.. _building:

Building
==============================================================================

.. index:: ! Building

Create a source distribution:
   .. code-block:: bash

      python setup.py sdist

Create a built (binary) distribution:
   .. code-block:: bash

      python setup.py bdist
      python setup.py bdist_wheel

Perform some checks on the package:
   .. code-block:: bash

      python setup.py check

Run unit tests using nosetests or after in-place build:
   .. code-block:: bash

      python setup.py nosetests
      python setup.py test

Run a specific colection of unit tests using nosetests:
   .. code-block:: bash

      python setup.py nosetests \
        --tests tests/test_module_meta.py:TestPublishingWithSphinxMetaData

Run a specific unit test using nosetests:
   .. code-block:: bash

      python setup.py nosetests \
        --tests tests/test_sphinx_ext_todo.py:TestCaseSphinxExtTodo.test_build_text

Build Sphinx documentation:
   .. code-block:: bash

      python setup.py build_sphinx

   Within any virtual Python 3.x runtime environment you will run into a
   well known build issue within the :literal:`sphinxcontrib.traceables`
   extension. See main issue tracker or file :literal:`TODO` for more
   details.

Cleanup all build artefacts:
   .. code-block:: bash

      python setup.py distclean


.. _testing:

Testing
==============================================================================

.. index:: ! Testing

The project uses |nose| for unit testing, |coverage| for testing coverage
reporting and |tox| for compliance testing. To execute the tests, run:

- Unittests: :program:`python setup.py nosetests`
- Compliance: :program:`tox`

The project repository comes with ready-made configuration for both of the
tools, which are used automatically.


.. _releasing:

Releasing
==============================================================================

.. index:: ! Releasing

Steps to make a release:

#. Increase the version number in :file:`publishing/withsphinx/__init__.py`
   and extend the information in :file:`CHANGES`

#. Run all compliance tests:

   .. code-block:: bash

      tox

#. Build documentation:

   .. code-block:: bash

      # NOTE: Sphinx-pypi-upload runs only with Python 2
      pip install sphinx-pypi-upload
      python setup.py build_sphinx

#. Upload documentation:

   .. code-block:: bash

      python setup.py upload_docs

#. Publish application:

   .. code-block:: bash

      python setup.py sdist upload
