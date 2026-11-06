class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMax, localMin, globalMax = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            localMax, localMin = (
                max(nums[i], nums[i] * localMax, nums[i] * localMin),
                min(nums[i], nums[i] * localMax, nums[i] * localMin)
            )
            globalMax = max(localMax, globalMax)
        return globalMax