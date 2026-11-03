class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        high = 0
        for num in nums:
            if num - 1 not in setNums:
                count = 1
                while num + count in setNums:
                    count += 1
                high = max(high, count)
        return high