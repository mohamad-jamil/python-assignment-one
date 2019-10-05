import random
import math

# using Pythagoras' theorem to determine whether the hit was inside the circle or not
def estimate_pi(precision):
    totalPts = 0
    hitPts = 0
    while True:
        x = random.random() - 0.5
        y = random.random() - 0.5
        if ((math.sqrt(x**2 + y**2)) < 0.5):
            hitPts += 1
            totalPts += 1
        else:
            totalPts += 1

        pi = (hitPts/totalPts) * 4
        roundedPi = round(pi, precision)
        print("Your approximation of pi was " + str(roundedPi) + "")

while True:
    # ask the user for the number of decimal places they want pi approximated to
    precision = int(input("How many decimal places would you like pi approximated to? "))
    estimate_pi(precision)