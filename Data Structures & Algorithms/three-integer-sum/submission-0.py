class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n^2) Space: O(num of triplets) 
        result = []
        # sort the array
        nums.sort()
        # outer loop
        for i, num in enumerate(nums):
            # prevents index wrap and skip duplicate values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # two pointer setup
            l, r = i+1, len(nums)-1
            while l < r:
                # three cases to compute nums[i] + nums[l] + nums[r]
                # sum equals zero, add nums i,l,r to result array
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # move l forward past equal values nums[l]
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    # move r backward past any values equal to nums[r]
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                # if too small, l to the right
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                # if sum is too big move r to the left
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1

        return result