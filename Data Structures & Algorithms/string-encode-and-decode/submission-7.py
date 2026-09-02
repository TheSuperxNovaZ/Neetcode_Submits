from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        uni = ""

        for word in strs:
            length = len(word)
            uni += str(length) + "@" + word

        return uni

    def decode(self, s: str) -> List[str]:
        lis = []
        i = 0

        while i < len(s):
            j = i

            # Find the @ delimiter
            while s[j] != "@":
                j += 1

            length = int(s[i:j])

            # Extract the word
            word = s[j + 1:j + 1 + length]
            lis.append(word)

            # Move to the beginning of the next encoded word
            i = j + 1 + length

        return lis