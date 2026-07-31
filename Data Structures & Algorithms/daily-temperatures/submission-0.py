class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # Monotonic stack storing INDICES of days waiting for warmer temps
        
        # Iterate through each day
        for i in range(len(temperatures)):
            # While stack is not empty AND current temp is warmer than the temp at stack's top index
            # This means we found a warmer day for the day at stack[-1]
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()  # Index of the day we're resolving
                result[idx] = i - idx  # Calculate days waited (current index - waiting day's index)
                
            stack.append(i)  # Push current day's index; it's waiting for its warmer day
            
        # Days remaining in stack never found a warmer temperature, so result stays 0
        return result


        