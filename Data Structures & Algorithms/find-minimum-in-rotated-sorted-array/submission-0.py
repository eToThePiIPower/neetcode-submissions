class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            # we need to find when the rotated, sorted nums crossver to the lowest element
            if nums[left] < nums[right]:
                return nums[left] # crossover is at the first element
            
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                # crossover must be on the right, so move the left past the mid
                left = mid + 1 
            else:
                # start must be on the left, so move the right over
                right = mid
        
        return nums[left] # left and right crossed so only one more left