from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeToEat(k: int) -> int:
            return sum(map(lambda pile: ceil(pile/k), piles))
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if timeToEat(mid) > h:
                low = mid + 1
            else:
                high = mid
        return low