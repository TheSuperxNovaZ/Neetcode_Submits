class Solution:
     def twoSum(self, nums: list, target: int) -> list:
       seen = {}
       for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
       return []