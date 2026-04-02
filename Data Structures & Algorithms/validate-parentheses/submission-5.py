class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        # Rule: most recently opened bracket must close first (LIFO)
        # Closing bracket is the key, openign. bracket is the value
        # only look up mapping when we see a closer
        # I see a closing bracket, I look up its matching opener

        for bracket in s:
            if bracket in mapping: # pop if we find closing
                top = stack.pop() if stack else '#' # remove and return the top bracket
                if mapping[bracket] != top: # check if top is the expected opening bracket
                    return False
            else: # using else instead of elif bracket in mapping.values() -- values() is O(n), else is O(1)
                stack.append(bracket)

        #return true if stack is empty else false
        return not stack

        # time: O(n) space:O(1)