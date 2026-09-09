class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height)-1
        lmax, rmax = height[left], height[right]
        water = 0
        while left < right:
            if height[left]<height[right]:
                left += 1
                lmax = max(height[left], lmax)
                water += lmax - height[left]
            else:
                right -= 1
                rmax = max(height[right], rmax)
                water += rmax - height[right]
        return water        