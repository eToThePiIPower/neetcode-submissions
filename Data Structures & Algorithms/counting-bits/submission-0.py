class Solution:
    def countBits(self, n: int) -> List[int]:
        return [int.bit_count(i) for i in range(n+1)]