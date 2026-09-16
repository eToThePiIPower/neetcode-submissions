class TimeMap:

    def __init__(self):
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store: return ""
        vals = self.store[key]

        low, high, pos = 0, len(vals) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if vals[mid][0] == timestamp:
                return vals[mid][1]
            elif vals[mid][0] <= timestamp:
                low = mid + 1
                pos = mid
            else:
                high = mid - 1
        if pos == -1: return ""
        return vals[pos][1]