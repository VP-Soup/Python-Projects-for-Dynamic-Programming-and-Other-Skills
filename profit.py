def profit(prices):
    max_profit = 0
    minimum = prices[0]
    for i in prices:
        if i < minimum:
            minimum = i
        max_profit = max(max_profit, i - minimum)
    return max_profit

pricetest = [7,4,3,2,1,5]
price = [5, 9, 4, 8, 2]
print(profit(price))
lower = float('inf')
print (1 < lower)