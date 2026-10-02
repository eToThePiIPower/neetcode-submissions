class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start_idx: int, current: List[int]):
            print(f"adding {current}")
            result.append(current[:])
            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i-1]:
                    print(f"skipping {nums[i]} in {current}")
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result