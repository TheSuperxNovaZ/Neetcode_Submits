class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                if i<seen[diff]:
                    return [i+1, seen[diff]+1]
                else:
                    return [seen[diff]+1, i+1]
            seen[num] = i
        return []
        