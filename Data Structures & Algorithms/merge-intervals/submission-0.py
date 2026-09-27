class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        r = []
        for i in intervals:
            if not r or i[0] > r[-1][1]:
                r.append(i)
            else:
                r[-1][1] = max(i[1], r[-1][1])
        return r