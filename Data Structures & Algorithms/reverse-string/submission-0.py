class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        # replace every element inside the existing list" with the reversed values
        # s = swaps the label on the box
        # s[:] = opens the box and swaps what's inside it