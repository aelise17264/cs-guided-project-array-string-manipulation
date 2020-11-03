from collections import deque

def buyAndSellStock(prices):
    max = 0
    prices = deque(prices)
    buy_price = prices.popleft()


    for price in prices:


        if price < buy_price:
            buy_price = price


        else:
            profit = price - buy_price


            if profit > max:
                max = profit


    if max:
        return max
    else:
        return 0



print(buyAndSellStock([6, 3, 1, 2, 5, 4]))
print(buyAndSellStock([8, 5, 3, 1]))
print(buyAndSellStock([4, 3, 3, 3, 3, 4]))

# def buyAndSellStock(prices):
#     buy_price = prices[0]
#     sell_price = 0
#     profit = -1

#     for i in range (0, len(prices)-1):
#         x = prices[i]
#         if x < buy_price:
#             buy_price = x
#             sell_price = 0
#         elif x > sell_price:
#             sell_price = x
#             profit = sell_price - buy_price
        
#     return profit