# Last updated: 12/23/2025, 4:03:54 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        if len(prices) == 1:
4            return 0
5        
6        l = 0
7        r = 1
8
9        zuida = 0
10
11        while r < len(prices):
12            if prices[l] >= prices[r]:
13                if l < r:
14                    l += 1
15                else:
16                    r += 1
17            else:
18                if prices[r] - prices[l] > zuida:
19                    zuida = prices[r] - prices[l]
20                
21                r += 1
22
23        return zuida