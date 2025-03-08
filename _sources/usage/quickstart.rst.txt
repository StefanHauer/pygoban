.. pygoban documentation master file, created by
   sphinx-quickstart on Tue Mar  4 22:42:51 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _Quickstart:

Quickstart
==========

Specifying the Board size
-------------------------

After :ref:`Installation`, import the GobanMaker class from the library.

.. code-block:: python
   :linenos:

   from pygoban import GobanMaker

To create your svg file, specify the size of the (square) grid as an integer. While he most common boards are 9 × 9, 13 × 13, or 19 × 19, you can use any number greater than 1.

.. code-block:: python
   :linenos:

   save_path = r"MyGoban.svg"
   g = GobanMaker(size=9)
   g.create_svg_file(save_path)

.. image:: ..\\..\\img\\goban_9x9.svg
  :width: 400
  :alt: Example of a 9 times 9 grid.

Instead of specifying the size as an integer, you can also use a tuple. So instead of size=9, you could also specify size=(9,9) and get the same output.

So while usually people play on square grids, if you want to create rectangular grids, you can do this too. Would anyone ever play on a board like this - most likely not, but if you ever do, let me know!

.. code-block:: python
   :linenos:

   g = GobanMaker(size=(8,5))
   g.create_svg_file(save_path)

.. image:: ..\\..\\img\\goban_8x5.svg
  :width: 400
  :alt: Example of a 8 times 5 grid.

In case you want to fine tune any of the created files with things that are beyond the capabilities of this library, you can always import the file into any vector graphics program and edit it there, for instanace with the free to use and open source software `Inkscape <https://inkscape.org/>`_.

Adjusting the Grid Spacing
--------------------------

Using the "line_spacing" parameter of the __init__ function, you can adjust the spacing between the grid lines. This way, you can tailor your board to the size of your Go stones.

.. code-block:: python
   :linenos:

   g = GobanMaker(
      size=(9,9),
      line_spacing=(22., 23.7)
   )
   g.create_svg_file(save_path)

Adding Annotation
-----------------

Most boards do not label the horizontal and vertical grids, but if you wish to, you can specify to annotate them either with Arabic numerals, Chinese numerals, or Latin letters using the parameters "x_annotation" and "y_annotation". You should also increase the space between the grid border and the border of the board so that stones on the sides will not overlap with the annotation.
Please note, that as a convention the letter "I" is skipped for the annotation, as "I" and "J" are similar and could lead to confusion.

.. code-block:: python

   g = GobanMaker(
      size=(9,9),
      x_annotation="latin_letters",
      y_annotation="roman_numerals",
      border_spacing=(28.,28.)
   )
   g.create_svg_file(save_path)

.. image:: ..\\..\\img\\goban_9x9_annotated.svg
  :width: 400
  :alt: Example of a 9 times 9 grid.

When you want to use Chinese numerals, make sure that the font face that you have selected can display Chinese characters. If your chosen font is unable to do so, you would see rectangles instead of Chinese character as the annotation. To show all fonts that are installed on your computer, you can use the following command:

.. code-block:: bash

   fc-list : family

Adjusting Star Point Markers
----------------------------

You can also adjust the star point markers of your board. For instance, you can change the diameter in mm with the "star_point_diameter" parameter.

.. code-block:: python

   g = GobanMaker(
      size=(9,9),
      star_point_pos='auto',
      star_point_diameter=10
   )
   g.create_svg_file(save_path)

.. image:: ..\\..\\img\\goban_9x9_spm10mm.svg
  :width: 400
  :alt: Example of a 9 times 9 grid.

When setting the parameter "star_point_pos" during initialization to an integer, it will put star points on the those lines.

.. code-block:: python

   g = GobanMaker(
      size=(9,9),
      star_point_diameter=6,
      star_point_pos=2
   )
   g.create_svg_file(save_path)

.. image:: ..\\..\\img\\goban_9x9_spm_at_2.svg
  :width: 400
  :alt: Example of a 9 times 9 grid with star point markers at the second grid lines.

You can also specify the star point marker positions manually, by defining a list of tuples denoting the positions on the grid.

.. code-block:: python

   star_point_pos = [
      (2,2), (3,4)
   ]
   g = GobanMaker(
      size=(9,9),
      star_point_diameter=6,
      star_point_pos=star_point_pos
   )
   g.create_svg_file(save_path)

.. image:: ..\\..\\img\\goban_9x9_two_spm.svg
  :width: 400
  :alt: Example of a 9 times 9 grid with only to star point markers.
