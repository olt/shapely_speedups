def patch_shapely():
    from shapely.geometry import linestring, polygon
    
    from shapely_speedups import speedups
    
    linestring.geos_linestring_from_py = speedups.geos_linestring_from_py
    polygon.geos_linearring_from_py = speedups.geos_linearring_from_py
    