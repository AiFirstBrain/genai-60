numbers = []
for i in range(1,6):
    elements = int(input("enter the number: "))
    numbers.append(elements)
print(numbers)
print(sorted(numbers))
print(sorted(numbers, reverse=True))    