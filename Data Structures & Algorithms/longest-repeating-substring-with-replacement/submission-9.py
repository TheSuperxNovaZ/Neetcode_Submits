class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        left = most = 0
        for right in range(len(s)):
            store[s[right]]=store.get(s[right], 0)+1
            while (right - left + 1) - max(store.values()) > k:
                store[s[left]]-=1
                left+=1
            most = max(most, right - left + 1)
        return most
