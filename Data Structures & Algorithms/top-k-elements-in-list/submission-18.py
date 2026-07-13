class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for num in nums:
            data[num]=data.get(num, 0)+1
        return sorted(data, key=data.get, reverse=True)[:k]