from shapely.geometry import linestring, polygon
from shapely_speedups import speedups

_orig_geos_linestring_from_py = None
_orig_geos_linearring_from_py = None

def patch_shapely():
    global _orig_geos_linestring_from_py
    global _orig_geos_linearring_from_py
    
    if linestring.geos_linestring_from_py != speedups.geos_linestring_from_py:
        _orig_geos_linestring_from_py = linestring.geos_linestring_from_py
        linestring.geos_linestring_from_py = speedups.geos_linestring_from_py
    if polygon.geos_linearring_from_py != speedups.geos_linearring_from_py:
        _orig_geos_linearring_from_py = polygon.geos_linearring_from_py
        polygon.geos_linearring_from_py = speedups.geos_linearring_from_py

def unpatch_shapely():
    global _orig_geos_linestring_from_py
    global _orig_geos_linearring_from_py
    
    if _orig_geos_linestring_from_py:
        linestring.geos_linestring_from_py = _orig_geos_linestring_from_py
        _orig_geos_linestring_from_py = None
    if _orig_geos_linearring_from_py:
        polygon.geos_linearring_from_py = _orig_geos_linearring_from_py
        _orig_geos_linearring_from_py = None
    