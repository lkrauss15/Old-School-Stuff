#Programmer Name: Luke Krauss
#Date: 10/3/14
#Program Name: calculations.py

#The purpose of this program is to solve various arithmetic using user-inputted values
#All white space is added for extra visibility when reading the programming

from math import * #Imports everything from math

def main(): #Defines a function "main" that takes no arguments
    
    length = float(input("Enter the length of the rectangle: ")) #Asks for user input and assigns it to a variable, then turns it into a float
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))

    rectangle_area = length * width * height #Calculates the area of a rectangle with user-inputted values
    print ("The area of the rectangle is " + str(rectangle_area)) #Prints a string and a float converted to a string for the user to read
    print () #Prints a blank line

    leg_one = float(input("Enter the length of leg 1: "))
    leg_two = float(input("Enter the length of leg 2: "))

    c = ((leg_one) ** 2) + ((leg_two) ** 2) #Calculates the length of the third line squared by squaring the other sides and adding them. Then, assignms that value to a variable
    hypotenuse = sqrt(c) #Takes the square root of the side squared to find the actual length
    print ("The length of the hypotenuse is " + str(hypotenuse))
    print ()

    
    radius_circle = float(input("Enter the radius of the circle: "))
    circle_area = (pi * (radius_circle ** 2)) #Calculates the area of the circle by using pi and a user-inputte value
    print ("The area of the circle is " + str(circle_area))
    print ()


    radius_sphere = float(input("Enter the radius of the sphere: "))
    surface_area = (pi * (radius_sphere ** 2)) * 4 #Calculates the surface area of a sphere by using pi and a user-inputted value
    print ("The surface area of the sphere is " + str(surface_area))
    print ()

main() #Calls the defined function "main" with nothing
