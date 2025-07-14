import random
x=random.randint(1,50)
c=0
y=0
while y != x:
    y=int(input("Enter guess value =>"))
    if y>x:
        print("The guess is greater than the number ")
    elif y<x:
        print("The guess is less than the number ")
    else:
        print("you won")
    c=c+1

print("no of guess =",c)