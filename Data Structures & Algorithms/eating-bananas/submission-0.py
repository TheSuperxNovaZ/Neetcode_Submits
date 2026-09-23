class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        def check(k):
            time = 0
            for pile in piles:
                time += (pile + k - 1) // k
            return time <= h
        left = 1
        right = max(piles)
        while left < right:
            k = (left + right) // 2
            if check(k):
                right = k
            else:
                left = k + 1
        return left