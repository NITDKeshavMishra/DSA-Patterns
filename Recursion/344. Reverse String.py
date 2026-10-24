class Solution:
    def revst(self, s: list[str], start: int, end: int) -> None:
        if start >= end:
            return

        s[start], s[end] = s[end], s[start]
        self.revst(s, start + 1, end - 1)
 
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        self.revst(s, 0, n - 1)