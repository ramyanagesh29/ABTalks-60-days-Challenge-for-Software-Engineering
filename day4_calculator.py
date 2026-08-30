a=int(input())
b=int(input())
operator=input()
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    if(b==0):
        print("Division by zero error")
    else:
        print(a/b)
else:
    print("Invalid operator")
