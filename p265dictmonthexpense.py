expenses={"January" : 2200,
"February" : 2350,
"March" : 2600,
"April" : 2130,
"May" : 2190,
"June" : 1980,
"July" : 2400,
"August" : 2250,
"September" : 2100,"October" : 2400,"November" : 2150,"December" : 2500,}
print("Que 1 - how many dollars did you spend more in feb than jan?")
extra_february = expenses["February"] - expenses["January"]
print(extra_february)
print("Que 2 - What is the total expense in first quarter ?")
Quarter_expense=expenses["January"]+expenses["February"]+expenses["March"]
print(Quarter_expense)
print("Que 3 - Check if you spend exactly 2400$ in any month?")
spent_2400=2400 in expenses.values()
print(spent_2400)
print("Que 4 - Modify the expense of june?")
expenses["June"]= 2080
print(expenses["June"])
print("Que 5 - You refund an item in month of April and god 200 dollars?")
expenses["April"]=expenses["April"]+200
print(expenses["April"])
print("Que 6 - Determine which month had the highest expense and print the name of the month and the amount?")
max_month = max(expenses, key=expenses.get)
max_amount = expenses[max_month]
print(max_month,"",max_amount)
print("Que 7 - Average of first half year?")
Average_expense=expenses["January"]/6+expenses["February"]/6+expenses["March"]/6+expenses["April"]/6+expenses["May"]/6+expenses["June"]/6
print(Average_expense)
print("Que 8 - Month with lowest expense, month name and amount?")
min_month = min(expenses, key=expenses.get)
min_amount = expenses[min_month]
print(min_month,"",min_amount )