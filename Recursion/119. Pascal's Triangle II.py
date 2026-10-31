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