class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        left = 0
        count = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]

            if char in need:
                need[char] -= 1
                if need[char] >= 0:
                    count += 1

            while count == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]

                if left_char in need:
                    need[left_char] += 1
                    if need[left_char] > 0:
                        count -= 1

                left += 1

        return result