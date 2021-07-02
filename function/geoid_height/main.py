from pathlib import Path

import pyproj


def get(lng=135.630, lat=34.290):
    pyproj.datadir.append_data_dir(Path(__file__).parent)
    transformer = pyproj.Transformer.from_crs(6667, 6695, always_xy=True)
    result = transformer.transform(lng, lat, 0)
    geoid_height = -result[2]
    return geoid_height
