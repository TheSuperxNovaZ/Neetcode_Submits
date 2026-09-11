class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key = "".join(sorted(s1))
        window = len(key)
        for i in range(len(s2)):
            if i+window<=len(s2) and "".join(sorted(s2[i:i+window]))==key:
                return True
        return False