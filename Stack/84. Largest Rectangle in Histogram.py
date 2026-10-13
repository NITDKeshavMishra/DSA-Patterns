from collections import deque
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        
        n=len(heights)
        left=[0]*n
        right=[0]*n
        st=deque()

        for i in range(n-1,-1,-1):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()

            right[i] = n if not st else st[-1]
            st.append(i)

        while st:
            st.pop()

        for i in range(0,n):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            
            left[i] = -1 if not st else st[-1]
            st.append(i)
        
        ans=0

        for i in range(0,n):
            wid=right[i]-left[i]-1
            currA=heights[i]*wid
            ans=max(ans,currA)
        
        return ans