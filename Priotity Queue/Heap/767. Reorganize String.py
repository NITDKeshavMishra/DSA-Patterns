import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = dict()

        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1

        heap = []

        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))

        res = ""
        prev = None  # previously used character, waiting to be pushed back

        while heap:
            count, char = heapq.heappop(heap)
            count = -count

            res += char
            count -= 1

            # Push back the previous character only if it still has count left
            if prev is not None:
                heapq.heappush(heap, prev)

            # Store current character if it still has remaining count
            if count > 0:
                prev = (-count, char)
            else:
                prev = None

        # If any character is still left, rearrangement is impossible
        if prev is not None:
            return ""

        return res