def max_profit_one_transaction(prices):
    if len(prices) < 2:
        return 0, None, None
    minimum_price = prices[0]
    minimum_day = 0
    best_profit = 0
    buy_day = sell_day = None
    for day in range(1, len(prices)):
        profit = prices[day] - minimum_price
        if profit > best_profit:
            best_profit, buy_day, sell_day = profit, minimum_day, day
        if prices[day] < minimum_price:
            minimum_price, minimum_day = prices[day], day
    return best_profit, buy_day, sell_day

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    profit, buy_day, sell_day = max_profit_one_transaction(prices)
    print("Optimization challenge: stock profit")
    print("Prices:", prices)
    print("Maximum profit:", profit)
    print("Buy day (0-based):", buy_day)
    print("Sell day (0-based):", sell_day)
