class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(0,len(nums)):
            ans.append(nums[nums[i]])
        return ans