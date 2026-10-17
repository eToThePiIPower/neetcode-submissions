class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] # early return for single house

        dfs_cache1 = [-1] * (len(nums) - 1)
        nums1 = nums[:-1]
        dfs_cache2 = [-1] * (len(nums) - 1)
        nums2 = nums[1:]

        def dfs(idx: int, nums, cache) -> int:
            if idx < 0 or idx >= len(nums): return 0
            elif cache[idx] != -1: return cache[idx]
            return max(nums[idx] + dfs(idx + 2, nums, cache), dfs(idx+1, nums, cache))
        
        for i in range(len(nums1) - 1, -1, -1):
            dfs_cache1[i] = dfs(i, nums1, dfs_cache1)
        for i in range(len(nums2) - 1, -1, -1):
            dfs_cache2[i] = dfs(i, nums2, dfs_cache2)

        return max(max(dfs_cache1), max(dfs_cache2))