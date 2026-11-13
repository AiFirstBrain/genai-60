#calculate tip function
def calculate_tip(amount,percent):
    return amount*percent/100
first_tip = calculate_tip(850, 12.5)
second_tip = calculate_tip(1200, 10)
print(f"first tip is: {first_tip:.2f}")
print(f"second tip is: {second_tip:.2f}")

#get grades from marks
def get_grade(marks):
    if 0<= marks <=100:
        if marks >=90:
            return "A"
        elif marks >=75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"
    else:
        return "invalid"
a = get_grade(89.5)
b = get_grade(150)
print(f"grade {a}")
print(f"grade {b}") 

#palindrome
def is_palindrome(word):
    return word.lower() == word[::-1].lower()

a = is_palindrome("Madam")
b = is_palindrome("python")
print(a)
print(b) 
if is_palindrome("level"):
    print("level is palindrome")
else:
    print("level is not palindrome")    
        