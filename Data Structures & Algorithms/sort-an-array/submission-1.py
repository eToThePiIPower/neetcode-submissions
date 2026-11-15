from random import randint
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(low: int, high: int) -> int:
            nonlocal nums
            r = randint(low, high)
            nums[r], nums[high] = nums[high], nums[r]
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        def quickSort(low: int, high: int) -> None:
            nonlocal nums
            if low < high:
                part_idx = partition(low, high)
                quickSort(low, part_idx - 1)
                quickSort(part_idx + 1, high)

        quickSort(0, len(nums) - 1)
        return nums
         