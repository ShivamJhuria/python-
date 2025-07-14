your_expenses={"Clothes":1100,"Shoes":1000,"Watch":900,"MobileRecharge":699,"Petrol":1980,}
wife_expenses={"Clothes":2310,"Shoes":999,"Make up":3670,"MobileRecharge":799,"Dth Recharge ":999,}
your_total = sum(your_expenses.values())
wife_total = sum(wife_expenses.values())
print(your_expenses,"<>",wife_expenses)
if your_total > wife_total:
    spender = "You"
    print(spender)
else:
    spender = "Your Wife"
    print(spender)
common_items = set(your_expenses.keys()) & set(wife_expenses.keys())
comparison = {}
for item in common_items:
    your_amount = your_expenses[item]
    wife_amount = wife_expenses[item]
    if your_amount > wife_amount:
        comparison[item] = "You"
        print(common_items)
    elif wife_amount > your_amount:
        comparison[item] = "Your Wife"
        print(common_items)
    else:
        comparison[item] = "Equal"
        print(common_items)

