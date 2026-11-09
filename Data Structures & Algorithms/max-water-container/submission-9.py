class Solution:
    def maxArea(self, heights: List[int]) -> int:
        tank = 0
        left = 0
        n = len(heights)
        right = n-1
        while left<right:
            area = min(heights[left], heights[right]) *  (right-left)
            tank = max(tank, area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return tank