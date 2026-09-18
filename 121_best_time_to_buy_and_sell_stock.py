class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = 0
        profit = 0
        for i in range(1 , len(prices)):
            buy = min (buy, prices[i])
            sell = prices[i] - buy
            profit = max(profit , sell)
        
        return profit
