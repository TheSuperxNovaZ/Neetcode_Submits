class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set(nums)
        return len(nums)!=len(uniq)