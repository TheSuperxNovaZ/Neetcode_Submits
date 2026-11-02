class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master = {}
        for st in strs:
            key = "".join(sorted(st))
            if key in master:
                master[key].append(st)
            else:
                master[key] = [st]
        return list(master.values())