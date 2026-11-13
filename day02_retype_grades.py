marks = float(input("marks obtained: "))
if 0<=marks<=100:
    if marks>= 90:
        print("A grade")
    elif marks>= 75:
        print("B grade")  
    elif marks>=60:
        print("C grade")
    elif marks>=40:
        print("D grade")
    else:
        print("F grade")
else:
    print("enter valid marks only")                     