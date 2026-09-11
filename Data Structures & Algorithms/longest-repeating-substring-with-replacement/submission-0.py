class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        left = 0
        most = 0

        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1

            while (right - left + 1) - max(dic.values()) > k:
                dic[s[left]] -= 1
                left += 1

            most = max(most, right - left + 1)

        return most