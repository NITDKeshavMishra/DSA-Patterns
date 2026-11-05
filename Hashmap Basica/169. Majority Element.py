class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq=dict()

        for i in range(0,len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        
        highest_freq_key = max(freq, key=freq.get)
        return highest_freq_key