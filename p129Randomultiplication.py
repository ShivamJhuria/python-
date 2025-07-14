import random
for i in range(1,7):
    a=random.randint(1,20)
    b=random.randint(1,20)
    c=a*b
    print("NO 1 => ",a,"No 2 => ",b)
    z=int(input("Enter your answer "))
    if c==z:
        print("The answer is correct")
    else:
        print("The answer is incorrect ")
