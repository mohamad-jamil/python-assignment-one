def GCD(a, b):
    while (a != b):
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

ax = 42
bx = 30
result = GCD(ax, bx)
print("The greatest common divisor of " + str(ax) + " and " + str(bx) + " is " + str(result), end=".")
