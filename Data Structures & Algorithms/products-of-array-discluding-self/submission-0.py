class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        i=0
        while i<len(nums):
            val=1
            for j in range(len(nums)):
                if j!=i:
                  val *= nums[j] 
            result.append(val)
            i+=1
        return result