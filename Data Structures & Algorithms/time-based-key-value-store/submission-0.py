class TimeMap:

    def __init__(self):
        self.mapp = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapp:
            self.mapp[key] = [(value, timestamp)]
        else:
            self.mapp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapp:
            return ""

        entries = self.mapp[key]
        l = 0
        r = len(entries) - 1
        while l <= r:
            mid = (l + r) // 2
            if entries[mid][1] == timestamp:
                return entries[mid][0]
            elif entries[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        
        # print(f'l: {l}, r: {r}, timestamp: {timestamp}, entries: {entries}')
        if l - 1 >= 0:
            return entries[l - 1][0]
        else:
            return ""
        
