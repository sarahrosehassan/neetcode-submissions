class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # create a dictionary of each integer in the array mapped to its frequency key = num, value = freq
        luckyArray = []
        dict = {}
        for num in arr:
            dict[num] =+ dict.get(num, 0) + 1

        # loop through dictionary
        # if number = frequency put in lucky integers array
        for num, freq in dict.items():
            if num == freq:
                luckyArray.append(num)

        # return max number in the array if array has values
        if luckyArray:
            return max(luckyArray)
        else: 
            return -1
