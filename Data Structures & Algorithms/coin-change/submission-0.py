class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = {0: 0} # start with the base case in cache
        def dfs(amount):
            if amount in dp: return dp[amount]
            if amount < 0: return float('inf')

            val = min([1 + dfs(amount - coins[i]) for i in range(n)])
            dp[amount] = val
            return val
    
        ans = dfs(amount)
        if ans == float('inf'):
            return -1
        else:
            return ans