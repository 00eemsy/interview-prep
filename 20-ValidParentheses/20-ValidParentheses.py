# Last updated: 12/23/2025, 4:04:48 PM
1class Node:
2    def __init__(self, val, next=None):
3        self.val = val
4        self.next = next
5
6class Stack:
7    def __init__(self, top=None):
8        self.top = top
9    
10    def push(self, n: Node):
11        n.next = self.top
12        self.top = n
13
14    def pop(self):
15        to_pop = self.top
16
17        self.top = self.top.next
18
19        del to_pop
20
21class Solution:
22    def isValid(self, s: str) -> bool:
23        d = {'(': ')', '{': '}', '[': ']'}
24
25        tracker = Stack()
26
27        if s[0] not in d.keys():
28            return False
29        else:
30            tracker.top = Node(s[0])
31
32
33        i = 1
34
35        while i < len(s):
36            if s[i] in d.keys():
37                tracker.push(Node(s[i]))
38            else:
39                if tracker.top == None:
40                    return False
41                elif d[tracker.top.val] != s[i]:
42                    return False
43                else:
44                    tracker.pop()
45
46            i+=1
47
48        if tracker.top:
49            return False
50
51        return True