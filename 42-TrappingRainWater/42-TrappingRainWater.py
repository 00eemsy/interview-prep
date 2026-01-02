# Last updated: 1/2/2026, 12:19:35 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        l = 0
4        r = len(height) - 1
5        max_l = 0
6        max_r = 0
7        rain = 0
8
9        while l < r:
10            if height[l] < height[r]:
11                max_l = max(height[l], max_l)
12                rain += max_l - height[l]
13                l += 1
14            else:
15                max_r = max(height[r], max_r)
16                rain += max_r - height[r]
17                r -= 1
18
19        return rain