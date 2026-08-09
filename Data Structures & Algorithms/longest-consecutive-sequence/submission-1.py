class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set
        numSet = set(nums)
        # check whether each number is the beginning of a run or stuck in the middle
        longest = 0
        for num in nums:
            if num - 1 not in numSet: # if it is beginning you start counting
                current_length = 1
                while num + current_length in numSet: # then climb while the next number is plus one
                    current_length += 1
                longest = max(current_length,longest) # when it stops you compare against longest
        return longest
        # Time: O(n) Space: O(n)
