# Take three numbers and print the largest one

n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
if n1>n2 and n1>n3:
    print("First number is the largest number:",n1)    #comma(,) is imp to tells python which is string and which is variable
elif n2>n1 and n2>n3:
    print("Second number is the largest number:",n2)
elif n3>n1 and n3>n2:
    print("Third number is the largest number:",n3)
else:
    print("Inappropriate Data Is Entered")
   