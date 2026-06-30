class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqA={}
        uniqB={}
        for i in s:
            if i in uniqA:
                uniqA[i]+=1
            else:
                uniqA[i]=1
        for i in t:
            if i in uniqB:
                uniqB[i]+=1
            else:
                uniqB[i]=1
        return uniqA==uniqB