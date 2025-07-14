import random
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
y=int(input("Enter one option from above => "))
if y==1:
    for i in range(1,6):
        a=random.randint(1,100)
        b=random.randint(1,100)
        c=a+b
        print("NO.1 =>",a,"NO.2 =>",b)
        z=int(input("Enter your answer "))
        if c==z:
            print("The answer is correct ")
        else:
            print("The answer is incorrect ")
elif y==2:
    for i in range(1,6):
        a=random.randint(1,100)
        b=random.randint(1,100)
        c=a-b
        print("NO.1 => ",a,"NO.2 => ",b)
        z=int(input("Enter your answer"))
        if c==z:
            print("The answer is correct")
        else:
            print("The answer is incorrect")
elif y==3:
    for i in range(1,6):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = a * b
        print("NO.1 => ", a, "No.2 => ", b)
        z = int(input("Enter your answer "))
        if c == z:
            print("The answer is correct")
        else:
             print("The answer is incorrect ")
elif y==4:
    for i in range(1, 6):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = a // b
        print("NO.1 => ", a, "NO.2 > ", b)
        z = float(input("Enter a number "))
        if c == z:
            print("The answer is correct ")
        else:
            print("The answer is incorrect")