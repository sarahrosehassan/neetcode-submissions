class Solution:
    def validPalindrome(self, s: str) -> bool:
        # keep track of how many letters do not match with avaraiables
        # do the generic algorithm for checkig for palindrome
        
        #helper function to check if substring s[l:r+1] is a palindrome
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        # two-pointer check with one deletion tolerance
        l,r = 0, len(s)-1

        while l<r:
            if s[l] != s[r]:
                # try skipping left char or right char
                return is_palindrome(l+1, r) or is_palindrome(l, r-1)
            l+=1
            r-=1

        return True # palindrome if goes through the whole whilte loop

        # Time: O(n), Space: O(1)
        

        

