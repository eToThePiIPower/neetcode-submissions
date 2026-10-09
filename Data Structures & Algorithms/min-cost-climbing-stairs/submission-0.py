class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mins = [None] * (n+1)
        mins[0] = mins[1] = 0
        for i in range(2, n+1):
            mins[i] = min(mins[i-2] + cost[i-2], mins[i-1] + cost[i-1])
        return mins[n]
