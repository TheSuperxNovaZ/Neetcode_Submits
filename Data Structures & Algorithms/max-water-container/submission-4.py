class Solution:
    def maxArea(self, heights: List[int]) -> int:
        tank = 0
        left = 0
        right = len(heights)-1
        while left<right:
            width=right-left
            tank = max(tank, min(heights[left], heights[right])*width)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return tank
