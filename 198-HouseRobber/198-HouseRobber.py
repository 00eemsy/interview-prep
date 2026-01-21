# Last updated: 1/21/2026, 12:36:54 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        d = {0: nums[0]}
4
5        for i in range(1, len(nums)):
6            if i == 1:
7                d[1] = nums[1]
8            elif i == 2:
9                d[2] = nums[2] + nums[0]
10            else:
11                d[i] = nums[i] + max(d[i-2], d[i-3])
12
13        if len(nums) == 1:
14            return d[0]
15        else:
16            return max(d[len(nums)-1], d[len(nums)-2])