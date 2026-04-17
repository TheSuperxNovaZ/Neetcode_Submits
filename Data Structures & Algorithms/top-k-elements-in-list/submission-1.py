class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        seq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        result = []
        for x in range(k):
            result.append(seq[x][0])
        return  result