class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left, right = 0, 0
        while right < len(nums) - 1:
            jumps += 1
            new_right = right
            for j in range(left, right+1):
                new_right = max(new_right, j + nums[j])
            left, right = right + 1, new_right
        return jumps