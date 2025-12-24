# Last updated: 12/23/2025, 4:03:26 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        heights = height
4        l = 0
5        r = len(heights) - 1
6
7        m = 0
8
9        while l < r:
10            xiao = min(heights[l], heights[r])
11            dist = (r-l) * xiao
12
13            if m < dist:
14                m = dist
15
16            if xiao == heights[l]:
17                l += 1
18            else:
19                r -= 1
20
21        return m