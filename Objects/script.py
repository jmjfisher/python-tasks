'''first we create the class City and create the __init__ that will set all of the attributes from the csv for each class
as so. after that, we create the empty list Cities which we will us to store and call the instances of City.'''

class City():
    def __init__(self,name='',label='',lat=0,lon=0,yr1970=0,yr1975=0,yr1980=0,yr1985=0,yr1990=0,yr1995=0,yr2000=0,yr2005=0,yr2010=0):
        self.name = name
        self.label = label
        self.lat = lat
        self.long = lon
        self.yr1970 = yr1970
        self.yr1975 = yr1975
        self.yr1980 = yr1980
        self.yr1985 = yr1985
        self.yr1990 = yr1990
        self.yr1995 = yr1995
        self.yr2000 = yr2000
        self.yr2005 = yr2005
        self.yr2010 = yr2010

    def printDistance(self,othercity):
        import math
        
        lata = self.lat
        lona = self.long
        latb = othercity.lat
        lonb = othercity.long
        
        lata = math.radians(lata)
        lona = math.radians(lona)
        latb = math.radians(latb)
        lonb = math.radians(lonb)
        
        angle = math.acos( (math.sin(lata)*math.sin(latb)) + (math.cos(lata)*math.cos(latb)*math.cos((lona-lonb)) ) )
        distance = int(round(angle*6300))

        print '\nThe distance between',self.label,'and',othercity.label,'is', distance,'km.'

    def printPopChange(self,year1,year2):
        yr1 = float(getattr(self, year1))
        yr2 = float(getattr(self, year2))
        change = abs(yr1-yr2)
        if yr1 < yr2:
            print "\nThe population change from",year1,"to",year2,"in",self.label,"was",change,"million."
        else:
            print "\nThe population change from",year2,"to",year1,"in",self.label,"was",change,"million."

'''THE FOLLOWING COMMENTS ARE FOR THE printDistance and printPopChange METHODS!
for the printDistance meathod, I repurposed a former lab's script so you have seen
how that works multiple times, but basically it extracts the lat/long values from the class
and uses those within the math module to calculate various values which are ultimately turned
into a distance value in km that is printed for the user's reference.
the printPopChange method is completely new and unique so I will go into that in a bit more
detail. the year arguments of the method do not exactly "extract" the values from the class that
we need, so the 'getattr' module which is built into all classes must be utilized in order extract
those years' data. this works by calling the 'self' followed by the argument of the year1 or year2
which is then 'looked-up' based on the class' __init__ method. from there we make sure it's a float
and then is stored in yr1 or yr2 to be manipulated later. those values are then subtracted and we take
the absolute value of that difference. from there we have the change stored in a value so everything
can be printed out nicely by calling the class instance's other __init__ values. the last little bit checks
to make sure that the smaller of the populations is printed first so in english it reads better.'''

Cities = []

'''in the following we try to find the correct file to open. if the file in the script doesn't exist
it will fall to the except statement and end peacefully. but since the file exists, it will then
extrac the lines, delete the headers (first row) and then for each remaining row (this is all in
the list 'lines' at this point) it will create an instance 'city' with the cooresponding values to
that city defined by the __init__ of the City class. once that is complete, that instance and its
'values' will be appended to the Cities list. this list is necessary for those instances to be called
later, as in task 2.'''

try:
    f = open("CityPop.csv" , 'r')
    lines = f.readlines()
    headers = lines[0]
    lines.remove(headers)
    count = 0
    while count < len(lines):
        for row in lines:
            b = row.split(',')
            city = City(name=str(b[3]),label=str(b[4]),lat=float(b[1]),lon=float(b[2]),yr1970=float(b[5]),yr1975=float(b[6]),yr1980=float(b[7]),\
                             yr1985=float(b[8]),yr1990=float(b[9]),yr1995=float(b[10]),yr2000=float(b[11]),yr2005=float(b[12]),yr2010=float(b[13]))
            Cities.append(city)
            count += 1
    f.close()
except:
    print "That file does not exist."

'''the last part of task 1 has us print out all of the attributes of the cities and we do this by
looping through the list where the instances are stored and then printing their attributes thanks
to them being stored properly by the __init__ method'''

for city in Cities:
    print city.name,city.label,city.lat,city.long,city.yr1970,city.yr1975,city.yr1980,city.yr1985,\
    city.yr1990,city.yr1995,city.yr2000,city.yr2005,city.yr2010

Cities[4].printDistance(Cities[6])
Cities[22].printDistance(Cities[0])
Cities[1].printPopChange('yr1970','yr1980')
Cities[21].printPopChange('yr2010','yr1975')

'''the above 4 lines are simply to prove that the methods of City class work properly.
thanks for all your help, Zeb!'''
