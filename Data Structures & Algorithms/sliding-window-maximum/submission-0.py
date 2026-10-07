import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(val, idx) for (idx, val) in enumerate(nums[:k])]
        heapq.heapify_max(heap)
        results = [heap[0][0]]
        for right in range(k, len(nums)):
            left = right - k + 1
            heapq.heappush_max(heap, (nums[right], right))
            while heap[0][1] < left: heapq.heappop_max(heap)
            results.append(heap[0][0])
        return results
