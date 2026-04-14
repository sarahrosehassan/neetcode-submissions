class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create letter to frequency dictionaries
        ransomNoteFreq = {}
        magazineFreq = {}
        for letter in ransomNote:
            ransomNoteFreq[letter] = ransomNoteFreq.get(letter, 0) + 1

        for letter in magazine:
            magazineFreq[letter] = magazineFreq.get(letter, 0) + 1

        # if letters in ransom note cannot be constructed with magazine return False
        # ransomNote > magazine
        for char in ransomNoteFreq:
            if ransomNoteFreq[char] > magazineFreq.get(char, 0):
                return False
        return True