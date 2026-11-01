class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq=dict()

        for i in range(0,len(text)):
            freq[text[i]]=freq.get(text[i],0)+1
        
        return min(
            freq.get('b',0),
            freq.get('a',0),
            freq.get('l',0)//2,
            freq.get('o',0)//2,
            freq.get('n',0),
            
        )