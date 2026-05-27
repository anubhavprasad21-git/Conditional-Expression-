name=input("enter name:")
total=int(input("How many subject you have:"))
sum=0
for i in range(1,total+1):
    marks=int(input("How many marks you got in this subject:"))
    sum+=marks
print(f"Total Marks in {total} subject is {sum}")
print("Percentage will be",(sum/(total*100))*100)
if (sum/(total*100))*100>=33:
    print(f"Congratulation {name} You Have Passed The Exam")
else:
    print(f"Sorry {name} You Failed")
if (sum/(total*100))*100>=60 and (sum/(total*100))*100<=100:
    print("Division : First Division")
elif (sum/(total*100))*100>=50 and (sum/(total*100))*100<60:
    print("Division : Second Division")
elif (sum/(total*100))*100>=33 and (sum/(total*100))*100<50:
    print("Division : Third Division")
    
