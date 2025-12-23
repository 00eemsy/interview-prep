# Last updated: 12/23/2025, 3:53:30 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        m = max(piles)
4
5        min_wrong = -1
6        mid = m//2
7
8        while True:
9            # go thru and calc # of moves req
10            print('mid: ' + str(mid))
11
12            if mid <= 0:
13                return 1
14
15            h_count = 0
16
17            for i in range(len(piles)):
18                h_count += piles[i]//mid
19
20                if piles[i] % mid != 0:
21                    h_count += 1
22
23            print('h_count: ' + str(h_count) + '\n')
24
25            # then check whether greater or less than target h
26            if h_count > h:
27                if min_wrong < mid:
28                    min_wrong = mid
29
30                if (m-mid)//2 == 0:
31                    mid = mid + 1
32                else:
33                    mid = mid + (m-mid)//2
34            else:
35                if mid - min_wrong == 1:
36                    return mid
37                
38                mid = mid - (mid - min_wrong)//2