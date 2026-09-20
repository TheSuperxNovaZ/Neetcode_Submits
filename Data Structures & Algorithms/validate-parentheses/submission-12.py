class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in pair:
                if not stack or stack[-1] != pair[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack