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
    them as variables. from there, those variables besides the city name are compiled into a list per city.
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
        citylist = [lat, lon, yr1970, yr1975, yr1980, yr1985, yr1990, yr1995, yr2000, yr2005, yr2010, city]
        citydict[city.lower()] = citylist
        count += 1
f.close()

'''
This is the comment section for the entire popyear function.
A while loop is created in order for the user to quit well or to make sure the user's
entry is valid/exists. First, the user is asked for a city and then that is checked properly.
If it exists in the dictionary, then it's asked for a year which is also checked for existance.
If the city/year combo are fine, then there are many if/elif statments set up to check for each
possible year entry between 1970-2010 (probably not the quickest way, but what I did).
Once the correct if/elif statement is found, the program will print out a string which also calls
that city's name written in the proper form (the user may enter the city regardless of case) and
references that city's key to find the cooresponding population value in millions.
'''

def popyear():
    while True :
        city = raw_input ("Please enter the name of the city for which you want population data (Return to exit):")
        if len(city) < 1 : break

        if str(city.lower()) in citydict:
            def yearcheck():
                while True :
                    year = raw_input ("\nPlease enter the year for which you want popuation data in the format 'yr1970' (Return to exit):")
                    if len(year) < 1 : break

                    if year == 'yr1970':
                        print "\nThe population in", citydict[city.lower()][11], "in 1970 was", citydict[city.lower()][2],"million."
                        break
                    elif year == 'yr1975':
                        print "\nThe population in", citydict[city.lower()][11], "in 1975 was", citydict[city.lower()][3],"million."
                        break
                    elif year == 'yr1980':
                        print "\nThe population in", citydict[city.lower()][11], "in 1980 was", citydict[city.lower()][4],"million."
                        break
                    elif year == 'yr1985':
                        print "\nThe population in", citydict[city.lower()][11], "in 1985 was", citydict[city.lower()][5],"million."
                        break
                    elif year == 'yr1990':
                        print "\nThe population in", citydict[city.lower()][11], "in 1990 was", citydict[city.lower()][6],"million."
                        break
                    elif year == 'yr1995':
                        print "\nThe population in", citydict[city.lower()][11], "in 1995 was", citydict[city.lower()][7],"million."
                        break
                    elif year == 'yr2000':
                        print "\nThe population in", citydict[city.lower()][11], "in 2000 was", citydict[city.lower()][8],"million."
                        break
                    elif year == 'yr2005':
                        print "\nThe population in", citydict[city.lower()][11], "in 2005 was", citydict[city.lower()][9],"million."
                        break
                    elif year == 'yr2010':
                        print "\nThe population in", citydict[city.lower()][11], "in 2010 was", citydict[city.lower()][10],"million."
                        break
                    else:
                        print "\nThat year was not found, please try again with a year between 1970-2010 ending in '0' or '5'."
                        
            yearcheck() 
            break
        
        else:
            print "\nThat city was not found, please try again.\n"

popyear()
