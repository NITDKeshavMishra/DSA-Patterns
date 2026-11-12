class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
    
        n=len(profits)
        projects= []
        for i in range(n):
            projects.append((capital[i],profits[i]))
        
        projects.sort()
        i=0
        maxcap=[]
        while k>0:
            while i<n and projects[i][0]<=w:
                heapq.heappush(maxcap,-projects[i][1])
                i+=1
            if not maxcap:
                break
            w-=heapq.heappop(maxcap)
            k-=1
        return w