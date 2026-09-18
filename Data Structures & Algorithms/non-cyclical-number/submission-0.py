class Solution:
    def isHappy(self, n: int) -> bool:
        def check(n: int) -> int:
            add = 0
            while n>0:
                digit = n%10
                add += digit * digit
                n//=10
            return add
        seen = set()
        while n!=1:
            n = check(n)
            if n in seen:
                return False
            seen.add(n)
        return True

