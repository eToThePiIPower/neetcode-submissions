import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for point in points:
            # sorting by dist^2 is same as by dist and saves a sqrt operation
            dist = point[0]**2 + point[1]**2
            if len(closest) >= k:
                heapq.heappushpop_max(closest, (dist, point))
            else:
                heapq.heappush_max(closest, (dist, point))
        return [p[1] for p in closest]