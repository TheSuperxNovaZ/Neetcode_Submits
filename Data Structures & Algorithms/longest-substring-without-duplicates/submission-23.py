class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = [-1]*128
        left = long = 0
        for right, char in enumerate(s):
            idx = ord(char)
            if seen[idx] >= left:
                left = seen[idx] + 1
            long = max(long, right - left + 1)
            seen[idx] = right
        return long