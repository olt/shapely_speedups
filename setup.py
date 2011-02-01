from setuptools import setup
from setuptools.extension import Extension

ext_modules = [Extension("shapely_speedups.speedups", ["shapely_speedups/speedups.c"], libraries=['geos_c'])]

setup_args = dict(
    name = 'shapely_speedups',
    long_description = open('README.md').read(),
    license = 'BSD',
    version = '0.1dev',
    ext_modules = ext_modules,
    )

setup(**setup_args)
