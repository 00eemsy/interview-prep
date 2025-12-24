# Last updated: 12/23/2025, 4:08:25 PM
1class StackNode:
2    def __init__(self, val, index):
3        self.val = val
4        self.index = index
5        self.next = None
6
7class Stack:
8    def __init__(self):
9        self.top = None
10
11    def push(self, n):
12        n.next = self.top
13        self.top = n
14
15    def pop(self):
16        temp = self.top
17        self.top = temp.next
18
19        temp.next = None
20        return temp
21
22
23class Solution:
24    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
25        s = Stack()
26        ret = []
27
28        for i in range(len(temperatures)):
29            temp = temperatures[i]
30            curr = s.top
31
32            while curr != None and curr.val < temp:
33                ret[curr.index] = i - curr.index
34
35                s.pop()
36                curr = s.top
37
38            n = StackNode(temperatures[i], i)
39            s.push(n)
40            ret.append(0)
41
42        return ret
43