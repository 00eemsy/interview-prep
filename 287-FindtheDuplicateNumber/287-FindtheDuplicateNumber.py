# Last updated: 12/26/2025, 5:14:16 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        s = set(nums)
4
5        for n in range(len(nums)):
6            if nums[n] in s:
7                s.remove(nums[n])
8            else:
9                return nums[n]