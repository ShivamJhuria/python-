while True:
    print("Menu")
    print("Press 1 for Pizza-30$")
    print("Press 2 for burger-5$")
    print("Press 3 for sandwich-10$")
    print("Press 4 for hot dog-8$")
    print("Press 5 for exit")
    op=int(input("Enter a option => "))
    if op==1:
        p=int(input("Enter the number of pizza needed => "))
        print("Cost for pizza's =",p*30)
    elif op==2:
        b=int(input("Enter the number of burgers needed => "))
        print("Cost for burger's =",b*5)
    elif op==3:
        s=int(input("Enter the number of sandwiches needed =>"))
        print("Cost of the Sandwiches is =",s*10)
    elif op==4:
        h=int(input("enter the number of hot dogs needed =>"))
        print("Cost for the hot dogs =",h*8)
    elif op==5:
        print("Exit")
        print("BYE ^_^")
    else:
        print("Wrong option")
