# Programmer Name: Luke Krauss
# Program Date: 10/15/14
# Program Name: kinematics.py

# Putting in more than one O or X still executes the if/elifs

# This program solves kinematic equations based on what the user inputs, then prints the answer
# All white space is added for greater readability

from math import *  # Imports everything from the math module
from sys import exit  # Imports just exit() from the sys module

def displacement_nofinal(initial_velo, time, accel):  # Defines a function with variables to be called later in code
    displacement = (float(initial_velo) * float(time)) + (float(accel) * float(time)) / 2  # Does an arithmetic equation with user-inputted variables converted to floats then assigns the value to a variable
    print("The displacement of the object is {0}.".format(displacement))  # Combines a variable converted to a string with another string, then prints the whole thing

def displacement_noaccel(initial_velo, final_velo, time):
    displacement = ((float(initial_velo) + float(final_velo)) * float(time)) / 2
    print("The displacement of the object is {0}".format(displacement))

def displacement_notime(final_velo, initial_velo, accel):
    displacement = ((pow(float(final_velo), 2))) - pow(float(initial_velo), 2) / (2 * float(accel))
    print("The displacement of the object is {0}".format(displacement))

def final_velo_nodisp(initial_velo, accel, time):
    final_velo = float(initial_velo) + (float(accel) * float(time))
    print("The final velocity of the object is {0}".format(final_velo))

def final_velo_notime(initial_velo, accel, displacement):
    final_velo = sqrt(pow(float(initial_velo), 2)) + (2 * (float(accel) * float(displacement)))
    print("The final velocity of the object is {0}".format(final_velo))

def final_velo_noaccel(displacement, time, initial_velo):
    final_velo = (2 * (float(displacement) / float(time))) - float(initial_velo)
    print("The final velocity of the object is {0}".format(final_velo))

def time_nodisp(final_velo, initial_velo, accel):
    time = (float(final_velo) - float(initial_velo)) / float(accel)
    print("The time the object traveled is {0}".format(time))

def time_noaccel(displacement, initial_velo, final_velo):
    time = (float(displacement) * 2) + (float(initial_velo) + float(final_velo))
    print("The time the object traveled is {0}".format(time))

def time_nofinal(displacement, initial_velo, time, accel):
    time = sqrt(abs(((float(displacement) - float(initial_velo)) * 2) / float(accel)))
    print("The time the object traveled is {0}".format(time))

def accel_nodisp(final_velo, initial_velo, time):
    accel = (float(final_velo) - float(initial_velo)) / float(time)
    print("The acceleration of the object is {0}".format(accel))

def accel_nofinal(displacement, initial_velo, time):
    accel = (float(displacement) - ((float(initial_velo)) * float(time)) / float(time)) * 2
    print("The acceleration of the object is {0}".format(accel))

def accel_notime(final_velo, initial_velo, displacement):
    accel = (pow(float(final_velo), 2)) - pow(float(initial_velo), 2) / (2 * float(displacement))
    print("The acceleration of the object is {0}".format(accel))

def initial_velo_noaccel(displacement, time, final_velo):
    initial_velo = ((float(displacement) * 2) / float(time)) - float(final_velo)
    print("The initial velocity of the object is {0}".format(initial_velo))

def initial_velo_nodisp(final_velo, accel, time):
    initial_velo = float(final_velo) - (float(accel) * float(time))
    print("The initial velocity of the object is {0}".format(initial_velo))

def initial_velo_notime(final_velo, accel, displacement):
    initial_velo = sqrt(pow(float(final_velo), 2)) - (2 * (float(accel) * float(displacement)))
    print("The initial velocity of the object is {0}".format(initial_velo))

def initial_velo_nofinal(displacement, accel, time):
    initial_velo = (float(displacement) - ((float(accel) * float(time)) / 2)) / float(time)
    print("The initial velocity of the object is {0}".format(initial_velo))



def directions():  # Defines a function that prints many strings which make up the directions
    print("DIRECTIONS:")
    print("If you don't have a value, put an X")
    print("If you're looking for the value, put O")
    print("Do NOT put more than one X or O")
    print("You need at least 3 values to solve")
    print("You always need an initial velocity unless solving for initial velocity.")
    print()
    
