# import relevant libraries 
import requests            # for api
import pandas as pd        # for dataframe
import json                # for exploring json data 


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

# explore JSON data - what is going on there 
len(data) # length of the data is 7 

# print the entire list
print(json.dumps(data, indent=2))

# print each element in the list
for i, row in enumerate(data):
    print(f"\nRow {i + 1}:")
    print(json.dumps(row, indent=2))