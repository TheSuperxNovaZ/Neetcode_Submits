from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        a = res.append
        for s in strs:
            a(str(len(s))); a('#'); a(s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        a = res.append
        i = 0
        n = len(s)

        while i < n:
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            j += 1
            a(s[j:j+length])
            i = j + length

        return res