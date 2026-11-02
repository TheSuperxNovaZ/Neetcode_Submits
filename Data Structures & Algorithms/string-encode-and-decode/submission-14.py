class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += st + "~"
        return s

    def decode(self, s: str) -> List[str]:
        lis=[]
        group=""
        for st in s:
            if st == "~":
                lis.append(group)
                group=""
                continue
            group+=st
        return lis    