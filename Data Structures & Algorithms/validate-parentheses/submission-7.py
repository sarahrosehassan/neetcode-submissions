class Solution:
    def isValid(self, s: str) -> bool:
        # s = "[]" output:true
        # s = "([{}])" output:true
        # s = "[(])" output: false
        # parenthese must be closed in the correct order
        # edge cases what if empty? one bracket? #all the same? output:false

        # brute force: compare every signle pair of brackets #O(n^2)
        # and check if every oen bracket can be closed by the right closed bracket O(n)

        # better? solution? We use a stack to get O(n) time
        # you need check if every closing bracket matched to the correct opener
        # put any open brackets in the stack

        stack = []
        mapping = {')':'(','}':'{',']':'[', }

        for bracket in s:
            if bracket in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[bracket] != top_element:
                    return False
            else:
                stack.append(bracket)

        return not stack

        # time complexity: O(n) space complexity: O(n)





