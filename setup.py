from setuptools import setup, find_packages
from setuptools.extension import Extension

ext_modules = [Extension("shapely_speedups.speedups", ["shapely_speedups/speedups.c"], libraries=['geos_c'])]

setup_args = dict(
    name = 'shapely_speedups',
    long_description = open('README.md').read(),
    license = 'BSD',
    packages = find_packages(),
    version = '0.2',
    ext_modules = ext_modules,
    )

setup(**setup_args)
