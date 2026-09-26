class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False
        for i in intervals:
            if inserted:
                result.append(i)
            else:
                if newInterval[1] < i[0]:
                    result.append(newInterval)
                    result.append(i)
                    inserted = True
                elif i[1] < newInterval[0]:
                    result.append(i)
                else:
                    newInterval[0] = min(newInterval[0], i[0])
                    newInterval[1] = max(newInterval[1], i[1])
        if not inserted: result.append(newInterval)
        return result