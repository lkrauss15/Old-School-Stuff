#Programmer Name: Luke Krauss
#Program Date: 10/3/14
#Program name fmacalc.py

#Force, acceleration, or mass calculator

def force_calc(a,b):
    c = a * b
    print()
    print("F = MxA = "+ str(a) + "x" + str(b))
    print()
    print ("The force of the object is: " + str(c))

def accel_calc(d,e):
    f = d / e
    print()
    print("A = F/M = " + str(d) + "/" + str(e))
    print()
    print("The acceleration of the object is: " + str(f))

def mass_calc(g,h):
    i = h / g
    print()
    print("M = F/A = " + str(h) + "/" + str(g))
    print()
    print("The mass of the object is: " + str(i))

def main():
    while True:
        question = input("Are you calculating force(1), acceleration(2), or mass(3)? ")
        if question == "1":
            accel = int(input("What's the acceleration of the object? "))
            mass = int(input("What's the mass of the object? "))
            force_calc(accel,mass)
            print()
            while True:
                again = str.upper(input("Again? (Y/N) "))
                print()
                if again == "Y":
                    break
                elif again == "N":
                    return
                else:
                    print("Please type Y or N.")
                    print()
                    continue
        elif question == "2":
            force = int(input("What's the force of the object? "))
            mass = int(input("What's the mass of the object? "))
            accel_calc(force,mass)
            print()
            while True:
                again = str.upper(input("Again? (Y/N) "))
                print()
                if again == "Y":
                    break
                elif again == "N":
                    return
                else:
                    print("Please enter Y or N.")
                    print()
                    continue
        elif question == "3":
            force = int(input("What's the force of the object? "))
            accel = int(input("What's the acceleration of the object? "))
            mass_calc(force,accel)
            print()
            while True:
                again = str.upper(input("Again? (Y/N) "))
                print()
                if again == "Y":
                    break
                elif again == "N":
                    return
                else:
                    print("Please enter Y or N.")
                    print()
                    continue
        else:
            print ("Please type either 1, 2, or 3.")
            print()
            continue
main()

