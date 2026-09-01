prices=[10,7,5,8,11,9]
min_price=prices[0]
max_profit=0
buy_day=0
sell_day=0
for index, price in enumerate(prices):
    profit=price-min_price
    if profit>max_profit:
        max_profit=profit
        sell_day=index+1
    if price < min_price:
        min_price=price
        buy_day=index+1
print("Max_profit:",max_profit)
print("Buy Day:",buy_day)
print("Sell Day:",sell_day)
    
    

