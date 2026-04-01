class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmaps = {}
        hashmapt = {}
        # .get(key, default) -- returns value for key, or default if key not found
        for letter in s:
            hashmaps[letter] = hashmaps.get(letter, 0) +  1 # need to initialize hashmap with 0 in order to increment

        for letter in t:
            hashmapt[letter] = hashmapt.get (letter, 0) + 1

        return hashmaps == hashmapt

        # Time: O(n+m) Space: O(1)