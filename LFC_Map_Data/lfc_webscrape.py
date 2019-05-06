print ('Importing libraries...')

import requests
import geocoder
import json
from bs4 import BeautifulSoup
from unidecode import unidecode

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

seasons = ['1992-1993',
'1993-1994',
'1994-1995',
'1995-1996',
'1996-1997',
'1997-1998',
'1998-1999',
'1999-2000',
'2000-2001',
'2001-2002',
'2002-2003',
'2003-2004',
'2004-2005',
'2005-2006',
'2006-2007',
'2007-2008',
'2008-2009',
'2009-2010',
'2010-2011',
'2011-2012',
'2012-2013',
'2013-2014',
'2014-2015',
'2015-2016',
'2016-2017',
'2017-2018',
'2018-2019']

final_dict = {}
stats_dict = {}

print ('Compiling list of players and season minutes...')

for season in seasons:

	page = 'https://fbref.com/en/squads/822bd0ba/'+season+'/Liverpool'
	pageTree = requests.get(page, headers=headers)
	soup = BeautifulSoup(pageTree.content, 'html.parser')
	pl_table = soup.find('tbody')
	players = pl_table.select('th')
	minutes = pl_table.select('td[data-stat="minutes"]')
	goals = pl_table.select('td[data-stat="goals"]')

	i = 0
	while i < len(players):
		
		player = str(unidecode(players[i].text))
		min_played = int(str(minutes[i].text).replace(',', ''))
		pl_goals = int(str(goals[i].text))
		link = str(players[i].find_all('a')[0]['href'])
		seasong = str(season+'g')

		if player in final_dict:
			final_dict[player][season] = min_played
			final_dict[player][seasong] = pl_goals
		
		else:
			player_dict = {'link':link,season:min_played,seasong:pl_goals}
			final_dict[player] = []
			final_dict[player] = player_dict
		
		i+=1
		
print ("Player and season list built, adding and geocoding players' birth cities...")

for player in final_dict:
        
        player_url = final_dict[player]['link']
        page = 'https://fbref.com'+player_url
        pageTree = requests.get(page, headers=headers)
        soup = BeautifulSoup(pageTree.content, 'html.parser')
        
        try:
                city = unidecode(soup.select('span[itemprop="birthPlace"]')[0].text.split('in ')[1].strip())
                g = geocoder.osm(city).json

                if g == None:
                        final_dict[player]['city'] = city
                        final_dict[player]['lat'] = 0
                        final_dict[player]['lon'] = 0

                else:
                        final_dict[player]['city'] = city
                        final_dict[player]['lat'] = g['lat']
                        final_dict[player]['lon'] = g['lng']

        except:
                final_dict[player]['city'] = 'UNKNOWN'
                final_dict[player]['lat'] = 0
                final_dict[player]['lon'] = 0

for player in final_dict:

        final_dict[player].pop('link')

print ('Summing minutes played and goals scored per season...')

for season in seasons:
        
        seasong = str(season+'g')
        stats_dict[season] = 0
        stats_dict[seasong] = 0

for player in final_dict:

        for stat_key in stats_dict:
                
                if stat_key in final_dict[player]:

                        stats_dict[stat_key] += final_dict[player][stat_key]

print ('Calculating player impact on goals and minutes...')

for player in final_dict:
        
        for stat_key in stats_dict:
                
                if stat_key in final_dict[player]:
                        
                        pct_key = str(stat_key+'p')
                        percent = float(final_dict[player][stat_key])/stats_dict[stat_key]
                        final_dict[player][pct_key] = percent

print ("Converting to JSON...")
       
with open ('liverpool.txt', 'w') as json_export:
        json.dump(final_dict, json_export, sort_keys=True)

print ("FINISHED!")
