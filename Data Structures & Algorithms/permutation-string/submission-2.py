class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key = "".join(sorted(s1))
        window = len(s1)

        for i in range(len(s2) - window + 1):
            if "".join(sorted(s2[i:i + window])) == key:
                return True

        return False