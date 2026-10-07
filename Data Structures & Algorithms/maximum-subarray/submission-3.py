from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -inf
        currSum = 0
        left, right = 0, 0
        while right < len(nums):
            if maxSum < nums[right] < 0:
                maxSum = nums[right]
                left += 1
                currSum = 0
            elif currSum + nums[right] < 0:
                left += 1
                currSum = 0
            else:
                currSum += nums[right]
                maxSum = max(currSum, maxSum)
            right += 1
        return maxSum

