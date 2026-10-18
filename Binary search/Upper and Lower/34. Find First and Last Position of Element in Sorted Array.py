class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def finfirst(nums,target):
            left=0
            right=len(nums)-1
            ans=-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]==target:
                    ans=mid
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return ans

        def finlast(nums,target):
            left=0
            right=len(nums)-1
            ans=-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]==target:
                    ans=mid
                    left=mid+1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return ans
        
        first=finfirst(nums,target)
        last=finlast(nums,target)
        return [first,last]