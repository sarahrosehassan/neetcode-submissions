class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1 
        for i in range(len(nums)): # prefix left to right sweep
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1 
        for i in range(len(nums) - 1, -1, -1): # suffix right to left sweep
            result[i] *= suffix # multiply prefix by suffix
            suffix *= nums[i]

        return result

        # Time: O(n) Space: O(1)
                    
        