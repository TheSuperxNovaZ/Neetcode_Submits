class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for char in s:
            if char.isalnum():
                check += char.lower()
        return check==check[::-1]
