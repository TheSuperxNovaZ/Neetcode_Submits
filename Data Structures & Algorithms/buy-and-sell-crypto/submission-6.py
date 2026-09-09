class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        buy = prices[0]
        for i in range(n):
            if prices[i]<buy:
                buy=prices[i]
            elif profit<prices[i]-buy:
                profit=prices[i]-buy
        return profit
            
