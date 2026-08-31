class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        result = []
        for key, values in sorted(freq.items(), key=lambda x:x[1], reverse=True):
                result.append(key)
        # if len(result)<k:
        #     return list(result[:len(result)])
        # else:
        return list(result[:k])