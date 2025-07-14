P=int(input("Enter the principle amount = "))
R=float(input("Enter the Rate of Interest = "))
T=int(input("Enter the time in years = "))
SI=(P*R*T)/100
print("The Simple Interest = ",SI)
print("Total amount to be given = ",SI+P)