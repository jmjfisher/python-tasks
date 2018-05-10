# This program calculates the area of a triangle or a trapezoid.

# Once this script is executed it will display the first string of text followed by a blank line for spacing
print "This program finds the area of a triangle or trapezoid."
print 	

# first this will ask the user to enter either triangle or trapezoid so it may use the correct area formula
def question ():
    shape = str(raw_input("Please enter if your shape is a triangle or trapezoid: "))
    print
# if user typed triangle, this will prompt the user to enter a value for both height and base of the triangle for which they want the area
# which will be stored in two variables appropriately named height and base
    if shape == 'triangle':
        height = input("Please enter the height of the triangle: ")
        base = input("Please enter the base length of the triangle: ")
        area = 0.5 * height * base
        print
        print "The area of a triangle with height", height, "and base", base, "is", area,"."
# if the user entered trapezoid, it will flow directly to this portion of the function which asks for the three necessary
# measurements of the shape to calculate its area. it will then ouput those sides and the shape's area
    elif shape == 'trapezoid':
        htrap = input("Please enter the height of the trapezoid: ")
        btrapone = input("Please enter the top base of the trapezoid: ")
        btraptwo = input("Please enter the bottom base of the trapezoid: ")
        tarea = htrap * ((btrapone + btraptwo) * .5)
        print
        print "The area of a trapezoid with height", htrap, "and top base", btrapone, "and bottom base", btraptwo, "is", tarea,"."
# if the user did not corretly type either shape or typed anything else, they will be prompted to do so again by this line.
    else: print "Make sure you enter the correct shape! " , question ()
# this line actually calls the function "question" to be run. this comes at the end because everything before this
# was actually setting what the function does
question ()
