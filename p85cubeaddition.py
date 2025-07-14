n=int(input("Enter a number => "))
s=0
for i in range(1,n+1):
    print(i*i*i,end="+")
    s=s+i*i*i

print("\nSum of cubes = ",s)