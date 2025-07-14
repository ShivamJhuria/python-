import random
for i in range(1,6):
    a=random.randint(1,20)
    b=random.randint(1,20)
    c=a//b
    print("NO 1 => ",a,"NO 2 > ",b)
    z=float(input("Enter a number "))
    if c==z:
        print("The answer is correct ")
    else:
        print("The answer is incorrect")