class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        
        # while the pointers do not cross
        while l < r:

            # if punctuation skip to next
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # if they are not equal return false
            if s[l].lower() != s[r].lower():
                return False
            
            # while condition is true keep walking
            l += 1
            r -= 1

        return True
