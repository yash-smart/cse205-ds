class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        min = prices[0]
        max = None
        for i in range(len(prices)) :
            if(prices[i] < min) :
                min = prices[i]
                max = None
            if (max) and (max < prices[i]) :
                max = prices[i]
                if (max-min) > curr_profit :
                    curr_profit = max-min
            elif (max == None) :
                if(prices[i]>min) :
                    max = prices[i]
                    if (max-min) > curr_profit :
                        curr_profit = max-min
        return curr_profit