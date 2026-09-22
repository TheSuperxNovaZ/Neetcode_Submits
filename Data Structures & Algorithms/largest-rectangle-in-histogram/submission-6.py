class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       stack = []
       area = 0
       for i, height in enumerate(heights):
        new_i = i
        while stack and stack[-1][1]>height:
            index, h = stack.pop()
            w = i - index
            area = max(area, h*w)
            new_i = index
        stack.append((new_i, height))
       for index, height in stack:
        width = len(heights)-index
        area = max(area, height*width)
       return area