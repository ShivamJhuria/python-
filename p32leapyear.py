numofdays=int(input("Enter the number of days => "))
if numofdays==366:
    print("Leap Year")
elif numofdays==365:
    print("Normal Year")
else:
    print("Invalid number")