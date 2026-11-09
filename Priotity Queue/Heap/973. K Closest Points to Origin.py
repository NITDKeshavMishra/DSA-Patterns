import heapq
from typing import List

class Pair:
    def __init__(self, dist, point):
        self.dist = dist
        self.point = point

    def __lt__(self, other):
        # Smaller distance comes first in the min-heap
        return self.dist < other.dist


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x, y = point
            dist = x * x + y * y

            pair = Pair(dist, point)
            heapq.heappush(heap, pair)

        ans = []

        for _ in range(k):
            pair = heapq.heappop(heap)
            ans.append(pair.point)

        return ans