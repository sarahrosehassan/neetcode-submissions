class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input = [7,1,5,3,6,4] output: 5
        # input = [7,6,4,3,1] output: 0
        # input = [3,3,3,3] output: 0

        # Optimal Solution
        # store the minimum price and the max profit as variables
        # loop through prices once storing minPrice and maxProfit if you findit

        if len(prices) <= 1:
            return 0

        minPrice = prices[0]
        maxProfit = 0 # returns 0 if prices always decrease or are all equal

        for price in prices:  
            if price < minPrice:
                minPrice = price

            curProfit = price - minPrice

            if curProfit > maxProfit:
                maxProfit = curProfit

        return maxProfit