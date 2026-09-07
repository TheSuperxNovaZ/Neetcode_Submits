class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        order = sorted(set(nums))
        count = 1
        high = 1
        for i in range(1, len(order)):
            if order[i] == order[i-1]+1:
                count += 1
                high = max(high,count)
            else:
                count=1
        return high

