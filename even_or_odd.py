number = int(input("Enter a whole number: "))
if number>=0:
    if number % 2 == 0:
        print(f"{number} is an even whole number.")
    else:
        print(f"{number} is an odd whole number.")
else:
    print("enter positive whole number")            