def main():  # Defines a main function
    def go_again():  # Defines the go_again() function
        while True:
            print()
            again = input("Again? (Y/N) ")
            print()
            if again == "Y":
                break  # Exits the while loop back into the start of main()
            elif again == "N":
                exit()  # Stops the program from running
            else:
                print("Please type Y or N.")
                print()
                continue  # Continues to the while loop
            
    first_time = 0  # Creates a variable called first_time, and sets it to 0 (placeholder)
    while first_time == 0:  # Checks to see if first_time is zero. If it is, it executed directions()
        directions()  # Calls the directions() function
        first_time += 1  # Adds 1 to first_time so this code is not executed again (because it won't be the first time)
            
    while True:  # While loop that executes what's included in the loop as long as the code remains True
        displacement = input("What is the displacement of the object? ")  # Asks the user for numerical input, then assigns that input to a variable
        time = input("What is the time the object travels? ")
        accel = input("What is the acceleration of the object? ")
        final_velo = input("What is the final velocity of the object? ")
        initial_velo = input("What is the initial veloctity of the object? ")
        
        xo_check = []
        xo_check.extend([str(displacement), str(time), str(accel), str(final_velo), str(initial_velo)])
        x_count = xo_check.count("X")
        o_count = xo_check.count("O")
        if x_count >= 2 or o_count >= 2:
            print()
            print("You've got too many Xs or Os")
            print()
            continue
        
        else:
        
            if displacement == "O" and accel == "X":  # Checks to see if something is true. If this statement is proven to be true, the following code is executed:
                print()
                displacement_noaccel(initial_velo, final_velo, time)  # Calls a previously defined function with three variables
                go_again()  # Calls the go_again function
                                     
            elif displacement == "O" and final_velo == "X":  # If the first if statement is not proven true, this elif statement aswell as the others are checked in descending order.
                print()
                displacement_nofinal(initial_velo, time, accel)
                go_again()

            elif displacement == "O" and time == "X":
                print()
                displacement_notime(final_velo, initial_velo, accel)
                go_again()

            elif final_velo == "O" and displacement == "X":
                print()
                final_velo_nodisp(initial_velo, accel, time)
                go_again()

            elif final_velo == "O" and time == "X":
                print()
                final_velo_notime(initial_velo, accel, displacement)
                go_again()

            elif final_velo == "O" and accel == "X":
                print()
                final_velo_noaccel(displacement, time, initial_velo)
                go_again()

            elif time == "O" and displacement == "X":
                print()
                time_nodisp(final_velo, initial_velo, accel)
                go_again()
                   
            elif time == "O" and accel == "X":
                print()
                time_noaccel(displacement, initial_velo, final_velo)
                go_again()

            elif time == "O" and final_velo == "X":
                print()
                time_nofinal(displacement, initial_velo, time, accel)
                go_again()

            elif accel == "O" and displacement == "X":
                print()
                accel_nodisp(final_velo, initial_velo, time)
                go_again()

            elif accel == "O" and final_velo == "X":
                print()
                accel_nofinal(displacement, initial_velo, time)
                go_again()

            elif accel == "O" and time == "X":
                print()
                accel_notime(final_velo, initial_velo, displacement)
                go_again()

            elif initial_velo == "O" and accel == "X":
                print()
                initial_velo_noaccel(displacement, time, final_velo)
                go_again()

            elif initial_velo == "O" and displacement == "X":
                print()
                initial_velo_nodisp(final_velo, accel, time)
                go_again()

            elif initial_velo == "O" and time == "X":
                print()
                initial_velo_notime(final_velo, accel, displacement)
                go_again()

            elif initial_velo == "O" and final_velo == "X":
                print()
                initial_velo_nofinal(displacement, accel, time)
                go_again()

            else:  # If none of the if or elif statements are proven true, this code will execute
                print()
                print("Please reread the directions and check inputted values")  # Prints a string for the user to read, giving them information that input may be wrong
                print()  # Prints a blank line
                directions()  # Executes the directions() again, so the user can reread them
                continue  # Sends the user back to the beginning of the while loop
main()  # Calls the main function so the code is executed
