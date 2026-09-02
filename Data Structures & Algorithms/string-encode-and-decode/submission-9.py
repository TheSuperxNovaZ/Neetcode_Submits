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
            while s[j] != "@":
                j += 1
            length = int(s[i:j])
            word = s[j + 1:j + 1 + length]
            lis.append(word)
            i = j + 1 + length
        return lis