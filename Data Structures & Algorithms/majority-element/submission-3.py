class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Optimal solution Time: O(n) Space: O(1)
        # Boyer-Moore Voting Algorithm

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate