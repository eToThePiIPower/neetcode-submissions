import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while stones and len(stones) > 1:
            bigger = heapq.heappop_max(stones)
            smaller = heapq.heappop_max(stones)
            if bigger > smaller:
                heapq.heappush_max(stones, bigger-smaller)
        return stones[0] if stones else 0