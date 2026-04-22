class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqA={}
        uniqB={}
        for x in s:
            if x in uniqA:
                uniqA[x] += 1
            else:
                uniqA[x] = 1
        for y in t:
            if y in uniqB:
                uniqB[y] += 1
            else:
                uniqB[y] = 1
        return uniqA==uniqB
