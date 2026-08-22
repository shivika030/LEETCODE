class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        profit=0
        for i in range(len(prices)-1):
            if prices[r]>prices[l]:
                profit+=prices[r]-prices[l]
            l+=1    
            r+=1       
        return profit        