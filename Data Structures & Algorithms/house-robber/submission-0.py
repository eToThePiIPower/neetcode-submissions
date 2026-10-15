class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dfs_cache = [None] * n

        def dfs(idx: int) -> int:
            if idx < 0 or idx >= n: return 0      
            elif dfs_cache[idx] is not None: return dfs_cache[idx]
            return max(nums[idx] + dfs(idx + 2), dfs(idx+1))
        
        for i in range(n-1,-1,-1):
            dfs_cache[i] = dfs(i)

        return max(dfs_cache)