n=int(input("Enter a number => "))
s=0

for i in range(1,n+1):
    if i%2==0:
        print(i*i)
    elif i%2!=0:
        print(i*i*i)
print("\nSum=",s)
