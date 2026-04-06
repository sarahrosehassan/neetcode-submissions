class Solution:
    def decodeString(self, s: str) -> str:
        # input:s = 2[a3[b]]c - "abbbabbbc"
        # brute force: make multiple copes of string, expand startign from innermost

        # optimize solution, one pass, stack
        # variables = stack, curStr, num

        # for char in s:
        #    digit -> update num
        #    [ - > add to stack, update (curStr, num), reset curStr to "" num = 0
        #    ] -> pop from stack, recieve (prevStr, k)
        #    letter += curStr
        # return curStr
        # Time: O(n) Space: O(n)

        stack = []
        curStr = ""
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            if char == "[":
                stack.append((curStr, num))
                curStr = ""
                num = 0
            if char == "]":
                prevStr, k = stack.pop()
                curStr = prevStr + k * curStr
            if char.isalpha():
                curStr += char

        return curStr
