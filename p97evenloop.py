n=int(input("Enter a number => "))
s=0
c=0
for i in range(1,n+1):
    if i % 2==0:
        print(i)
        s=s+i
        c=c+1
print("\nSum",s,"Count",c)