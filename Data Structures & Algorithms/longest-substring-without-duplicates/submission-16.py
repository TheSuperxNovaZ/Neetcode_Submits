class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 128
        left = longest = 0

        for right, char in enumerate(s):
            idx = ord(char)

            if last_seen[idx] >= left:
                left = last_seen[idx] + 1

            last_seen[idx] = right
            longest = max(longest, right - left + 1)

        return longest
        
