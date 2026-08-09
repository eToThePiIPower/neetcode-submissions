class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ns = {}
        for i, num in enumerate(nums):
            diff = target - num
            j = ns.get(diff)
            if j is not None:
                return [j, i]
            ns[num] = i
