class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        long = 0
        left = 0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1
            char.add(s[right])
            long = max(long, right-left+1)
        return long