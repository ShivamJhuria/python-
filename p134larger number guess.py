import random
x=random.randint(1,100)
c=0
y=0
s=1
e=100
while y != x:
    print("Your range is ",s," = ",e)
    y=int(input("Enter guess value =>"))
    if y>x:
        print("The guess is less than the number",y)
        e=y
    elif y<x:
        print("The guess is more than the number",y)
        s=y
    else:
        print("you won")
    c=c+1

print("no of guess =",c)