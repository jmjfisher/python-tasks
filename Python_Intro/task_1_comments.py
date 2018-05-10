# This program calculates the area of a triangle.

# Once this script is executed it will display the first string of text followed by a blank line for spacing
print "This program finds the area of a triangle."
print 	

# this will prompt the user to enter a value for both height and base of the triangle for which they want the area
#  which will be stored in two variables appropriately named height and base
height = input("Please enter the height of the triangle: ")
base = input("Please enter the base length of the triangle: ")

# a variable called area is created which will have the area of the triangle stored as its value
# which was obtained by multiplying together the user's entered heigh, base, and the value .5
area = 0.5 * height * base

# finally, the program will output the following string of text with the numerical values
# of height, base, and area dispersed accordingly so the user can easily comprehend
# what was calculated
print "The area of a triangle with height", height, "and base", base, "is", area, "."
