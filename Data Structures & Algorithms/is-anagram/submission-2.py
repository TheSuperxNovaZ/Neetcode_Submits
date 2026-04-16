class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqA={}
        uniqB={}
        for x in s:
            uniqA[x] = uniqA.get(x,0) + 1
        for y in t:
            if y in uniqB:
                uniqB[y] += 1
            else:
                uniqB[y] = 1
        return uniqA==uniqB