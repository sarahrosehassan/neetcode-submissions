class Solution:
    def decodeString(self, s: str) -> str:
        # input: 3[b] -> bbb, 2[a3[b]]c -> abbbabbbc
        # pattern: nested brackets, innermost expands first (LIFO)

        # brute force: find innermost k[str], expand, repeat until no brackets
        # O(n * nesting_depth) time, O(n) space

        # optimal: stack - one pass, push on '[', pop and expand on ']'
        # Variables: stack, currentStr, num

        # for each char in s:
        #   digit -> build num
        #    '[' -> push (curStr, num), reset both
        #    ']' -> pop (prevStr, k), curStr = prevStr + k * curStr
        #    letter -> add to curStr
        # return curStr

        # char | curStr | num | stack
        # "2" | "" | 2 | []
        # "[" | "" | 0 | [("", 2)]
        # "a" | "a" | 0 | [("", 2)]
        # skip ahead to unhappy path
        # "]" | "a" + 3 * "b" = "abbb"
        # "]" | "" + 2 * "abbb" = "abbbabbb"

        stack = []
        curStr = ""
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((curStr, num))
                curStr = ""
                num = 0
            elif char == ']':
                prevStr, k = stack.pop()
                curStr = prevStr + k * curStr
            elif char.isalpha():
                curStr += char
        return curStr
