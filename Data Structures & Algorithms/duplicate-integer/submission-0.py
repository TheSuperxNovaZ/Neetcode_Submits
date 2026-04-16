class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set(nums)
        if len(uniq)== len(nums):
            return False
        else:
            return True
        
