class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # given array of intervals [[1,3], [1,5], [6,7]]
        # we need to merge all the overlapping intervals
        # return array of non overlappig intervals 
        # [[1,5], [6,7]]

        # Brute Force
        # Compare every interval against every other interval to check for overlaps O(n^2) time

        # Optimal Solution
        # Sort by start
        # Initialize result with first interval
        # Loop through the list
        #     if there is an overlap where current start <= last end 
        #       update the 2nd interval's end to  be the max of both lasts
        #     else:
        #       add the current interval to the result
        # return result
        # Time: O(n log n) Space: O(n)

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for interval in intervals:
            if interval[0] <= result[-1][1]:
                result[-1][-1] = max(interval[1], result[-1][-1])
            else:
                result.append(interval)
        return result