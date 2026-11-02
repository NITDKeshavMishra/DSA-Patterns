class Solution:
    def helper(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.helper(x, -n)
        
        half = self.helper(x, n // 2)
        
        if n % 2 == 0:
            return half * half
        
        return x * half * half

    def myPow(self, x: float, n: int) -> float:
        return self.helper(x, n)