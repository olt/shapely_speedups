from shapely.geometry import linestring, polygon, multilinestring
from shapely import coords
from shapely_speedups import speedups

_orig = {}

def patch_shapely():
    if _orig:
        return
    
    _orig['CoordinateSequence.ctypes'] = coords.CoordinateSequence.ctypes
    coords.CoordinateSequence.ctypes = property(speedups.coordseq_ctypes)
    
    _orig['geos_linestring_from_py'] = linestring.geos_linestring_from_py
    linestring.geos_linestring_from_py = speedups.geos_linestring_from_py
    
    _orig['geos_linestring_from_py'] = multilinestring.geos_linestring_from_py
    multilinestring.geos_linestring_from_py = speedups.geos_linestring_from_py

    _orig['geos_linearring_from_py']  = polygon.geos_linearring_from_py
    polygon.geos_linearring_from_py = speedups.geos_linearring_from_py

def unpatch_shapely():
    if not _orig:
        return

    coords.CoordinateSequence.ctypes = _orig['CoordinateSequence.ctypes']
    linestring.geos_linestring_from_py = _orig['geos_linestring_from_py']
    multilinestring.geos_linestring_from_py = _orig['geos_linestring_from_py']
    polygon.geos_linearring_from_py = _orig['geos_linearring_from_py']
    _orig.clear()