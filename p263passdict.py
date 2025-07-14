# Sample data
marks = {"ram": 33,"rahul": 15,"devesh": 30,"jayul": 34,"jiya": 16,"sadhana": 11,"meena": 19,"karan": 20}
# Print header
print(f"{'name':<10} {'mark':<6} {'result'}")
# Iterate through the dictionary and print students who failed
for name, mark in marks.items():
    if mark < 18:
        print(f"{name:<10} {mark:<6} fail")