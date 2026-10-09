class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        intervals = sorted(intervals)
        prevEnd = intervals[0][1]
        for idx in range(1, len(intervals)):
            if intervals[idx][0] >= prevEnd:
                prevEnd = intervals[idx][1]
            else:
                prevEnd = min(intervals[idx][1], prevEnd)
                removed += 1
        return removed