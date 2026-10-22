class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                return num
            else:
                seen[num] = seen.get(num, 0)+1
        return None