from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))
            groups[key] = groups.get(key, []) + [word]

        return list(groups.values())