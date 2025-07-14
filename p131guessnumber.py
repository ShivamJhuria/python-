import random
x=random.randint(1,50)
c=0
y=0
while y!=x:
    y=int(input("Enter your guess : "))
    c=c+1
print("no of guess =",c)