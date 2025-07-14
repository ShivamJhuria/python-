attended=int(input("Enter the number of classes attended => "))
held=int(input("Enter the number of classes held => "))
attendance=(attended/held)*100
if attendance<75:
    print("The Student cannot sit in the exam => ",attendance)
else:
    print("The Student can sit in the exam => ",attendance)
