temp=int(input("Enter the Temperature => "))
if temp<0:
    print("Frezzing cold")
elif 0<=temp<=10:
    print("Very cold Atmosphere")
elif 10<=temp<=20:
    print("Cold Atmosphere")
elif 20<=temp<=30:
    print("Normal Tmperature")
elif 30<=temp<=40:
    print("Hot Atmosphere")
elif temp>40:
    print("Very Hot Atmosphere")

