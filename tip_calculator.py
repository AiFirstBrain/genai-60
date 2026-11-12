amount = float(input("enter bill amount in digits: "))
tip_percentage = float(input("enter tip percentage in valid decimal points: "))
tip = amount*tip_percentage/100
print(f"the tip for Rupees {amount:.2f} is rupees {tip:.2f}.")
total = amount + tip
print(f"and the total amount is {total:.2f}.")