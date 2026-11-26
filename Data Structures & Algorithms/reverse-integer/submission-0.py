class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        parity = 1 if x > 0 else -1
        x = abs(x)

        res = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if res * 10 + pop > MAX_INT:
                return 0
            res = res * 10 + pop

        return parity * res
