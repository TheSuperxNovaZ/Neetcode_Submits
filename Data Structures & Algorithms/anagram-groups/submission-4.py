class Solution:
    def groupAnagrams(self, strs: list) -> list:
        groups={}
        for word in strs:
            key = ''.join(sorted(word))
            groups[key] = groups.get(key, []) + [word]
        return list(groups.values())