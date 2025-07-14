weight=float(input("Enter your weight => "))
height=float(input("Enter your height => "))
bmi=(height/weight*weight)
if bmi<18.5:
    print("Underweight",bmi)
elif 18.5<=bmi<=24.9:
    print("normal",bmi)
elif 25<=bmi<=29.9:
    print("Overweight",bmi)
elif 30<=bmi:
    print("Obese",bmi)