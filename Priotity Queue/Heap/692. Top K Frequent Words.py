import heapq

class Pair:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        # Higher frequency should come first
        if self.count != other.count:
            return self.count > other.count

        # If frequencies are equal, smaller word comes first
        return self.word < other.word


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = dict()

        for i in range(len(words)):
            freq[words[i]] = freq.get(words[i], 0) + 1

        heap = []

        for key, value in freq.items():
            heapq.heappush(heap, Pair(value, key))

        ans = []

        for _ in range(k):
            pair = heapq.heappop(heap)
            ans.append(pair.word)

        return ans