class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Variables: dict, bucket, result
        # fill the dict
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
                
        # create and fill the bucket
        bucket = [[] for i in range(len(nums) + 1)]
        for num, count in dict.items():
            bucket[count].append(num)
            
        # use the bucket to build the result
        # example [[], [1], [2], [3], [], [], [] ]
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
                    
        # Time: O(n) Space: O(n)

