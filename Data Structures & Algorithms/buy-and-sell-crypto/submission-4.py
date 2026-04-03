class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input = [7,1,5,3,6,4] output: 5
        # input = [7,6,4,3,1] output: 0
        # input = [3,3,3,3] output: 0

        # Optimal Solution
        # store the minimum price and the max profit as variables
        # loop through prices once storing minPrice afi you find a price lower than minprice,
        # Store maxProfit if you find current profit you calculated is higher than the maxProfit
        # Time: O(n) Space: O(1)
        # Dry Run [7,1,5,3,6,4]
        # is price less than minPrice? // is price - minPrice higher than maxProfit?
        # 7 -> minPrice = 7, maxProfit = 0
        # 1 -> minPrice = 1, maxProfit = 0
        # 5 -> minPrice = 1, maxProfit = 4
        # 3 -> minPrice = 1, maxProfit = 4
        # 6 -> minPrice = 1, maxProfit = 5
        # 4 -> minPrice = 1, maxProfit = 5


        minPrice = prices[0]
        maxProfit = 0 # returns 0 if prices always decrease or are all equal
        if len(prices) <= 1:
            return 0

        for price in prices:  
            if price < minPrice:
                minPrice = price

            curProfit = price - minPrice

            if curProfit > maxProfit:
                maxProfit = curProfit

        return maxProfit