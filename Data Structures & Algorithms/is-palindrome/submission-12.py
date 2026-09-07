class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw = ""
        for char in s:
            if char.isalnum():
                raw += char.lower()
        return raw == raw[::-1]