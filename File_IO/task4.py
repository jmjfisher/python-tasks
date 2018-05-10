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
    them as variables. from there, those variables besides the city name are compiled into a DICTIONARY (only task 4) per city.
    from there the dictionary will have a key added associated to a city which is followed by that city's
    DICTIONARY of population and location figures. once this is all done, the file is closed to free up memory'''
    for a in lines:
        b = a.split(',')
        ide = str(b[0])
        city = str(b[4])
        yr1970 = float(b[5])
        yr1975 = float(b[6])
        yr1980 = float(b[7])
        yr1985 = float(b[8])
        yr1990 = float(b[9])
        yr1995 = float(b[10])
        yr2000 = float(b[11])
        yr2005 = float(b[12])
        yr2010 = float(b[13])
        citylist = {'1970': yr1970, '1975': yr1975, '1980': yr1980, '1985': yr1985,\
                    '1990': yr1990, '1995': yr1995, '2000': yr2000, '2005': yr2005, \
                    '2010': yr2010, 'capcity': city, 'ident': ide}
        citydict[city.lower()] = citylist
        count += 1
f.close()

'''
I would like to place all of my comments for the following code here
First we create a list of all acceptable years so that we can check if the user's
years entered are OK. we create a while True loop in order to make sure the entries
are acceptable and in the correct format and so the user can kill the program
when they like. the user will enter a tuple of two years (and if not, they will
be prompted to do correctly again). that tuple is split by the comma, and the two
years are extracted. from there if the first and second years entered are in the
year list, the program moves on to running the actual calculation. different from
the other tasks in this lab, i redefined the citydict so that each key has a
dictionary associated with it with cooresponding values so they may be called easier.
also, the headers are written into the newly created CityPopChange.csv file which has read
and write capabilities.
finally for every key in the citydict, the ID, NAME, and specific population fields
are extracted into variables (called by their keys). from there they are manipulated a bit to get the change
calculation. they are then stored as one long string separated by commas called 'values'
that is then written into the file via c.write which works since they're all a string.
once this has gone through every key, the file closes and the csv is ready.
'''

yearlist = ('1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010')
print "\nThis program will require you to enter two years between 1970-2010\nthat end in either '0' or '5' in order to compare population change."

def popchange():
    while True :
        poptuple = raw_input ("\nPlease enter the years between which you'd like to find the population\nchange in the format '1970,2010' (Return to exit):")
        if len(poptuple) < 1 : break

        if ',' in poptuple:
            pops = poptuple.split(',')
            pop1 = pops[0]
            pop2 = pops[1]
            if str(pop1) in yearlist:
                if str(pop2) in yearlist:
                    def export():
                        c = open('CityPopChg.csv' , 'w+t')
                        heads = 'id, city, population_change\n'
                        c.write(heads)
                        for x in citydict:
                            citycity = citydict[x]['capcity']
                            idnumber = citydict[x]['ident']
                            diff1 = citydict[x][str(pop1)]
                            diff2 = citydict[x][str(pop2)]
                            diftot = str(abs(float(diff1) - float(diff2)))
                            values = idnumber + ',' + citycity + ',' + diftot
                            c.write(values + '\n')                       
                        c.close()
                        print "\nYour file creation was a success. Please open CityPopChg.csv to see the change in population for each city."
                    export()
                    break
            
                else:
                    print "\nThe second year you entered was not found, please try again.\n"
            else:
                print "\nThe first year you entered was not found, please try again.\n"
        else: print "\nIt appears as if you entered your years incorrectly. Please try again in the correct format of 'Year1,Year2'\n"
popchange()
