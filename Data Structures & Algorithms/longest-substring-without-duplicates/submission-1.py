class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window and hashset pattern
        # variables: charSet, l, r, resultLen
        # single loop
        #   if there is a duplicate, remove it from set and move left pointer + 1
        #   if there is no duplicate, add char to the set, update resultLen

        charSet = set() # sliding window
        l, r, resultLen = 0, 0, 0

        while (r < len(s)):
            while s[r] in charSet: # there is a duplicate, shrink window until no duplicate
                charSet.remove(s[l])
                l += 1
                
            charSet.add(s[r]) # no duplicate
            resultLen = max(resultLen, len(charSet))
            r += 1

        return resultLen

        # O(n) Time and O(n) space

        
            