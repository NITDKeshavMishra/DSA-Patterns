class Solution:
    def helper(self,row,col)->int:
        if row==0 or col==0 or row==col:
            return 1
        
        return self.helper(row-1,col-1)+self.helper(row-1,col)

    def getRow(self, rowIndex: int) -> list[int]:
        res=[]
        row=rowIndex
        for col in range(0,rowIndex+1):
            res.append(self.helper(row,col))
        
        return res



    class Solution:
    def helper(self,row,col,memo: dict)->int:
        if row==0 or col==0 or row==col:
            return 1
        if (row,col) in memo:
            return memo[(row,col)]
        
        
        memo[(row,col)]= self.helper(row-1,col-1,memo)+self.helper(row-1,col,memo)
        return memo[(row,col)]
    def getRow(self, rowIndex: int) -> list[int]:
        res=[]
        memo={}
        row=rowIndex
        for col in range(0,rowIndex+1):
            res.append(self.helper(row,col,memo))
        
        return res