class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqA={}
        uniqB={}
        for i in s:
           uniqA[i] = uniqA.get(i, 0)+1
        for i in t:
            uniqB[i] = uniqB.get(i, 0)+1
        return uniqA==uniqB