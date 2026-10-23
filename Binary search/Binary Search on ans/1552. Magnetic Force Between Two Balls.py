class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        def ispos(position: list[int], m: int, mid: int) -> bool:
            curpos = position[0]
            balls = 1

            for i in range(1, len(position)):
                if position[i] - curpos >= mid:
                    balls += 1
                    curpos = position[i]

                if balls == m:
                    return True

            return False

        position.sort()

        l = 1
        r = position[-1] - position[0]
        ans = 1

        while l <= r:
            mid = l + (r - l) // 2

            if ispos(position, m, mid):
                ans = mid
                l = mid + 1
            else:
                r = mid-1

        return ans