num=int(input("Enter a number => "))
if num%2!=0:
    print("Wierd")
elif num%2==0 & 2<=num<=5:
    print("Not Wierd")
elif num%2==0 & 6<=num<=20:
    print("Wierd")
elif num%2==0 & num>20:
    print("Not Wierd")
