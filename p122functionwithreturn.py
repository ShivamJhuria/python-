def multiply(a, b):
    return a * b

def max2(a,b):
    if a>b:
        return a
    else:
        return b

a=int(input("Enter a number"))
b=int(input("Enter second number"))
result = multiply(a,b)
print(result)

result=max2(a,b)
print(result)