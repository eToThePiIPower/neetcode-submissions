class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        current = [None] * n
        result = []

        def backtrack(idx: int):
            if idx >= n:
                result.append(current[:])
                return
            for i, num in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    current[idx] = num
                    backtrack(idx+1)
                    used[i] = False

        backtrack(0)
        return result