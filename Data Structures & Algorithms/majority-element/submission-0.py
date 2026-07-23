class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # check if the element appears more than len(nums)/2 times

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1 # initiliziing the hashmap with all the counts key = number, value = number of times i occurs
        
        # check in the dictionary if the value occurs more than  ⌊len(nums) / 2⌋ times

        for key, value in count.items():
            if value > (len(nums) / 2):
                return key

        # Time O(n) Space: O(n)

        
        