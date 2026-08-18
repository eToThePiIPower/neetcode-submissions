class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break # everything is positive so now more triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue # no duplicate solutions

            l, r = i + 1, len(nums) - 1
            while (l < r): # no more solutions for this i
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l = l + 1
                if sum > 0:
                    r = r - 1
                if sum == 0:
                    if [nums[i], nums[l], nums[r]] not in triplets:
                        triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

        return triplets