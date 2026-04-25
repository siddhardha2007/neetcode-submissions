class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # initialize before loop
        profit = 0                 # initialize before loop
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit
  
       
        


                

        