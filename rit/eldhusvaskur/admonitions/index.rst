Admonitions
===========

.. toctree::
   :caption: Admonitions kaflar
   :maxdepth: 6

   admonitions-1/index
   admonitions-2/index
   admonitions-3/index

Hér er smá texti fyrir ofan yfirlit fyrirsafna.

.. contents:: Yfirlit fyrirsagna í Admonitions
    :depth: 4
    :local:
    :backlinks: none

Setjum :math:`6b_y=-6b_x` inn og fáum:

.. math:: 6b_y = -6b_x

.. math:: e^{i\pi} + 1 = 0
   :label: euler7

.. index:: single: Euler's identity

Smá annað test:

.. math:: e^{i\pi} + 2 = 0
   :label: euler8

Euler's **identity**, equation :eq:`euler8`, was elected one of the most
beautiful mathematical formulas.

.. figure:: https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg
   :name: litilmynd4
   :height: 200
   :width: 200

   Þetta er caption fyrir litla mynd.

.. figure:: https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg
   :name: stormynd4
   :height: 400
   :width: 400

   Þetta er caption fyrir stóra mynd.

Samanber :numref:`stormynd4`, þá er þetta mjög flott.

.. table:: Sample Table
   :name: prufutafla4

   +--------------------+---------------------+---------------------+
   | Header 1           | Header 2            | Header 3            |
   +====================+=====================+=====================+
   | Row 1, Column 1    | Row 1, Column 2     | Row 1, Column 3     |
   +--------------------+---------------------+---------------------+
   | Row 2, Column 1    | Row 2, Column 2     | Row 2, Column 3     |
   +--------------------+---------------------+---------------------+
   | Row 3, Column 1    | Row 3, Column 2     | Row 3, Column 3     |
   +--------------------+---------------------+---------------------+

Samanber :numref:`prufutafla4`, þá er þetta mjög flott tafla.

Text below header one

.. code-block:: python
   :caption: This is the code block caption
   :name: kodabalkur1

   def hello_world():
       print("Hello, world!")

Samanber :numref:`kodabalkur1`, þá er þetta mjög flottur kóði.


Header two
----------

.. figure:: https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg
   :name: litilmynd5
   :height: 200
   :width: 200

   Þetta er caption fyrir litla mynd.

.. figure:: https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg
   :name: stormynd5
   :height: 400
   :width: 400

   Þetta er caption fyrir stóra mynd.

Samanber :numref:`stormynd5`, þá er þetta mjög flott.

.. table:: Sample Table
   :name: prufutafla5

   +--------------------+---------------------+---------------------+
   | Header 1           | Header 2            | Header 3            |
   +====================+=====================+=====================+
   | Row 1, Column 1    | Row 1, Column 2     | Row 1, Column 3     |
   +--------------------+---------------------+---------------------+
   | Row 2, Column 1    | Row 2, Column 2     | Row 2, Column 3     |
   +--------------------+---------------------+---------------------+
   | Row 3, Column 1    | Row 3, Column 2     | Row 3, Column 3     |
   +--------------------+---------------------+---------------------+

Samanber :numref:`prufutafla5`, þá er þetta mjög flott tafla.

.. _kodanafn:

.. code-block:: python
   :caption: This is the code block caption
   :name: kodabalkur2

   def hello_world():
       print("Hello, world!")

Samanber :numref:`kodabalkur2`, þá er þetta mjög flottur kóði.

Og aftur, samanber :ref:`þennan geggjaða kóða <kodanafn>`, þá er þetta mjög flottur kóði.

Header three
^^^^^^^^^^^^

Text below header three

Header four
~~~~~~~~~~~

Text below header four

Header five
"""""""""""

Text below header five

Header six
++++++++++

Text below header six

