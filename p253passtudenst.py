print("Name","Marks","Result")
students={"ram": 33,"rahul": 15,"devesh": 30,"jayul": 34,"jiya": 16,"sadhana": 11,"meena": 19,"karan": 20}
for value,key in students.items():
    if key>=18:
        print(value,key,"pass")