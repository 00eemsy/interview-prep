# Last updated: 1/2/2026, 1:15:24 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        return self.memoClimb(n)
4
5    def memoClimb(self, n, d = {}):
6        if n == 0 or n == 1:
7            return 1
8        elif n in d.keys():
9            return d[n]
10        else:
11            d[n] = self.memoClimb(n-1, d) + self.memoClimb(n-2, d)
12            return d[n]