import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def ispossible(speed: int) -> bool:
            totalh = 0
            for pile in piles:
                totalh += math.ceil(pile / speed)
            return totalh <= h

        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high - low) // 2
            if ispossible(mid):
                high = mid  # Try a smaller speed
            else:
                low = mid + 1  # Speed is too slow, increase it
                
        return low