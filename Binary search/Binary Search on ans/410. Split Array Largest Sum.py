class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def capri(nums: int, mid: int)->int:
            seperate=0
            talia=0
            for i in range(0,len(nums)):
                talia+=nums[i]
                if talia>mid:
                    seperate+=1
                    talia=nums[i]
            return seperate+1

        low=max(nums)
        high=sum(nums)
        while low<high:
            mid=low+(high-low)//2
            bestgalomi=capri(nums,mid)

            if bestgalomi<=k:
                high=mid
            else:
                low=mid+1
        return low