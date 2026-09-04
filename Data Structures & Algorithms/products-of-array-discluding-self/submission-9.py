class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       n = len(nums)
       results=[]
       prefix = 1
       for i in range(n):
         results.append(prefix)
         prefix*=nums[i]
       postfix = 1
       for i in range(n-1, -1 , -1):
         results[i]*=postfix
         postfix*=nums[i]
       return results
