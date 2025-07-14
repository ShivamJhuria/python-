while True:
    print("press 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 5 for exit")
    op=int(input("Enter a option =>"))
    if op==1:
        a=int(input("Enter number first => "))
        b=int(input("Enter number first => "))
        print(a+b)
    elif op==2:
        a=int(input("Enter number first => "))
        b=int(input("Enter number first => "))
        print(a-b)
    elif op==3:
        a=int(input("Enter number first => "))
        b=int(input("Enter number first => "))
        print(a*b)
    elif op==4:
        a=int(input("Enter number first => "))
        b=int(input("Enter number first => "))
        print(a/b)
    elif op==5:
        print("Exit")
        print("see you^_^")
    else:
        print("Error Input")