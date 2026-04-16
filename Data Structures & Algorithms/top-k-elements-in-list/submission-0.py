class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = {}
        for num in nums:
            final[num]=final.get(num, 0) + 1
        sorted_nums = sorted(final, key=final.get, reverse=True)
        return sorted_nums[:k]