n=int(input("Enter the number of elements in first list => "))
list1=[input(f"Enter element in the list{i+1}:")for i in range(n)]
list1=sorted(list1)
print(list1)
list1=reversed(list1)
print(list1)