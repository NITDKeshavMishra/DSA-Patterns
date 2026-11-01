class Solution:
    def checker(self,need:dict,have:dict)->bool:
        for i in need:
            if have.get(i,0)<need[i]:
                return False
        return True


    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        have=dict()
        need=dict()
        

        for i in range(0,len(ransomNote)):
            need[ransomNote[i]]=need.get(ransomNote[i],0)+1
        
        for i in range(0,len(magazine)):
            have[magazine[i]]=have.get(magazine[i],0)+1
        
        return self.checker(need,have)