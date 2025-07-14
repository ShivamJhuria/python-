marks = {"ram": 33,"rahul": 15,"devesh": 30,"jayul": 34,"jiya": 16,"sadhana": 11,"meena": 19,"karan": 20,"anita": 25}
passed_count = 0
for student, mark in marks.items():
    if mark >= 18:
        passed_count += 1
print("Number of passed students:", passed_count)
