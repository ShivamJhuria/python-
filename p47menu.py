print("Press 1 for Square")
print("PRess 2 for Cube")
ch=int(input("Enter option =>"))

if ch==1:
    no=int(input("Enter no =>"))
    print("Square =",no*no)
elif ch==2:
    no=int(input("Enter no =>"))
    print("Cube =",no*no*no)
else:
    print("Wrong opt")