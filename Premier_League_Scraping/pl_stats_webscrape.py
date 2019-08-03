print ('Importing libraries...')

import requests
import geocoder
import json
import csv
from bs4 import BeautifulSoup, Comment
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

urls = ['/en/comps/9/26/stats/1992-1993-Premiership-Stats']

final_dict = {}
stats_dict = {}

main_page = 'https://fbref.com'

s = 0
while s < len(seasons):

    season = seasons[s]
    url = urls[s]

    print ('Compiling ' + season)

    pageTree = requests.get(main_page+url, headers=headers)
    soup = BeautifulSoup(pageTree.content,'html.parser')

    try:
        next_url = soup.find("a", class_="next")['href']
        urls.append(next_url)
    except:
        print ('no next season')

    stats_div = soup.find('div', id='all_stats_players')
    comments = stats_div.findAll(text=lambda text:isinstance(text, Comment))

    player_table_div = BeautifulSoup(comments[0],'html.parser')
    player_table = player_table_div.find('tbody')

    players = player_table.select('td[data-stat="player"]')
    #clubs = player_table.select('td[data-stat="squad"]')
    minutes = player_table.select('td[data-stat="minutes"]')
    nations = player_table.select('td[data-stat="nationality"]')

    i = 0
    while i < len(players):
            
        player = str(unidecode(players[i].text))
        natl_test = str(unidecode(nations[i].text)).split()

#if a player has a national team, clean up the text
        if len(natl_test) > 1:
            natl = natl_test[1]
#if a player has multiple national teams, take the first one
            if len(natl) > 3:
                natl = natl.split(',')[0]
#if no known national team, just blank it out
        else:
            natl = 'UKN'      

        try:
            link = str(players[i].find_all('a')[0]['href'])
            link_break = link.split('/')
            player_id = str(link_break[3])
        except:
            link = 'NONE'
            player_id = player+link
        
        try:
            min_played = int(str(minutes[i].text).replace(',', ''))
        except:
            min_played = 0
            
        #club = str(unidecode(clubs[i].text))

        if player_id in final_dict:
            if season in final_dict[player_id]:
                final_dict[player_id][season] += min_played

            else:
                final_dict[player_id][season] = min_played
            
        else:
            player_dict = {'name':player, 'link':link, season:min_played, 'nation':natl}
            final_dict[player_id] = []
            final_dict[player_id] = player_dict
            
        i+=1

    s+=1
        
print ("Player and season list built, adding and geocoding players' birth cities...")

count = 0
for player in final_dict:

    print(len(final_dict)-count)

    count += 1
        
    player_url = final_dict[player]['link']

#if the player has a URL, go to it
    if player_url != 'NONE':
            
        page = 'https://fbref.com'+player_url
        pageTree = requests.get(page, headers=headers)
        soup = BeautifulSoup(pageTree.content, 'html.parser')

#TRY to scrape for the city of birth in the HTML
        try:
            city = unidecode(soup.select('span[itemprop="birthPlace"]')[0].text.split('in ')[1].strip())

#TRY to use OSM to geocode it (this fails)
            try:
                g = geocoder.osm(city).json

#IF OSM returned no results
                if g == None:

#throw that city into the MapBox geocoder
                    g = geocoder.mapbox(city,key='NOPE').json
                    print ("mapbox")

#IF mapbox still couldn't find the city, we know the city at least!
                    if g == None:
                        final_dict[player]['city'] = city
                        final_dict[player]['lat'] = 0
                        final_dict[player]['lon'] = 0

#otherwise use what mapbox found  
                    else:
                        final_dict[player]['city'] = city
                        final_dict[player]['lat'] = g['lat']
                        final_dict[player]['lon'] = g['lng']

#use the information OSM found
                else:
                    final_dict[player]['city'] = city
                    final_dict[player]['lat'] = g['lat']
                    final_dict[player]['lon'] = g['lng']

#OSM geocoding straight up failed, we know there's a city though!
            except:
                final_dict[player]['city'] = city
                final_dict[player]['lat'] = 0
                final_dict[player]['lon'] = 0

#there is no city of birth and we know nothing
        except:
            final_dict[player]['city'] = 'UNKNOWN'
            final_dict[player]['lat'] = 0
            final_dict[player]['lon'] = 0

#if the player does NOT have a URL, we know nothing
    else:
        final_dict[player]['city'] = 'UNKNOWN'
        final_dict[player]['lat'] = 0
        final_dict[player]['lon'] = 0

    final_dict[player].pop('link')

print ('Summing minutes played per season...')
'''
for season in seasons:
        
    stats_dict[season] = 0

for player in final_dict:

    for stat_key in stats_dict:
                
        if stat_key in final_dict[player]:

            stats_dict[stat_key] += final_dict[player][stat_key]

print ('Calculating player impact on minutes...')

for player in final_dict:
        
    for stat_key in stats_dict:
                
        if stat_key in final_dict[player]:
                        
            pct_key = str(stat_key+'p')
            percent = float(final_dict[player][stat_key])/stats_dict[stat_key]
            final_dict[player][pct_key] = percent
'''
print ("Converting to JSON...")
       
with open ('pl_master.txt', 'w') as json_export:
    json.dump(final_dict, json_export, sort_keys=True)

print ("Converting to CSV...")

headers = ['name','nation','city','lat','lon','1992-1993','1993-1994','1994-1995','1995-1996','1996-1997','1997-1998','1998-1999','1999-2000','2000-2001','2001-2002','2002-2003','2003-2004','2004-2005','2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019']

with open('pl_master.csv','wb') as csvfile:
    w = csv.writer(csvfile)
    w.writerow(headers)
    
    for player in final_dict:
        row_data = []
        
        for i in headers:
            try:
                row_data.append(final_dict[player][i])
            except:
                row_data.append('')
            
        w.writerow(row_data)

print ("Total all-time PL players: " + str(len(final_dict)))
