class Solution:
    def ispos(self,mid:int,candies:list[int],k:int)->bool:
        tchil=0
        for i in range(0,len(candies)):
            tchil+=candies[i]//mid

            if tchil>=k:
                return True
        return False
    
        
    def maximumCandies(self, candies: list[int], k: int) -> int:
        l=1
        r=max(candies)
        ans=0
        while l<=r:
            mid=l+(r-l)//2

            if self.ispos(mid,candies,k):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        
        return ans

