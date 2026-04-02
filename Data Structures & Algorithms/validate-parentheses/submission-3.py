class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        # I see a closing bracket, I look up. its matching opener

        for bracket in s:
            if bracket in mapping: # pop if we find closing
                top = stack.pop() if stack else '#' # remove and return the top bracket
                if mapping[bracket] != top: # check if top is the expected opening bracket
                    return False
            elif bracket in mapping.values(): # check keys for opening bracket to add to stack
                stack.append(bracket)

        #return true if stack is empty else false
        return not stack