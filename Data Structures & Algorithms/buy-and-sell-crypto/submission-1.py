class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input = [7,1,5,3,6,4] output: 5
        # input = [7,6,4,3,1] output: 0
        # input = [3,3,3,3] output: 0

        # brute force: two loops, you look at every single pair you check the difference, store the current highest profit
        # compare the difference you go the highest profit, if the difference is higher than the current high profit you store
        # edge cases = empty array?1element?all the same element? return 0 nothing to buy or else 
        # time : O(n^2) Space: O(1)

        # dry run with [7,1,5]
        # i = 0
          # j = 1 comparing 7 and 1
          # j = 2 comparing 7 and 5

        if len(prices) == 0 or len(prices) == 1:
            return 0

        maxprofit = 0

        for i in range(len(prices)): # buy loop
            for j in range(i+1, len(prices)): # sell

                if (prices[j] - prices[i]) > maxprofit:
                    maxprofit = prices[j] - prices[i]

        return maxprofit
        

        