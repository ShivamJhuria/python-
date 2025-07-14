n=int(input("Enter a number => "))
s=0
e=0
for i in range(1,n+1):
    if i % 2==0:
        print(i)
        s=s+i
        e=e+1
print("\nSum",s,"Count",e)
o=0
r=0
for i in range(1,n+1):
    if i % 2!=0:
        print(i)
        r=r+i
        o=o+1
print("\nSum",r,"Count",o)