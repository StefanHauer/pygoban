.. pygoban documentation master file, created by
   sphinx-quickstart on Wed Mar  5 08:02:41 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pygoban's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage/installation
   usage/quickstart
   usage/pygoban_class

What is Go?
===========

Go is an ancient Chinese board game about capturing territory by placing stones on a grid. If you are new to the game of Go you might want to learn `about the basic rules first <https://en.wikipedia.org/wiki/Rules_of_Go>`_ and afterward trying out to `play online <https://online-go.com/>`_.

What is Pygoban?
================

Pygoban is a small Python library to create vector graphics of customized Go boards using `Pycairo <https://pycairo.readthedocs.io/en/latest/>`_. The created svg files can be used for printing a board out on paper, or to etch it into wood using a laser cutter. This way you can very quickly create cheap Go boards to play everywhere!

Why does this library exist?
============================

I moved Switzerland, had my Go stones with me but forgot to bring my board. So I decided to make my own board from plywood with a laser cutter. While templates for Go boards of traditional sizes exist readily available on the internet, I decided I wanted a bit more freedom and customizability. After all, the nice thing about traditions is that you can start your own at any time.

How do I use Pygoban?
=====================

If you want to use Pygoban, take a look at the pages for :ref:`Installation` and :ref:`Quickstart`. The GobanMaker class is in even more detail described on the :ref:`API` page. Should you still have some problems, questions, or suggestions how this could be improved, write me a mail to stefan.f.hauer@gmx.at or create an issue on `my GitHub repository <https://github.com/StefanHauer/pygoban/issues>`_. Also, send me pictures of the physical boards that you create!
