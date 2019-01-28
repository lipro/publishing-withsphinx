.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

test for sphinxcontrib.programoutput
====================================

Include the output of command in the documentation:

.. program-output:: cat ${TEST_FIXTURES_ROOTS}/test-contrib-ansi/index.rst
   :shell:

If used with two comma-separated line numbers, all lines in between the
specified lines are omitted. Again, a negative number counts from the last
line backwards:

.. program-output:: python --help
   :ellipsis: 2,-12

Same, but with enabled prompt option:

.. command-output:: cat ${TEST_FIXTURES_ROOTS}/test-contrib-ansi/index.rst
   :shell:

If used with a single number, all lines after the specified line are omitted:

.. command-output:: python --help
   :ellipsis: 2

Normally the command is splitted according to the POSIX shell syntax (see
:py:mod:`shlex`), and executed directly.  Thus special shell features like
expansion of environment variables will not work:

.. command-output:: echo "$USER"
   :shell:
