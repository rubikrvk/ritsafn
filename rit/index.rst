Velkomin
========

.. index::
   single: index hugtak í rót
   see: index hugtak í rót; hugtak í fjarmal fyrirtækja

1 Hér er asdf smá texti frá rit/index.rst. Og svo vil ég indexa þetta :index:`inline hugtak í rót`.

This is a test. Here is an equation:
:math:`X_{0:5} = (X_0, X_1, X_2, X_3, X_4)`.
Here is another:

.. math:: 6b_y = -6b_x

.. math:: e^{i\pi} + 1 = 0
   :label: euler

.. index:: single: Euler's identity

Smá annað test:

.. math:: e^{i\pi} + 2 = 0

Euler's identity, equation :eq:`euler`, was elected one of the most
beautiful mathematical formulas.

:math:`\underline{x}=[  x_{1}, ...,  x_{n}]^{T}`

.. math::
   9 = \sqrt{b_x^2+b_y^2}

.. math::
   \begin{aligned}
   9 &= \sqrt{b_x^2+b_y^2}\\
   &=\sqrt{b_x^2+(-6b_x)^2} \\
   &= \sqrt{b_x^2+36b_x^2} \\
   &=\sqrt{37b_x^2} \\
   &=b_x\sqrt{37} \\
   b_x&=\frac{9}{\sqrt{37}} \approx 1.480\\
   b_y&= -6b_x = \frac{-54}{\sqrt{37}} \approx -8.878
   \end{aligned}

2 Hér er asdf smá texti frá rit/index.rst.

.. figure:: https://source.unsplash.com/200x200/daily?cute+puppy
   :name: litilmynd1
   :height: 200
   :width: 200

   Þetta er caption fyrir litla mynd.

.. figure:: https://source.unsplash.com/200x200/daily?cute+puppy
   :name: stormynd1
   :height: 400
   :width: 400

   Þetta er caption fyrir stóra mynd.

Samanber :numref:`stormynd1`, þá er þetta mjög flott.

3 Hér er asdf smá texti frá rit/index.rst.

4 Hér er asdf smá texti frá rit/index.rst.

.. table:: Sample Table
   :name: prufutafla1

   +--------------------+---------------------+---------------------+
   | Header 1           | Header 2            | Header 3            |
   +====================+=====================+=====================+
   | Row 1, Column 1    | Row 1, Column 2     | Row 1, Column 3     |
   +--------------------+---------------------+---------------------+
   | Row 2, Column 1    | Row 2, Column 2     | Row 2, Column 3     |
   +--------------------+---------------------+---------------------+
   | Row 3, Column 1    | Row 3, Column 2     | Row 3, Column 3     |
   +--------------------+---------------------+---------------------+

Samanber :numref:`prufutafla1`, þá er þetta mjög flott tafla.

.. code-block:: python
   :caption: This is the code block caption
   :name: kodabalkur

   def hello_world():
       print("Hello, world!")

Samanber :numref:`kodabalkur`, þá er þetta mjög flottur kóði.

5 Hér er asdf smá texti frá rit/index.rst.

6 Hér er asdf smá texti frá rit/index.rst.

7 Hér er asdf smá texti frá rit/index.rst.

8 Hér er asdf smá texti frá rit/index.rst.

9 Hér er asdf smá texti frá rit/index.rst.

10 Hér er asdf smá texti frá rit/index.rst.

11 Hér er asdf smá texti frá rit/index.rst.

12 Hér er asdf smá texti frá rit/index.rst.

.. toctree::
   :maxdepth: 7

   fjarmal-einstaklinga/index
   fjarmal-fyrirtaekja/index
   eldhusvaskur/index

.. toctree::
   :numbered:
   :maxdepth: 7

   testing

.. toctree::
   :maxdepth: 7

   genindex