.. -*- coding: utf-8 -*-
.. -*- restructuredtext -*-

Mathematical notation
=====================

Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`.

Multiple equations, separated by a blank line:

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2

Multiple aligned lines in an equation:

.. math::

   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2

Prevents any wrapping of the given math in a math environment:

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}

Cross-referencing equations via their label:

.. math:: e^{i\pi} + 1 = 0
   :label: euler

Euler's identity, equation :eq:`euler`, was elected one of the most
beautiful mathematical formulas.
