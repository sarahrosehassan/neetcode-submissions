class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums = [1,2,3,3] output: True
        # nums= [1,2,3,4] output: False

        # Brute force solution two nested loops we compare every pair and check if any of them are the same
        # if any of the numbers are the sae, return true

        '''
        for i in range(len(nums)):
            for j in range (i+1, len(nums)): # O(n^2)
                if nums[i] == nums[j]:
                    return True # if numbers are the same 
        return False # space: O(1)
        '''

        # more efficient solution with hashmap: memory O(n) time: O(n)
        '''
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
        '''

        # one liner Pythonic solution memory O(n) time: O(n)
        # if we convert our array to a set and the length is the same as array without conversion to a set
        # this means there are no duplicates and we return False
        # if there are duplicates we return True

        return len(set(nums)) != len(nums)
        