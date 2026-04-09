# Problem: Best Time to Buy and Sell Stock
# Topic: Arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution:
def stock_buy_sell(prices):
    max_profit=0
    current_profit=prices[0]
    prev_mininum=prices[0]

    for i in range(len(prices)):
        current_profit=max(prices[i]-prev_mininum,current_profit)
        max_profit=max(current_profit,max_profit)
        prev_mininum=min(prices[i],prev_mininum)
    return max_profit

i=[1,2,58,2,21,5,52,1,82,2,8,2,4,8,]

i=stock_buy_sell(i)
print(i)
    
