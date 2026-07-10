class Solution:
    from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in master:
                master[key] = []

            master[key].append(word)

        result = []

        for value in master.values():
            result.append(value)

        return result