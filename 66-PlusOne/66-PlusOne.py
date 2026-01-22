# Last updated: 1/22/2026, 12:30:06 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        s = 0
4
5        for n in digits:
6            # print('s in the making: ' + str(s))
7            s = s*10 + n
8
9        s += 1
10        # print('s: ' + str(s))
11
12        ret = []
13
14        while s > 0:
15            temp = s % 10
16            s = (s - temp)//10
17
18            ret.insert(0,temp)
19
20        return ret