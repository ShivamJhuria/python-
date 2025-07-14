from copyreg import add_extension
from pkgutil import extend_path

n=int(input("Enter the number of elements in first list => "))
list1=[input(f"Enter element in the list{i+1}:")for i in range(n)]
print("list",list1)
c=int(input("Enter the number of elements in second list => "))
list2=[input(f"Enter element in the list {x+1}:")for x in range(c)]
print("list",list2)
list1.extend(list2)
print("Extended List =",list1)


