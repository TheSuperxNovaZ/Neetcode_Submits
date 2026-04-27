from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        append = res.append  # local binding (faster)

        for s in strs:
            append(str(len(s)))
            append('#')
            append(s)

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        append = res.append  # local binding (faster)

        i = 0
        n = len(s)

        while i < n:
            j = i

            # find '#'
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            j += 1  # skip '#'

            append(s[j:j + length])
            i = j + length

        return res