# Last updated: 1/6/2026, 3:31:28 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        ret = []
4
5        def helper(curr, i):
6            # print('curr: ' + str(curr) + ', i: ' + str(i))
7            if len(curr) == len(nums):
8                ret.append(curr[::])
9                return
10
11            temp = set(curr)
12
13            for j in range(len(nums)):
14                if j != i and nums[j] not in temp:
15                    curr.append(nums[j])
16                    helper(curr, j)
17                    curr.pop()
18
19        helper([], -1)
20        return ret