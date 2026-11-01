class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=dict()

        for i in range(0,len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        odd=False
        res=0
        for i in freq:
            if freq[i]%2==0:
                res+=freq[i]
            else:
                res+=freq[i]-1
                odd=True
        
        if odd:
            res+=1
        return res