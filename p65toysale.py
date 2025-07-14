toy=int(input("For electric toy press 1, for key based toy press 2, for charging based toy press 3 => "))
n=int(input("Enter the amount of money for the order => "))
if toy==1:
    if n>1000:
        print("The total amount to be paid =",n-n*10/100)
    else:
        print("No discount",n)
elif toy==2:
    if n>100:
        print("The total amount to be paid =",n-n*5/100)
    else:
        print("No Discount",n)
elif toy==3:
    if n>500:
     print("The total amount to be paid =",n-n*10/100)
    else:
     print("No Discount",n)