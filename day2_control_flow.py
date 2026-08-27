marks=int(input())
if marks>=0 and marks<=100:
    if marks>=90:
        print("A")
        
    elif marks>=75:
        print("B")
        
    elif marks>=50:
        print("C")
    
    if marks>=50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not valid")