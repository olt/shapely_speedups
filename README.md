Shapely Speedups
================

This Python package contains a replacement for two internal Shapely functions that are responsible for build new geometries.

The replacement functions are written in C (with cython) and are up-to 100-200x faster.

Installation
------------

Installation of this package should work with ``pip``, ``easy_install`` and ``python setup.py install``.

A C compiler, the Python libraries/header and GEOS libraries/header are required for installation.

How to use
----------

    import shapely_speedups
    shapely_speedups.patch_shapely()


Feedback
--------

Send feedback to olt@bogosoft.com or @oltonn