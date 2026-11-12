number = float(input("enter your number: "))
choice = input("enter k2m for km to miles and m2k for miles to km: ")
if choice == "k2m" and number>=0:
    result = number * 0.621371
    print(f"the {number}km will be {result:.2f} miles.")
elif choice == "m2k" and number>=0:
    result = number / 0.621371
    print(f"the {number} miles is {result:.2f} km.")    
else:
    print("please enter valid choice or direction")    