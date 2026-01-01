a=6
b=2
count=0
print("You have two numbers a and b with values, a=6 and b=2\n")
sum=int(input("Enter the sum of two numbers:"))
if(sum==8):
    print("Yes you are correct")
    count=count+1
else:
    print("Incorrect!! Correct answer is:",6+2)

diff=int(input("Enter the subtraction of two numbers:"))
if(diff==4):
    print("Yes you are correct")
    count+=1
else:
    print("Incorrect!! Correct answer is:",6-2)

mul=int(input("Enter the multiplication of two numbers:"))
if(mul==12):
    print("Yes you are correct")
    count+=1
else:
    print("Incorrect!! Correct answer is:",6*2)
div=int(input("Enter the division of two numbers"))
if(div==3):
    print("You are correct")
    count+=1
else:
    print("Incorrect!! correct answer is:",6/2)
exp=int(input("Enter the exponent of two numbers:"))
if(exp==32):
    print("yes you are correct")
    count+=1
else:
    print("You are wrong correct answer is:",2**6)

print("You scored ",count,"out of 5")

