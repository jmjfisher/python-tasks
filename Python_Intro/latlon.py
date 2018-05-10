# this must be a function so it may be re-run if something fails
def latlong () :
    # prompts the user for their lat and long values and checks to see if
    # they fit the type float, if not, it will jump out of the try sequence
    # and the except clause will run which will rerun the function from the
    # top which begins with the prompts
    try:
        lat = float(raw_input ('Please enter your location\'s latitude: '))
        lon = float(raw_input ('Please enter your location\'s longitude: '))

        # here it checks to see what the lat is and prints out the appropriate
        # location if the parameter is met
        if lat == 0: print 'That location is on the equator.'
        elif 0 < lat <= 90: print 'That location is north of the equator.'
        elif -90 <= lat < 0: print 'That location is south of the equator.'
        else: print 'That location does not have a valid latitude!'

        # similar to the lat check, this checks the user's long value against
        # various degrees on earth
        if lon == 0: print 'That location is on the prime meridian.'
        elif 0 < lon <= 180: print 'That location is east of the prime meridian.'
        elif -180 <= lon < 0: print 'That location is west of the prime meridian.'
        else: print 'That location does not have a valid longitude!'
        
    except:
        # this tells the user they didn't enter numbers and restarts the script
        print
        print 'Please enter numbers for your values.'
        print
        latlong ()

# after the function has been defined, it must be called
latlong ()
