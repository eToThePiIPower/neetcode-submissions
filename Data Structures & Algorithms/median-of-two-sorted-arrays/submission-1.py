class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m: return self.findMedianSortedArrays(nums2, nums1)

        lo, hi = 0, n
        while lo <= hi:
            mid1 = (lo + hi) // 2          # midpoint of lo & hi in nums1
            mid2 = (n + m + 1) // 2 - mid1  # remaining in nums2 must partition whole n + m
            
            # get values at left/right of the partition points
            l1 = (mid1 == 0) and float('-inf') or nums1[mid1 - 1]
            r1 = (mid1 == n) and float('inf') or nums1[mid1]
            l2 = (mid2 == 0) and float('-inf') or nums2[mid2 - 1]
            r2 = (mid2 == m) and float('inf') or nums2[mid2]

            # if a valid partition
            if l1 <= r2 and l2 <= r1:
                if (n + m) % 2 == 0: return (max(l1, l2) + min(r1, r2)) / 2.0
                else: return max(l1, l2)
            elif l1 > r2: hi = mid1 - 1
            else: lo = mid1 + 1
