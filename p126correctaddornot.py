import random
a=random.randint(1,30)
b=random.randint(1,30)
c=a+b
print("No1",a,"No2",b)
z=int(input("Enter ur answer => "))
if c==z:
    print("The answer is correct ")
else:
    print("The answer is incorrect")