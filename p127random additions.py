import random
c1=0
c2=0
for i in range(1,6):
    a=random.randint(1,30)
    b=random.randint(1,30)
    c=a+b
    print("No1 ->",a,"No2 ->",b)
    z=int(input("Enter ur answer => "))
    if c==z:
        print("The answer is correct ")
        c1=c1+1
    else:
        print("The answer is incorrect")
        c2=c2+1
print("Right answer = ",c1," Wrong answer = ",c2)