class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ana = {}
        # for i in s:
        #     ana[i] = ana.get(i, 0) + 1
        # anb = {}
        # for j in t:
        #     anb[j] = anb.get(j, 0) + 1
        # return ana == anb
        return sorted(s)==sorted(t)