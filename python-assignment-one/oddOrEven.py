while True:
    try:
        num = int(input("Pick any number and I will identify it to be odd or even: "))
    except ValueError:
        print("That's not a number!\n")
        continue
    else:
        break

if (int(num) % 2) == 0:
    print("Your number was even!\n")
elif (int(num) % 2) == 1:
    print("Your number was odd!\n")