print ("Running...")

import pandas as pd

centroids = {}
full = {}
start = {}
sub = {}
fed = {}

long_season = ['S1992-1993','S1993-1994','S1994-1995']

seasons = [
'S1992-1993',
'S1993-1994',
'S1994-1995',
'S1995-1996',
'S1996-1997',
'S1997-1998',
'S1998-1999',
'S1999-2000',
'S2000-2001',
'S2001-2002',
'S2002-2003',
'S2003-2004',
'S2004-2005',
'S2005-2006',
'S2006-2007',
'S2007-2008',
'S2008-2009',
'S2009-2010',
'S2010-2011',
'S2011-2012',
'S2012-2013',
'S2013-2014',
'S2014-2015',
'S2015-2016',
'S2016-2017',
'S2017-2018',
'S2018-2019']

df = pd.read_csv('pl_final_fed.csv',header=0)
tot_min = df.sum()

for season in seasons:

        centroids[season] = {}
        full[season] = {}
        start[season] = {}
        sub[season] = {}
        fed[season] = {}

        new_field = season+'P'
        rel_lat = season+'LAT'
        rel_lon = season+'LON'

        #create a new field in the data frame and set it equal to the percent of all minutes played that season
        df[new_field] = df[season]/tot_min[season]

        #multiply the percent of minutes by the lat/lon
        df[rel_lat] = df[new_field]*df['LAT']
        df[rel_lon] = df[new_field]*df['LON']

        #sum the lat and lon fields to arrive at the average lat and lon for said season
        c_lat = df[rel_lat].sum()
        c_lon = df[rel_lon].sum()

        # add the average lat and lon to the dictionary for exporting
        centroids[season]['LAT'] = c_lat
        centroids[season]['LON'] = c_lon

        if season in long_season:
                df_filt_sub = df[(df[season]>=420)]
                df_filt_start = df[(df[season]>=1890)]
        else:
                df_filt_sub = df[(df[season]>=380)]
                df_filt_start = df[(df[season]>=1710)]

        df_filt_full = df[(df[season]>=1)]
        
        df_nat_sub = df_filt_sub.groupby(['NATION']).count()
        data_dict_sub = df_nat_sub['CITY'].to_dict()
        sub[season] = data_dict_sub

        df_nat_start = df_filt_start.groupby(['NATION']).count()
        data_dict_start = df_nat_start['CITY'].to_dict()
        start[season] = data_dict_start

        df_nat_full = df_filt_full.groupby(['NATION']).count()
        data_dict_full = df_nat_full['CITY'].to_dict()
        full[season] = data_dict_full

        df_fed = df_filt_full.groupby(['CONFED']).count()
        data_dict_fed = df_fed['CITY'].to_dict()
        fed[season] = data_dict_fed


c_df = pd.DataFrame.from_dict(centroids,orient='index')
c_df.to_csv('season_centroids.csv')

sub_df = pd.DataFrame.from_dict(sub)
sub_tot_players = sub_df.sum()

start_df = pd.DataFrame.from_dict(start)
start_tot_players = start_df.sum()

full_df = pd.DataFrame.from_dict(full)
full_tot_players = full_df.sum()

fed_df = pd.DataFrame.from_dict(fed)
fed_tot_players = fed_df.sum()

for season in seasons:
        
        new_field = season+'P'
        sub_df[new_field] = 100*(sub_df[season]/sub_tot_players[season])
        start_df[new_field] = 100*(start_df[season]/start_tot_players[season])
        full_df[new_field] = 100*(full_df[season]/full_tot_players[season])
        fed_df[new_field] = 100*(fed_df[season]/fed_tot_players[season])

sub_df.to_csv('substitute_10_nations_count.csv')
start_df.to_csv('starter_45_nations_count.csv')
full_df.to_csv('full_1_nations_count.csv')
fed_df.to_csv('federations_count.csv')

print ('FINISHED')



