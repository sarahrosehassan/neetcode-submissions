class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Brute force approach
        # edge cases: need to check uppercase or lowercase and punctuation
        # filter out characters so you only et alphanums (need to handle spaces and punctuation)
        # add each letter but no uppercase so only convert to lowercase (case-insensitivity)
        alnumString = ""
        for letter in s:
            if letter.isalnum():
                alnumString += letter.lower()

        return alnumString[::-1] == alnumString

        # Time: O(n) Space: O(n)