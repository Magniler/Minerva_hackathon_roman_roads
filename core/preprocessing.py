import geopandas as gpd
from pathlib import Path

# Load a shape file of world lakes as a GeoDataFrame:
path = Path('C:\\Users\\mlind\\github\\Minerva_hackathon\\data\\split segments\\road_merge_split_08112023.shp')
world_lakes = gpd.read_file(path)
world_lakes.head(3)