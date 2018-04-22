.. xhale documentation master file, created by
   sphinx-quickstart on Sun Apr 22 20:02:10 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to xhale's documentation!
=================================

xhale transforms an inventory file given by sphinx into a doxygen tag file. This package is mainly used for `xeus-cling <https://github.com/QuantStack/xeus-cling>`_ in order to be able to get the documentation of a C++ package in a jupyter notebook.

To create your tag file, you just have to use the script **xhale** and give the following arguments

- the package name which will be the name of the tag file
- the url where to find the inventory file

Here is an example

.. code:: bash

    xhale -p xtensor --url https://xtensor.readthedocs.io/en/latest/

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api/xhale


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
