n=int(input("Enter the number of elements in first list => "))
list1=[input(f"Enter element in the list{i+1}:")for i in range(n)]
p=int(input("Enter the number of elements in first list => "))
list2=[input(f"Enter element in the list{j+1}:")for j in range(p)]
list=list1+list2
print(list)