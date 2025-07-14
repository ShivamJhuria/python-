print("Press s for Square")
print("PRess c for Cube")
ch=input("Enter character =>")

if ch=="s":
    no=int(input("Enter no =>"))
    print("Square =",no*no)
elif ch=="c":
    no=int(input("Enter no =>"))
    print("Cube =",no*no*no)
else:
    print("Wrong opt")