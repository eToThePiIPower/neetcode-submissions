class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ns = {}
        for i, num in enumerate(nums):
            if (target - num) in ns:
                return [ns[target - num], i]
            ns[num] = i
