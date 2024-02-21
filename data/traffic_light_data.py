# import relevant libraries 
import requests            # for api
import pandas as pd        # for dataframe
import geojson             # for exploring json data 
import geopandas as gpd    # for geographical data
from pyproj import CRS
from owslib.wfs import WebFeatureService

url = "https://kartta.hel.fi/ws/geoserver/avoindata/wfs" # where API is ?

# what I want to get from the API
params = {
    "service": "WFS",
    "version": "2.0.0",
    "request": "GetFeature",             # request feature data 
    "typeName": "Liikennevalot_piste",   # get all data related to traffic lights
    "outputFormat": "application/json",  # set ouput to json 
}

# read in data from API and convert to JSON
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code} - {response.text}")

# create GeoDataFrame from geojson and set coordinate reference system
tf_light_data = gpd.GeoDataFrame.from_features(geojson.loads(response.content), 
                                                    crs="EPSG:3067")

# get column names 
print(tf_light_data.columns.values.tolist())
# translate column names to english 
tf_light_data.columns = ['geometry', 'id', 'number', 'type', 'intersection', 
                         'additional_information', 'data_owner', 'date_updated']

