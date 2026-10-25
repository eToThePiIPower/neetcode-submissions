class Solution:
    def countBits(self, n: int) -> List[int]:
        if n <= 0: return [0]

        bits = [0] * (n + 1)
        bits[1] = offset = 1

        for i in range(2, n + 1):
            if i == offset * 2:
                bits[i] = 1
                offset = i
            else:
                bits[i] = bits[i - offset] + 1
        
        return bits