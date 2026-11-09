class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left,right,water,lmax,rmax = 0,n-1,0,0,0
        while left<right:
            if height[left]<=height[right]:
                lmax=max(lmax, height[left])
                water+=lmax-height[left]
                left+=1
            else:
                rmax=max(rmax, height[right])
                water+=rmax-height[right]
                right-=1
        return water
