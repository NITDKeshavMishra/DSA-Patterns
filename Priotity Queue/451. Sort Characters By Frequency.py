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
    def frequencySort(self, s: str) -> str:
        freq=dict()
        heap=[]

        for i in range(0,len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        ans=[]
        for key, value in freq.items():
            heapq.heappush(heap, Pair(value, key))
        
        while heap:
            pair = heapq.heappop(heap)
            ans.append(pair.word * pair.count)

        return "".join(ans)
        