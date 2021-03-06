JDFT: A differantiable Jax implementation for density functional theory
=======================================================================


This is a `JAX <https://github.com/google/jax/>`_-based package for differantiable density functional theory and quantum chemistry.


.. warning::

   This project is **under** development.


.. important::
   The guidance for development:

   - **Involving more functional programming.**  We try to use pure functions and reduce side affects as much as possible. The only class in :guilabel:`JDFT` is ``jdft.molecule``. Functional programming is also one the most important characteristics of :guilabel:`Jax`
   - **Align** :guilabel:`JDFT` **with** :guilabel:`PySCF`. The functions, attributes and methods are optimized to align with those in :guilabel:`PySCF`.


.. _installation:

Installation
------------

To use :guilabel:`JDFT`, first install it using pip:

.. code-block:: console

   $ pip install jdft


Contents
--------

.. toctree::
   :maxdepth: 2

   math/index
   jdft/index
   pyscf/index
   examples/index


