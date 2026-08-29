class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # two pointers l and r
        l, r = 0, len(nums) - 1

        # search in the middle. if too low remove left half if too high look in right half

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        # else return -1
        return -1

        # Time: O(logn)
        # Space: O(1)

        