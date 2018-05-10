def dist ():
    # first we will need to import the math tools
    import math
    # then the script prompts the user for their 4 lat/long coordinates with respect
    # to their two points. if their coordinates are anything that's not an
    # integer or float, it will fall to the except clause and re-run the script
    # from the top, otherwise they'll be stored in their proper variables
    try:
        lata = float(raw_input ('Please enter your first location\'s latitude: '))
        lona = float(raw_input ('Please enter your first location\'s longitude: '))
        latb = float(raw_input ('Please enter your second location\'s latitude: '))
        lonb = float(raw_input ('Please enter your second location\'s longitude: '))

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
        print 'The distance between your first and second location is', distance,'km.'
        print
        
    except:
        print
        print 'Please enter numbers for your values.'
        print
        dist ()
dist ()
