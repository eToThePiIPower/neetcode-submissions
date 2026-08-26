class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(f"m:{mid}, l:{left}, r:{right}")
            if nums[mid] == target:
                return mid # target found at mid point
            if nums[mid] >= nums[left]:
                # left half sorted
                if target >= nums[left] and target <= nums[mid]:
                    # target in the left half
                    right = mid - 1
                else:
                    # target in the right half
                    left = mid + 1
            else:
                # right half is sorted
                if target >= nums[mid] and target <= nums[right]:
                    # target in the right half
                    left = mid + 1
                else:
                    # target in the left half
                    right = mid - 1
        return -1 # target never found