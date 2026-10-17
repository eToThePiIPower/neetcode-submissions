class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] # early return for single house

        def dfs(idx: int, nums, cache) -> int:
            if idx < 0 or idx >= len(nums): return 0
            elif cache[idx] != -1: return cache[idx]
            return max(nums[idx] + dfs(idx + 2, nums, cache), dfs(idx+1, nums, cache))
        
        cache = [-1] * (len(nums) - 1)
        nums_t = nums[:-1]
        for i in range(len(nums_t) - 1, -1, -1):
            cache[i] = dfs(i, nums_t, cache)
        m1 = max(cache)

        cache = [-1] * (len(nums) - 1)
        nums_t = nums[1:]
        for i in range(len(nums_t) - 1, -1, -1):
            cache[i] = dfs(i, nums_t, cache)
        m2 = max(cache)

        return max(m1, m2)