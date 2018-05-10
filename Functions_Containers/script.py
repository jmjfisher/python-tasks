# this is the function for Task 2
def ddTOdms ():
    '''This is the function that converts DD to DMS, the notes in the first block may be used by all six parts of the function as
    each section is extremely similar besides the inital checks of positivity, followed by if the number is greater(less) than 100(-100)
    or less(greater) than 100(-100) and then if it's within -10 and 10 for slicing purposes'''
    #First there is a check for positivity of the raw_input
    if float(degree) >= 0:
        # then there is a check to see if it's over 100 as that means the slicing will be different
        if float(degree) >= 100:
        # degree like 100.123456
            # a pulls out the "degree" part from DD from which will be returned as the main D, slicing the raw_input to incorporate the first 3 figures
            a = int(degree[0:3])
            # this will then slice out the . and everything after it
            minout = float(degree[3:])
            # to figure out minutes, we multiply the decimal by 60, and then turning it into a string to use the split functionality
            brk = str(minout*60)
            # this breaks the minute integer from the remaining decimals which will be used for the seconds calculation
            brk = brk.split('.')
            # b is the minute, taken from the list brk
            b = int(brk[0])
            # secout is a string, so we can add a . to the front and then store that as a float so we can multiply it by 60
            secout = float("."+brk[1])
            # c is the second, we only need the integer part
            c = int(secout * 60)
            # "final" gathers the D, M, and S and stores them in a tuple
            final = (a, b, c)
            # finally, the text may be displayed which informs the user of their alteration, spit out as its tuple, final, is called
            print "\nThat degree value is in DD form.\n\nIts DMS form is", final

        elif 0 <= float(degree) < 10:
        # degree like 3.14159
            # a is the degree
            a = int(degree[0:1])
            minout = float(degree[1:])
            brk = str(minout*60)
            brk = brk.split('.')
            # b is the minute
            b = int(brk[0])
            secout = float("."+brk[1])
            # c is the second
            c = int(secout * 60)
            final = (a, b, c)
            print "\nThat degree value is in DD form.\n\nIts DMS form is", final

        else:
        # degree positive and like 45.123456
            # a is the degree
            a = int(degree[0:2])
            minout = float(degree[2:])
            brk = str(minout*60)
            brk = brk.split('.')
            # b is the minute
            b = int(brk[0])
            secout = float("."+brk[1])
            # c is the second
            c = int(secout * 60)
            final = (a, b, c)
            print "\nThat degree value is in DD form.\n\nIts DMS form is", final
            
    else:
    #Negative degree was given
        if float(degree) <= -100:
        #degree like -100.12345
            a = int(degree[0:4])
            minout = float(degree[4:])
            brk = str(minout*60)
            brk = brk.split('.')
            # b is the minute
            b = int(brk[0])
            secout = float("."+brk[1])
            # c is the second
            c = int(secout * 60)
            final = (a, b, c)
            print "\nThat degree value is in DD form.\n\nIts DMS form is", final

        elif -10 < float(degree) < 0:
        #degree like -1.1234
            a = int(degree[0:2])
            minout = float(degree[2:])
            brk = str(minout*60)
            brk = brk.split('.')
            # b is the minute
            b = int(brk[0])
            secout = float("."+brk[1])
            # c is the second
            c = int(secout * 60)
            final = (a, b, c)
            print "\nThat degree value is in DD form.\n\nIts DMS form is", final

        else:
        # degree negative and like -45.1234
            a = int(degree[0:3])
            minout = float(degree[3:])
            brk = str(minout*60)
            brk = brk.split('.')
            # b is the minute
            b = int(brk[0])
            secout = float("."+brk[1])
            # c is the second
            c = int(secout * 60)
            final = (a, b, c)
            print "\nThat degree value is in DD form.\n\nIts DMS form is", final

# this is the function for Task 1
def dmsTOdd ():
    '''This function converts DMS to DD and is called when there is a comma in the degree input
    at this point, degree has already been split at the commas and turn into a tuple'''
    # checks for negativity
    if int(degree[0]) < 0:
        # this takes all parts of the degree tuple and alters them a bit, storing them as floats and dividing them accordingly
        test = (float(degree[0]), float(degree[1])/60, float(degree[2])/3600)
        # this extracts all parts of the test and subtracts them from eachother as this is the negative part of the function
        finaldd = test[0]-test[1]-test[2]
        # finally, the text is shown with the computed DD format
        print "\nThat degree value is in DMS form.\n\nIts DD form is", finaldd
    else:
    # runs when the degree entered was positive
        # similar to the negative side, this creates a new tuple (test) which has divided out parts of the DMS to get them read for DD form
        test = (float(degree[0]), float(degree[1])/60, float(degree[2])/3600)
        # again, similar to the negative part, but this time all parts of the test tuple are added together to get it in DD format
        # and ready to be displayed by the script
        finaldd = test[0]+test[1]+test[2]
        print "\nThat degree value is in DMS form.\n\nIts DD form is", finaldd

# this prompts the user to enter their coordinates. per our intructions, we can assume they will be entered correctly        
degree = raw_input("Please enter a latitude or longitude value in DMS (D,M,S) or DD format: ")
print "\nYou entered:", degree
# the user will use commmas to seperate DMS, so this says that if a comma exists, we know it's in DMS and can call the DMS to DD function
if ',' in degree:
    degree = tuple(degree.split(','))
    dmsTOdd ()
# if a comma doesn't exist, then we know it's in DD format so the DD to DMS function is called
else:
    ddTOdms ()
