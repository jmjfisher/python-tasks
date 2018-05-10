# This program calculates the area of a triangle or a trapezoid but kicks out of the program if the user keeps entering non-number values.

# Once this script is executed it will display the first string of text followed by a blank line for spacing
print "This program finds the area of a triangle or trapezoid."
print 	

# first this will ask the user to enter either triangle or trapezoid so it may use the correct area formula
def question ():
    import sys
    shape = str(raw_input("Please enter if your shape is a triangle or trapezoid: "))
    print
# if user typed triangle, this will prompt the user to enter a value for both height and base of the triangle for which they want the area
# which will be stored in two variables appropriately named height and base, however, there is a counter set up in a while loop which
# asks the user to enter their value again if it cannot be stored as a number (float). if the user enters two figures, they're stored
# as the appropriate variables and then entered into the area equation and then it's printed properly. the "except" statement is only
# called when they didn't enter numbers and triggers the while loop to add a value to loopCount.
    if shape == 'triangle':
        loopCount = 0
        while loopCount < 6:
            loopCount += 1
            if loopCount > 4: sys.exit()
            else:
                try:
                    height = float(raw_input("Please enter the height of the triangle: "))
                    base = float(input("Please enter the base length of the triangle: "))
                    area = 0.5 * height * base
                    print
                    print "The area of a triangle with height", height, "and base", base, "is", area,"."
                    break
                except:
                    print "Sorry, you did not enter a number for your value."
                    
# if the user entered trapezoid, it will flow directly to this portion of the function which asks for the three necessary
# measurements of the shape to calculate its area. it will then ouput those sides and the shape's area, this utilizes
# the same counter while loop as the triangle portion of this script uses.
    elif shape == 'trapezoid':
        loopCount = 0
        while loopCount < 6:
            loopCount += 1
            if loopCount > 4: sys.exit()
            else:
                try:
                    htrap = float(input("Please enter the height of the trapezoid: "))
                    btrapone = float(input("Please enter the top base of the trapezoid: "))
                    btraptwo = float(input("Please enter the bottom base of the trapezoid: "))
                    tarea = htrap * ((btrapone + btraptwo) * .5)
                    print
                    print "The area of a trapezoid with height", htrap, "and top base", btrapone, "and bottom base", btraptwo, "is", tarea,"."
                    break
                except:
                    print "Sorry, you did not enter a number for your value."
                    
# if the user did not corretly type either shape or typed anything else, they will be prompted to do so again by this line.
    else: print "Make sure you enter the correct shape! " , question ()
    
# this line actually calls the function "question" to be run. this comes at the end because everything before this
# was actually setting what the function does
question ()
