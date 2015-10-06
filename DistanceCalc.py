from math import sqrt

def distance_calc(x1,x2, y1, y2):
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print ("%s cm" % (distance))

distance_calc(2, 3, 17, 9)
