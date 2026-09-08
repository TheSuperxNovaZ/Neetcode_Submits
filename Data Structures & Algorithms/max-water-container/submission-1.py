class Solution:
    def maxArea(self, heights: List[int]) -> int:
        tank = 0
        n = len(heights)
        left = 0
        right = n-1
        while left<right:
            width=right-left
            area = min(heights[left], heights[right])*width
            tank = max(tank, area)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1

        return tank
