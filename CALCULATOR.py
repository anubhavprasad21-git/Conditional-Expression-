#SIMPLE CALCULATOR
num1=int(input("enter number:"))
num2=int(input("enter number:"))
operator=input("enter what to do sum,sub,multi,div:")
if operator=="sum":
    print(num1+num2)
elif operator == "sub":
    print(num1-num2)
elif operator == "multi":
    print(num1*num2)
elif operator == "div":
    print(num1/num2)
else:
    print("WRONG OPERATOR TYPED")




