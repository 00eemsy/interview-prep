# Last updated: 12/26/2025, 4:51:59 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        curr = 0
4        prev = 0
5
6        if len(nums) == 1:
7            return nums[0]
8
9        while True:
10            if nums[curr-1] > nums[curr]:
11                return nums[curr]
12            elif nums[prev] > nums[curr]:
13                curr = prev + (curr-prev)//2
14            else:
15                prev = curr
16                curr += (len(nums)-curr)//2