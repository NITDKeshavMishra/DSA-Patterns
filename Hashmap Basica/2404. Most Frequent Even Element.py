class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        
        freq=dict()

        for i in range(0,len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1

        ans=-1
        maxif=0
        
        for num,count in freq.items():
            if num%2==0:
                if count >maxif or count == maxif and num < ans:
                    ans=num
                    maxif=count
        
        return ans