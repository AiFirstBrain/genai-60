marks = int(input("enter obtained marks: "))
if 0<=marks<=100:
    if 90 <= marks :
        print("grade is A")
    elif marks >= 75:
        print("grade is B")   
    elif marks>= 60:
        print("grade is C")    
    elif marks>= 40:
        print("grade is D")
    else:
        print("grade is F")    
else:
    print("error")            
    #90, 75, 60, 40, 100