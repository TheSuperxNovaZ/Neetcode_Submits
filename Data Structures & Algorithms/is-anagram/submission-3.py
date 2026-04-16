class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqA={}
        uniqB={}
        for x in s:
            uniqA[x] = uniqA.get(x,0) + 1
        for y in t:
            uniqB[y] = uniqB.get(y,0) + 1
        return uniqA==uniqB