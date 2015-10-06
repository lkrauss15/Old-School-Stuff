def main():
    while True:
        meal_cost = int(input("What is the cost of the meal? "))
        tip_percent = int(input("Would you like to give a 15% or an 18% tip? "))
        tax  = meal_cost * 0.0675
        if tip_percent == 15:
            tip_one = meal_cost * 0.15
            meal_one = meal_cost + tip_one + tax
            print("The cost of the meal with tax and a tip is:" + str(meal_one))
            break
        elif tip_percent  == 18:
            tip_two = meal_cost * 0.18
            meal_two = meal_cost + tip_two + tax
            print("The cost of the meal with tax and a tip is: " + str(meal_two))
            break
        else:
            print("Please enter either 15 or 18.")
            print()
            continue  
main()
