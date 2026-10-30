class Solution:
    def helper(self, n: int, memo: dict) -> int:
        if n <= 2:
            return n
        if n in memo:
            return memo[n]
        memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        return memo[n]

    def climbStairs(self, n: int, memo=None) -> int:
        if memo is None:
            memo = {}
        return self.helper(n, memo)