class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap=[]
        for num in arr:
            dist=abs(num-x)
            heapq.heappush(heap,(dist,num))
            
        
        res=[]
        for i in range(0,k):
            dist,num=heapq.heappop(heap)
            res.append(num)
        
        res.sort()
        return res
        
