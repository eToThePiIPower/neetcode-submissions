import heapq
class MedianFinder:

    def __init__(self):
        self.right = []
        self.left = []

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heapq.heappush_max(self.left, num)
        elif not self.right:
            if num > self.left[0]:
                heapq.heappush(self.right, num)
            else:
                v = heapq.heappop_max(self.left)
                heapq.heappush_max(self.left, num)
                heapq.heappush(self.right, v)
        # sides are equal, so easy to add
        elif len(self.left) == len(self.right):
            if num > self.left[0]:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush_max(self.left, num)
        # left (lower) side has 1 more, so possibly rebalance
        elif len(self.left) > len(self.right):
            if num >= self.left[0]:
                heapq.heappush(self.right, num)
            else:
                v = heapq.heappop_max(self.left)
                heapq.heappush_max(self.left, num)
                heapq.heappush(self.right, v)
        # right (higher) side has 1 more, so possibly rebalance
        else:
            if num <= self.right[0]:
                heapq.heappush_max(self.left, num)
            else:
                v = heapq.heappop(self.right)
                heapq.heappush(self.right, num)
                heapq.heappush_max(self.left, v)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return self.left[0]
        else:
            return self.right[0]
        