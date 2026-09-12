class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDigitSquares(n):
            if (n%10) == n:
                return n**2
            else:
               return (n%10)**2 + sumDigitSquares(n//10)
        loop = set()
        i = n
        while i not in loop:
            if i == 1:
                return True
            loop.add(i)
            i = sumDigitSquares(i)
        return False