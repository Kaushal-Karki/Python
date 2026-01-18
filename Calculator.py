a = float(input("Enter your Number:"))
b = float(input("Enter your Number:"))
op = input("Enter operator +-/*:")

if(op=='+'):
    print(a+b)
elif(op=='-'):
    print(a-b)
elif(op=='/'):
    print(a/b)
elif(op=='*'):
    print(a*b)

else:
    print("Invalid OPerator")