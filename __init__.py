"""
PYGOBAN
=======

The Python library pygoban is intended for creating scalable vector graphics files of Go boards.
You can then use these files to either print them out on paper, or better yet, etch and cut them
on the material of your choice using a laser cutter.

With this library you can easily create your own boards with
  * custom grids, allowing for any number of grid lines, and even rectangular grids,
  * custom grid spacing tailored to your stone sizes,
  * custom star point marker positions,
  * and different annotation styles for the grid lines.


How to use the documentation
----------------------------
Documentation is available in three forms:
  1. Docstrings as part of the code
  2. Sphinx documentation created from the docstrings
  3. Basic examples of use are also documented in the README file.
"""

__version__ = "0.1.0"

from .pygoban import GobanMaker

__all__ = [
    "__version__",
    "GobanMaker"
]
