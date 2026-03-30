class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Example 1 [3,4,5,6], target = 7 , Output: [0,1]
        # nums = [4,5,6] , target = 10, [0,2]

        # Brute force:  nested loop where we compare every single pair in the list to see if it adds up to target
        # Brute force: O(n^2)

        # Optmized: Hashmap, one pass, add number and index to the hashmap, calculate the complement target - num
        # we check if the partner of the number we are loopign through is in the hashmap O(n)

        hashmap = {}

        for i, num in enumerate (nums):
            complement = target - num # checking if partner is in hashmap
            if complement in hashmap: # check if in keys
                return [hashmap[complement], i] # return indices
            hashmap[num] = i

