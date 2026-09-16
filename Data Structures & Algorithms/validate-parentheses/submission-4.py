class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i].isalnum():
                continue
            elif s[i] in ("(","{","["):
                stack.append(s[i])
            elif s[i] in (")","}","]"):
                if s[i] == ")":
                    if stack and stack[-1]=="(":
                        stack.pop()
                    else:
                        return False
                if s[i] == "}":
                    if stack and stack[-1]=="{":
                        stack.pop()
                    else:
                        return False
                if s[i] == "]":
                    if stack and stack[-1]=="[":
                            stack.pop()
                    else:
                            return False
        return not stack