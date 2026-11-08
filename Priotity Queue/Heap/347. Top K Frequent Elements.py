class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq=dict()

        for i in range(0,len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        
        heap=[]

        for key,value in freq.items():
            heapq.heappush_max(heap,(value,key))
        
        ans=[]

        for i in range(k):
            count,num=heapq.heappop_max(heap)
            ans.append(num)
        return ans