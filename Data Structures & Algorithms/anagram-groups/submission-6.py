from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            key = ''.join(sorted(word))
            result[key]=result.get(key, [])+[word]
        return list(result.values())