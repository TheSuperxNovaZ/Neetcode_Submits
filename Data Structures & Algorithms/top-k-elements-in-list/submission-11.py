class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return sorted(freq, key=freq.get, reverse=True)[:k]