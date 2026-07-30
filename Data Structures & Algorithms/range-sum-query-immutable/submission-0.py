class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = []
        total = 0
        for num in nums:
            total += num
            self.prefixSums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefixSums[right]
        leftSum = self.prefixSums[left-1] if left > 0 else 0

        return rightSum - leftSum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)