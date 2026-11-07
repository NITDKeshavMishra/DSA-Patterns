class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        heapm=[]

        for i in range(0,len(nums)):
            heapq.heappush_max(heapm,nums[i])

        for i in range(0,k-1):
            heapq.heappop_max(heapm)
        
        return heapm[0]