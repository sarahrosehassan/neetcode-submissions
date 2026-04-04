class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: ["act","pots","tops"]
        # output[['act'], ["pots","tops"]]

        # how would we know that the string in the input is part of a anagram group and which one        
        
        # naive solution 
        # for each string sort it
        # group the strings that have the same sorted version
        # edge cases: if 0-1 strings return string in single list

        # "act" -> sorted -> "act"
        # "pots" -> sorted -> "opts"
        # "tops" -> sorted -> "opts" # same as previous

        # store the alphabetical versions in a hashmap 
        # where key = sorted strings and values = originals

        # dry run
        # word = "act" -> key = "act" -> result = {"act":["act"]}
        # word = "pots" -> key = "opts" -> result = {"act":["act"], "opts":["pots"]}
        # word = "tops" -> key = "opts" -> result = {"act":["act"], "opts":["pots", "tops"]}
        # return values in a list

        result = {}
        for word in strs:
            anagramGroup = "".join(sorted(word)) # join the sorted characters back into a string
            if anagramGroup not in result:
                result[anagramGroup] = [] # initialize anagram group with empty list
            result[anagramGroup].append(word) # get the values list for this key, then add this word to it
        return list(result.values())