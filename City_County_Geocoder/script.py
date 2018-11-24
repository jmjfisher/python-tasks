#script to obtain county of city, state using ArcGIS geocoder and Census API

import geocoder
import requests

cities = ['Los Angeles, CA', 'Madison, Wisconsin']
coords = []

for i in cities:
    g = geocoder.arcgis(i)
    lat = str(g.lat)
    lng = str(g.lng)
    new_coord = [lat, lng]
    print new_coord
    coords.append(new_coord)

for i in coords:
    y = i[0]
    x = i[1]
    url = 'https://geocoding.geo.census.gov/geocoder/geographies/coordinates?x='+x+'&y='+y+'&benchmark=4&vintage=4&format=json'
    try:
        r = requests.get(url)
        print r.json()['result']['geographies']['Counties'][0]['BASENAME']
    except:
        print 'NO ADDRESS'
