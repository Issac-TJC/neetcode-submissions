class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            self.mp[key].append([value, timestamp])
        else:
            self.mp[key] = []
            self.mp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.mp:
            res = ""
            l = 0
            r = len(self.mp[key]) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if self.mp[key][mid][1] <= timestamp:
                    res = self.mp[key][mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        else:
            return ""
