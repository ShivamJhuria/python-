n=int(input("Enter a number => "))
s=1
for i in range(1,n+1):
    print(i,end="X")
    s=s*i

print("\nProduct=",s)