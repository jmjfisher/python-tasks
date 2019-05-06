print ("Running...")

import pandas as pd
import json

centroids = {}

seasons = ['X19921993',
'X19931994',
'X19941995',
'X19951996',
'X19961997',
'X19971998',
'X19981999',
'X19992000',
'X20002001',
'X20012002',
'X20022003',
'X20032004',
'X20042005',
'X20052006',
'X20062007',
'X20072008',
'X20082009',
'X20092010',
'X20102011',
'X20112012',
'X20122013',
'X20132014',
'X20142015',
'X20152016',
'X20162017',
'X20172018',
'X20182019']

for season in seasons:
        
        seasong = str(season+'g')
        centroids[season] = {'lat':0,'lon':0}
        centroids[seasong] = {'lat':0,'lon':0}

data = pd.read_csv('result.csv',header=0)

for season in seasons:

        seasong = str(season+'g')
        seasonp = str(season+'p')
        seasongp = str(season+'gp')

        data['PLAT'] = data.XLAT*data[seasonp]
        data['PLON'] = data.XLON*data[seasonp]
        data['GPLAT'] = data.XLAT*data[seasongp]
        data['GPLON'] = data.XLON*data[seasongp]

        plat = data.PLAT.sum()
        plon = data.PLON.sum()
        gplat = data.GPLAT.sum()
        gplon = data.GPLON.sum()

        centroids[season]['lat'] = plat
        centroids[season]['lon'] = plon
        centroids[seasong]['lat'] = gplat
        centroids[seasong]['lon'] = gplon

print ("Converting to JSON...")
       
with open ('centroids.txt', 'w') as json_export:
        json.dump(centroids, json_export, sort_keys=True)

print ("FINISHED!")
