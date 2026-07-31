class Solution:
    def maxProfit(self, num: List[int]) -> int:
        profit=0
        for i in range(0,len(num)-1):
            for j in range(i+1, len(num)):
                if num[j]-num[i]>profit:
                    profit=num[j]-num[i]
        return profit
                