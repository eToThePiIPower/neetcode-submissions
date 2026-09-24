class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()

        def backtrack(current_sum: int, idx: int, current_nums: List[int] = []):
            # base cases
            if current_sum == target:
                results.append(list(current_nums))
                return
            
            # explore each decision
            for i in range(idx, len(nums)):
                if current_sum + nums[i] > target: break
                current_nums.append(nums[i])
                backtrack(current_sum + nums[i], i, current_nums)
                # Backtrack the last decision
                current_nums.pop()

        backtrack(0, 0)
        return results       