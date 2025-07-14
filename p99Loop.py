n=int(input("Enter a number => "))
s=0
e=0
o=0
r=0
for i in range(1,n+1):
    if i % 2==0:
        print(i,"is even")
        s=s+i
        e=e+1
    else:
        print(i,"is odd")
        r=r+i
        o=o+1
print("\nSum of even ",s,"Count",e)
print("Sum of odd ",r,"Count",o)