# Last updated: 2/2/2026, 9:28:41 AM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        b_str = bin(n)[2:]
4        count = 0
5
6        for bit in b_str:
7            if bit == '1':
8                count += 1
9
10        return count