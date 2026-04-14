class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # create a dictionary of each integer in the array mapped to its frequency key = num, value = freq
        dict = {}
        for num in arr:
            dict[num] = dict.get(num, 0) + 1

        # loop through dictionary
        # if number = frequency and number bigger than max, replace max_lucky
        max_lucky = -1
        for num, freq in dict.items():
            if num == freq and num > max_lucky:
                max_lucky = num

        return max_lucky

