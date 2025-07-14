tenure=int(input("Enter the years of working in the company => "))
salary=int(input("Enter the salary => "))
if tenure>=5:
    salary=salary*5/100+salary
    print("The total salary given to the employee is =>",salary)

