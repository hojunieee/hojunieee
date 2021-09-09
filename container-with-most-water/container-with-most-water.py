class Solution:
    def maxArea(self, height: List[int]) -> int:
        L=0
        R=len(height)-1
        maxarea = (R-L)*(min(height[L],height[R]))

        while L!=R:
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
            
            temp = (R-L)*min(height[L], height[R])
            if temp > maxarea:
                maxarea = temp
            
        return maxarea