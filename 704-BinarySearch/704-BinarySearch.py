# Last updated: 12/23/2025, 4:09:20 PM
1import math
2
3class Solution:
4    def __init__(self):
5        self.zeroEquals = 0
6
7    def search(self, nums: List[int], target: int) -> int:
8        mid = math.floor(len(nums)//2)
9
10        if len(nums) == 0:
11            return -1
12        elif len(nums) == 1:
13            if nums[0] != target:
14                return -1
15            else:
16                return self.zeroEquals + mid
17        else:
18            if nums[mid] == target:
19                return self.zeroEquals + mid
20            elif nums[mid] < target:
21                self.zeroEquals += mid+1
22                return self.search(nums[mid+1:], target)
23            else:
24                return self.search(nums[0:mid], target)