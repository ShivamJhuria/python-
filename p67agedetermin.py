age=int(input("Enter the age of the user => "))
if age<13:
    print("The user is a child")
elif 12<age<20:
    print("The user is a teenager")
elif 20<=age<=64:
    print("The user is an adult")
elif age>64:
    print("The user is a Senior")