import random
secret = random.randint(1,20)
my_guess = 21
guess = 0
while secret != my_guess:
    my_guess = int(input("enter a random integer in range (1,20): "))
    if secret > my_guess:
        print("too low")
        
            
    if secret<my_guess:
        print("too high")
        
    guess +=1            
print(guess)            