citydict = {}
# this creates an empty dictionary to which our data will be stored
f = open("CityPop.csv" , 'r')
# this opens the csv file and stores it in the value 'f'
lines = f.readlines()
# this reads all of the lines of the csv and stores them into the list 'lines'
headers = lines[0]
# the first row of the csv file was stored as the first entry of 'lines' and now is saved as headers so...
lines.remove(headers)
# they can be removed as we only want the exact values, otherwise we'd have a useless dictionary entry
count = 0
# i was having troulbe with the dictionary having way more enteries than 39, so i added the while
# and count loop to make sure it stopped after it read every line once
while count <= len(lines):
    '''the following code goes through every line in the list 'lines' and creates a new list 'b' that
    is split by the commas. from there it extracts all of the necessary values from that list and stores
    them as variables. from there, those variables besides the city name are compiled into a list per city (though altered to a dictionary for task 4).
    from there the dictionary will have a key added associated to a city which is followed by that city's
    list of population and location figures. once this is all done, the file is closed to free up memory'''
    for a in lines:
        b = a.split(',')
        city = str(b[4])
        lat = float(b[1])
        lon = float(b[2])
        yr1970 = float(b[5])
        yr1975 = float(b[6])
        yr1980 = float(b[7])
        yr1985 = float(b[8])
        yr1990 = float(b[9])
        yr1995 = float(b[10])
        yr2000 = float(b[11])
        yr2005 = float(b[12])
        yr2010 = float(b[13])
        citylist = [lat, lon, yr1970, yr1975, yr1980, yr1985, yr1990, yr1995, yr2000,yr2005, yr2010]
        citydict[city] = citylist
        count += 1
f.close()
