list1 = ["ram", "rahul", "disha", "neha", "akash", "priya", "vikas", "sneha", "anil", "rohit", "riya", "tanmay", "shivani", "kiran", "deepak", "sunita"]
c=0
for x in list1:
    if len(x)>5:
        print(x,len(x))
        c+=1

print("total = ",c)