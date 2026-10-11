"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = sorted([i.start for i in intervals])
        endTimes   = sorted([i.end   for i in intervals])
        count, maxCount = 0, 0
        s, e = 0, 0
        while s < len(startTimes) and e < len(startTimes):
            if startTimes[s] < endTimes[e]:
                count += 1
                s += 1
                maxCount = max(count, maxCount)
            elif startTimes[s] == endTimes[e]:
                e += 1
                s += 1
            else:
                count -= 1
                e += 1
        return maxCount