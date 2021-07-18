class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tempMin = prices[0]
        Maxprofit =0 

        for i in prices:
            if i <tempMin:
                tempMin = i
            else:
                if Maxprofit < i-tempMin:
                    Maxprofit = i-tempMin
        return Maxprofit