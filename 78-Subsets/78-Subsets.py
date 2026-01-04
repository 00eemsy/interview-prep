# Last updated: 1/4/2026, 3:07:10 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        res = []
4
5        def helper(i, curr):
6            if i == len(nums):
7                res.append(curr[::])
8                return
9            curr.append(nums[i])
10            helper(i+1, curr)
11            curr.pop()
12            helper(i+1, curr)
13
14        helper(0, [])
15        return res