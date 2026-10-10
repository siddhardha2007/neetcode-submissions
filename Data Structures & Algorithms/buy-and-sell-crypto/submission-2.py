class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxProfit=0
        for i in range(n):
            for j in range(i,n):
                maxProfit=max(maxProfit,prices[j]-prices[i])
        return maxProfit
    
                