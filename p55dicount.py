market_price=int(input("Enter the Market Price => "))
if market_price>10000:
    market_price=(market_price-market_price*20/100)
    print("The Value is ", market_price)
elif 7000<=market_price<=10000:
    market_price=(market_price-market_price*15/100)
    print("The Value is ", market_price)
elif market_price<=7000:
    market_price=(market_price-market_price*10/100)
    print("The Value is ",market_price)
else:
    print("Not a valid value")