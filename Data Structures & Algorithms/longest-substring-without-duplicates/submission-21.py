class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1]*128
        long = left = 0
        for right, char in enumerate(s):
            idx = ord(char)
            if left <= last_seen[idx]:
                left = last_seen[idx] + 1
            long = max(long, right - left + 1)
            last_seen[idx] = right
        return long
        
