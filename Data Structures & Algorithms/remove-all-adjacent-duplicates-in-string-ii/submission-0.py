class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # What we are given: s = "deeedbbcccbdaa" string and integer k = 3
        # What we do: delete all the groups of k adjacent identical characters
        # concatenate leftover string and repeatedly delete
        # What we return: return the final string
        
        # Pseudocode
        # Variables: stack = []
        # single loop
        #     if top char in stack matches curr char:
        #         increment count
        #     else:
        #         append(char, +1)
        #     if top count equals k:
        #         pop it off
        # build result string from what's left on the stack

        # Dry Run
        # s = "aabba", k = 2
        # stack
        # char = 'a', stack = []
        # stack = [['a', 1]]

        # char = 'a', top = 'a', increment count
        # stack = [['a', 2]] 
        # count = k, pop it off
        # stack = []

        # stack = [['a', 1]]
        # a * 1 = 'a'
        # return a

        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1  # increment count
            else:
                stack.append([char, +1])
            if stack[-1][1] == k:
                stack.pop() # delete char, count pair from stack
        
        result = ""
        for char, count in stack:
            result += char * count
        return result

        # One liner result: return "". join(char*count for char count in stack)
        # Time: O(n) one pass Space: O(n)



