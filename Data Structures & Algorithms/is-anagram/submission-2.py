class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = "racecar", T = "carrace" output: True
        # s = jar, t = "jam" output: false
        # s = "aaa", t = "aaa" output:True
        # s = "aab", t = "aba" output:True
        # s = "a", t = "a" output:True

        # put all our strings in an array, then sort them and check if they are equal
        # if they are equal we will return True, if the two arrays are not equal: return false
        # s = "racecar", T = "carrace" output: True

        # s = ['r', 'a', 'c', 'e', 'c' ,'a', 'r']
        # s = ['a', 'a', 'c', 'c', 'c' , 'r'] sort array is going ottake nlogn time
        # should return true s= ['a', 'a', 'c', 'c', 'c' , 'r']t = ['a', 'a', 'c', 'c', 'c' , 'r']
        
        # return sorted(s) == sorted(t)
        # time complexity = nlogn space: complexity O(n)

        # to get better time we'll use a hashmap
        # two hashmaps, put all our letters in the hashmap key = letter, value =  frequency, increment value when you add new letters
        # check if hashmaps are equvalent
        # edge case: if the strings are not the same length they are not anagrams
        

        if len(s) != len(t):
            return False

        hashmaps = {}
        hashmapt = {}

        for letter in s:
            hashmaps[letter] = hashmaps.get(letter,0)  + 1 # need to 1 to our value to add frequency

        for letter in t:
            hashmapt[letter] = hashmapt.get(letter,0) + 1
            
        return hashmaps == hashmapt

        # time complexity O(n) space: O(1)

