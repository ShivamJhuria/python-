n=int(input("Enter a number => "))
s=0
for i in range(n,0,-1):
    print(i,end="+")
    s=s+i

print("\nSum=",s)