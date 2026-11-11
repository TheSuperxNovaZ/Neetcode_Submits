class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        water, left, right = 0, 0, n-1
        while left<right:
            water = max(water, min(heights[left], heights[right])*(right-left))
            left, right = (left + 1, right) if heights[left] < heights[right] else (left, right - 1)
        return water
        