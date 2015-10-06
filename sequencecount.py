# Programmer: Luke Krauss
# Date: 11/12/14
# File: sequencecount.py

#The purpose of this program is to count using numbers in a sequence
#All blank lines are added for extra readability

from itertools import * #Imports everything from the itertools module

def main():
    x = y = 2       #Sets two variable equal to 2
    z = (x + y) - 1 #Sets a third variable equal to the sum of previous two variables (x and y), then subtracts 1
    
    print (x)         #Prints a variable
    print (y)
    
    times = 10      #Creates a variable to control a while loop. (Change this to iterate more or less times)
    count = 0 
    
    while times > 0:                #As long as times is greater than 0, execute the following code:
        if count == 0:              #If count is 0, execute this code
            seq_list = []           #Creates an empty list and assigns it to a variable
            seq_list.extend([x, y]) #Extends the list with x and y
            count = 1               #Sets count to 1 so the else statement executes
        else:                       #Otherwise, execute this code
            seq_list.append(y)      #Appends y to a list

        z = (x + y) - 1
        x = y
        y = z
        
        print (z)
        times -= 1  #Subtracts 1 from times
        
    seq_set = set()                             #Creates an empty set using the set() function
    for n in range(len(seq_list)):              #For every n in the range of the length of the list, execute the following code:
        for i in combinations(seq_list, n + 1): #For every i in the list seq_list, find the "combinations" that can be created using those numbers
            seq_set.add(sum(i))                 #Add the sum of the previous combinations. Without sum(). (This would show only the numbers than can be combined, not the combined numbers themselves)

    print
    print (seq_list)
    print 
    print (seq_set)
               
main() #Calls the main function
