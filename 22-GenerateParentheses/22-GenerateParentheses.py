# Last updated: 1/16/2026, 10:22:35 AM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        ret = []
4
5        def helper(curr, stock):
6            # print('curr: ' + str(curr) + ', stock: ' + str(stock))
7            if len(curr) == n*2:
8                ret.append(curr)
9                return
10            else:
11                for char in stock:
12                    # print('char: ' + str(char))
13                    if stock[char] > 0:
14                        # if ((char == '(') or 
15                        # (char == ')' and stock['('] > stock[')'])):
16                        if char == '(':
17                            stock[char] -= 1
18                            helper(curr + str(char), stock)
19                            stock[char] += 1
20                        elif char == ')' and stock['('] < stock[')']:
21                            stock[char] -= 1
22                            helper(curr + str(char), stock)
23                            stock[char] += 1
24
25        helper('', {'(': n, ')': n})
26        return ret