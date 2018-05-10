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
The following comments section is in regards to all of the citiesdist function, minus the dist function.
There is a while loop created so that the user may exit by pressing enter and to make sure with various
'if' statements that the cities they entered are spelled correctly, exist all together, or in the correct
format. The two cities entered are then split by the comma and saved as two variables which are both checked
for existance in the citydict dictionary. If they don't the user is prompted again, otherwise the distance
function may begin. the distance function is slightly altered so that it looks in the dictionary to find the correct
lat/long coordinates by referencing those cells in each key's associated list. from there it runs just as it did
in the previous lab.
'''

def citiesdist():
    while True :
        citytuple = raw_input ("Please enter the cities between which you'd like to find the distance in the format 'City1,City2' (Return to exit):")
        if len(citytuple) < 1 : break

        if ',' in citytuple:
            cities = citytuple.split(',')
            city1 = cities[0]
            city2 = cities[1]
            if str(city1.lower()) in citydict:
                if str(city2.lower()) in citydict:
                    def dist ():
                        # first we will need to import the math tools
                        import math

                        lata = citydict[city1.lower()][0]
                        lona = citydict[city1.lower()][1]
                        latb = citydict[city2.lower()][0]
                        lonb = citydict[city2.lower()][1]

                        # this is where those decimal degrees are converted into radians by using
                        # the math module that was imported at the beginning
                        lata = math.radians(lata)
                        lona = math.radians(lona)
                        latb = math.radians(latb)
                        lonb = math.radians(lonb)

                        # here the actual calculation occurs, plugging in the now radian variables
                        # into various trig functions usable with the imported math module
                        # the output angle is multiplied by the radius of the earth, rounded
                        # and then stored as an integer to be called later
                        angle = math.acos( (math.sin(lata)*math.sin(latb)) + (math.cos(lata)*math.cos(latb)*math.cos((lona-lonb)) ) )
                        distance = int(round(angle*6300))

                        # finally, the distance is written out in a format the users can easily understand
                        print
                        print 'The distance between',citydict[city1.lower()][11],'and',citydict[city2.lower()][11],'is', distance,'km.'
                        print

                    dist ()
                    break
            
                else:
                    print "\nThe second city you entered was not found, please try again.\n"            
            else:
                print "\nThe first city you entered was not found, please try again.\n"
        else: print "\nIt appears as if you entered your cities incorrectly. Please try again in the correct format of 'City1,City2'\n"
citiesdist()
