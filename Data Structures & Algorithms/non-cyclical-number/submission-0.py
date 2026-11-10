class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
    
        def square(num):
            val = 0
            while num > 0:
                digit = num % 10
                num //= 10
                val += digit**2
            return val
        while n not in seen:
            seen.add(n)
            n = square(n)
            if n == 1:
                return True
        return False