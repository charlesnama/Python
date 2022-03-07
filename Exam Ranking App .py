'''     
1) Get marks as the input from user.
mark greater than 35, print pass
greater than 100, you print invalid
lesser than 35 print fail'''

#This code seeks to determine ranking from the marks

print("Kindly input your grades below")
print(" \n")

score=int(input("What is your score?:"))
a=35
b=100
if(int(score) > int(a) and int(score) < int(b)):
    print("PASSED")
if(int(score) > int(b)):
    print("INVALID")
if(int(score) < int(a)):
    print("FAILED")
