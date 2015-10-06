# Programmer: Luke Krauss
# Date: 9/15/14
# File: Wordproblems.py

# This program allows a user to input specific numbers for a word problem. In this case, the user is saing up to purchase a car.

def main():

    print ("So you're saving up to buy a car?")
    carCost = input("How much is the car? ")
    currentCash = input("How much money do you have now? ")
    jobWage = input("How much money do you make per hour? ")
    hours = (carCost - currentCash)/jobWage
    days = (hours/24.0)
    weeks = (days/7.0)

    print ("You will need to work " + str(hours) + " hours,"+ str(days) + " days, or " + str(weeks) + " weeks in order to afford this car.")
main()

