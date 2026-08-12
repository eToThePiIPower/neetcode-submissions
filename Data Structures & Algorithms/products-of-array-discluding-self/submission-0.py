import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        postfixes = [1] * len(nums)
        
        for i in range(1,len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i-1] 
        for i in reversed(range(len(nums)-1)):
            postfixes[i] = postfixes[i+1] * nums[i+1]
        
        return [x * y for x, y in zip(prefixes, postfixes)]