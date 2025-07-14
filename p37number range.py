eng=int(input("Enter marks in English => "))
Maths=int(input("Enter marks in Maths => "))
SS=int(input("Enter marks in SS => "))
total=eng+Maths+SS
if 0<total<50:
    print(" C ")
elif 50<total<100:
    print(" B ")
else:
    print(" A ")