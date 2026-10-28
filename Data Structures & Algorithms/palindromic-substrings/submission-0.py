class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        # To get even and odd length intervals we'll double count range,
        # then floor-divide center and center + 1 by 2 (//2)
        # Even n will start at right == left     (an odd length)
        #  Odd n will start at right == left + 1 (an even length)
        for center in range(2 * n - 1):
            left = center // 2
            right = (center + 1) // 2
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
