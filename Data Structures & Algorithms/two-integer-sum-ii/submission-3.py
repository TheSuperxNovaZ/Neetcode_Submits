class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                sort = [seen[diff]+1, i+1]
                return sorted(sort)
            seen[num] = i
        return []
        