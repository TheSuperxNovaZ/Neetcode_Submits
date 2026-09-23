class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if i<n-1 and nums[i+1]-nums[i]<0:
                return nums[i+1]
        return nums[0]
            

                