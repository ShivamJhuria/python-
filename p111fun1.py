from itertools import product


def add():
    a=int(input("Enter no1 for addition =>"))
    b = int(input("Enter no2 for addition=>"))
    print("Add = ",a+b)

def max2():
    a = int(input("Enter no1 for finding maximum =>"))
    b = int(input("Enter no2  for finding maximum=>"))
    if a>b:
        print("no1 is max")
    else:
        print("no2 is max")
def aot():
    base=int(input("Enter the base of the triangle=> "))
    height=int(input("Enter the height of the triangle=> "))
    print("Area of the triangle =",base*height*1/2)

def aoc():
    rad=int(input("Enter the radius of the circle => "))
    pi=3.14
    print("The area of the Circle =",rad*rad*pi)

def aos():
    side=int(input("Enter the side of the square => "))
    print("Area of the square =",side*side)

def table():
    n=int(input("Enter the number of which table you want => "))
    i=1
    while i<=10:
        print(n,"X",i,"=",n*i)
        i=i+1

def cube():
    num=int(input("Enter the value for it's cube => "))
    print("The cube of the number =",num*num*num)

def max3():
    num1=int(input("Enter the first number to find maximum => "))
    num2=int(input("Enter the second number to find maximum => "))
    num3=int(input("Enter the third number to find maximum =>"))
    if num1>num2 and num1>num3:
        print("First number is MAX ")
    elif num2>num3 and num2>num1:
        print("Second number is MAX")
    elif num3>num2 and num3>num1:
        print("Third number is MAX")
    else:
        print("all are equal")

def oddeven():
    num=int(input("Enter a number to find if it is odd or even => "))
    if num%2==0:
        print("The number is Even ",num)
    elif num%2!=0:
        print("The number is Odd",num)

def positivenegative():
    num=int(input("Enter a number to see if it is positive or negative "))
    if num>=0:
        print("The entered number is positive ",num)
    elif num<0:
        print("The entered number is negative ",num)

def factorial():
    num=int(input("Enter a number whose factorials you want => "))
    f=1
    for i in range(num,0,-1):
        print(i,end="*")
        f=f*i
    print("\nfactorial =",f)

factorial()
add()
max2()
aot()
aoc()
aos()
table()
cube()
max3()
oddeven()
positivenegative()
