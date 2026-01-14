# Last updated: 1/14/2026, 2:27:33 PM
1class TimeMap:
2
3    def __init__(self):
4        self.d = {}
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.d.keys():
8            self.d[key] = [[], {}]
9        
10        self.d[key][0].append(timestamp)
11        self.d[key][1][timestamp] = value
12
13    def get(self, key: str, timestamp: int) -> str:
14        # print('key: ' + key + ', timestamp: ' + str(timestamp))
15        if key not in self.d.keys():
16            return ''
17
18        if timestamp in self.d[key][1].keys():
19            return self.d[key][1][timestamp]
20
21        arr = self.d[key][0]
22        l = 0
23        r = len(arr) - 1
24
25        while l <= r:
26            mid = (l+r)//2
27            # print('l: ' + str(l) + ', r: ' + str(r) + ', mid: ' + str(arr[mid]))
28
29            if (arr[mid] < timestamp and mid == len(arr) - 1) or (arr[mid] < timestamp and arr[mid + 1] > timestamp):
30                return self.d[key][1][arr[mid]]
31            elif arr[mid] > timestamp:
32                r = mid - 1
33            else:
34                l = mid + 1
35
36        if l < 0 or r < 0:
37            return ''
38        else:
39            return self.d[key][1][arr[(l+r)//2]]
40
41
42# Your TimeMap object will be instantiated and called as such:
43# obj = TimeMap()
44# obj.set(key,value,timestamp)
45# param_2 = obj.get(key,timestamp)