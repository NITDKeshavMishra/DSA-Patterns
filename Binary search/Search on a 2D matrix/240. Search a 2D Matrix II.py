class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])

        r=0
        c=m-1

        while r<n and c>=0:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                r+=1
            else:
                c-=1
        return False