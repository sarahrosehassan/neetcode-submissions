class Solution:

    def encode(self, strs: List[str]) -> str:
        # Pack the list into one string.
        # For each word write: its length, a '#' fence, then the word.

        result = ""
        for word in strs:
            result += str(len(word)) + '#' + word
        return result

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0 # finger: start of the current chunk
        while i < len(s):
            # BEAT 1: find the fence. Walk j from i to the '#'

            j = i #  marker: will walk to the '#'
            while s[j] != '#':
                j += 1 # push j forward one step at a time

            # BEAT 2: read the number. Digits sit between i and j
            length = int(s[i:j])

            # BEAT 3: take the word. It starts after the fence,
            # and runs exactly 'length' characters.
            start = j + 1
            word = s[start: start + length]
            words.append(word)

            # BEAT 4: jump the finger to the next chunk's length label.
            i = start + length
        return words
