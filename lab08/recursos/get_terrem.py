import json
import requests

#curl 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson' -o dia_terr2.json

response = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson')

terremotos_hora = response.json()
list_terremotos = terremotos_hora['features']

for t in list_terremotos:
    print(f"Lugar :{t['properties']['place']:<50} Magnitud:{t['properties']['mag']:>15}")