class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        profit=0
        maxi=0
        for i in range(len(prices)):
            if prices[r]>prices[l]:
                profit= prices[r]-prices[l]
                maxi=max(maxi,profit)
            if prices[r]<prices[l]:
                l=r    
            r+=1    
        return maxi        