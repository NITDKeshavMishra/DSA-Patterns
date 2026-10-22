import math

class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        def isposs(speed: int) -> bool:
            ans = 0

            for i in range(len(dist) - 1):
                ans += math.ceil(dist[i] / speed)

            ans += dist[-1] / speed
            return ans <= hour

        if hour <= len(dist) - 1:
            return -1

        low = 1
        high = max(max(dist), 10**7)

        while low < high:
            mid = low + (high - low) // 2

            if isposs(mid):
                high = mid
            else:
                low = mid + 1

        return low