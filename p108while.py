while True:
    print("press 1 for Square")
    print("press 2 for Cube")
    print("press 3 for exit")
    op=int(input("Enter opt=> "))
    if op==1:
        num = int(input("Enter the number => "))
        print("Square = ",num*num)
    elif op==2:
        num = int(input("Enter the number => "))
        print("Cube = ", num * num*num)
    elif op==3:
        print("Bye")
        break
    else:
        print("Wrong opt")