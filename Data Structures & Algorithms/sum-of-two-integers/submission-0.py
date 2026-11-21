class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_int = 0x7fffffff
        mask = 0xffffffff

        while b != 0:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry
        
        return a if a <= max_int else ~(a ^ mask)
